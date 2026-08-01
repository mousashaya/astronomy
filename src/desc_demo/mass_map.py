"""Dark matter side: reconstruct cluster mass from weak lensing shear.

Two independent looks at the same catalog:
  - `fit_cluster_mass`: quantitative NFW halo mass fit using CLMM (LSST
    DESC's own cluster-lensing package). Reproduces the DESC CLMM tutorial
    workflow on our TAP-fetched catalog.
  - `kaiser_squires_map`: a 2D projected-mass (convergence) map via the
    classic Kaiser & Squires (1993) FFT inversion, for a visual light-vs-mass
    comparison.
"""
import numpy as np
from astropy.table import Table

from desc_demo.config import ClusterTarget


def _select_background_galaxies(catalog: Table, cluster: ClusterTarget, z_max: float = 1.5) -> Table:
    """Quality + ellipticity + background-redshift cuts, per the CLMM tutorial."""
    good_e = catalog["g1"] ** 2 + catalog["g2"] ** 2 <= 1.0
    background = (catalog["mean_z"] > (cluster.redshift + 0.1)) & (catalog["mean_z"] < z_max)
    return catalog[good_e & background]


def fit_cluster_mass(catalog: Table, cluster: ClusterTarget) -> dict:
    """NFW mass fit via CLMM, following the LSST DESC worked example."""
    import clmm
    import clmm.dataops as da
    from clmm import Cosmology
    from clmm.support.sampler import fitters

    galaxies = _select_background_galaxies(catalog, cluster)

    cosmo = Cosmology(H0=70.0, Omega_dm0=0.27 - 0.045, Omega_b0=0.045, Omega_k0=0.0)

    gcdata = clmm.GCData(
        [galaxies["ra"], galaxies["dec"], galaxies["g1"], galaxies["g2"],
         galaxies["mean_z"], np.arange(len(galaxies))],
        names=["ra", "dec", "e1", "e2", "z", "id"],
    )
    gc = clmm.GalaxyCluster(cluster.name, cluster.ra_deg, cluster.dec_deg, cluster.redshift, gcdata)
    gc.compute_tangential_and_cross_components()
    gc.make_radial_profile(
        bins=da.make_bins(0.2, 5.0, 7, method="evenlog10width"),
        bin_units="Mpc",
        cosmo=cosmo,
        include_empty_bins=False,
        gal_ids_in_bins=True,
    )

    concentration = 4.0
    z_inf = 1000
    beta_s = clmm.utils.compute_beta_s(gc.galcat["z"], cluster.redshift, z_inf, cosmo)
    bs_mean, bs2_mean = np.mean(beta_s), np.mean(beta_s**2)

    def predict(profile, logm):
        return clmm.compute_reduced_tangential_shear(
            r_proj=profile["radius"],
            mdelta=10**logm,
            cdelta=concentration,
            z_cluster=cluster.redshift,
            z_src=(bs_mean, bs2_mean),
            z_src_info="beta",
            approx="order1",
            cosmo=cosmo,
            delta_mdef=200,
            massdef="critical",
            halo_profile_model="nfw",
        )

    fit_data = gc.profile[gc.profile["n_src"] > 2]
    popt, pcov = fitters["curve_fit"](predict, fit_data, fit_data["gt"], fit_data["gt_err"], bounds=[10.0, 17.0])
    logm, logm_err = popt[0], np.sqrt(pcov[0][0])

    r_smooth = np.geomspace(fit_data["radius"].min(), fit_data["radius"].max(), 100)
    best_fit_gt = clmm.compute_reduced_tangential_shear(
        r_proj=r_smooth,
        mdelta=10**logm,
        cdelta=concentration,
        z_cluster=cluster.redshift,
        z_src=(bs_mean, bs2_mean),
        z_src_info="beta",
        approx="order1",
        cosmo=cosmo,
        delta_mdef=200,
        massdef="critical",
        halo_profile_model="nfw",
    )

    return {
        "logm": logm,
        "logm_err": logm_err,
        "m_msun": 10**logm,
        "m_msun_err": (10**logm) * logm_err * np.log(10),
        "n_source_galaxies": len(galaxies),
        "profile": gc.profile,
        "fit_data": fit_data,
        "best_fit_r_mpc": r_smooth,
        "best_fit_gt": best_fit_gt,
    }


def _tangent_plane(ra, dec, ra0, dec0):
    """Small-angle gnomonic (tangent plane) projection, in degrees -> arcmin, centered on the target."""
    d2r = np.pi / 180.0
    dx = (ra - ra0) * np.cos(dec0 * d2r) * 60.0
    dy = (dec - dec0) * 60.0
    return dx, dy


def kaiser_squires_map(catalog: Table, cluster: ClusterTarget, grid_size: int = 64,
                        fov_arcmin: float = None, smoothing_sigma_arcmin: float = 2.0) -> dict:
    """FFT-based Kaiser & Squires (1993) convergence map from a shear catalog.

    With only a few thousand source galaxies, the per-cell shear is
    shape-noise dominated (variance ~ sigma_e^2 / n_gal per cell) and the
    raw inversion is unusable — the reconstructed peak lands nowhere near
    the actual halo. Smoothing the shear field before inverting is the
    standard fix (e.g. Van Waerbeke 2000); it trades resolution for a
    smaller-variance map. Set `smoothing_sigma_arcmin=0` to disable.

    The TAP query pulls a *circular* footprint of radius `cluster.radius_deg`.
    If the square analysis grid is bigger than that circle inscribes, its
    corners have zero galaxies -> zero shear by construction, which is a
    sharp discontinuity that corrupts the FFT inversion (edge/Gibbs
    artifacts, often masquerading as a fake high-kappa peak at the grid
    edge). Default `fov_arcmin` keeps the square safely inside the circle.

    Returns a dict with the grid coordinates and the reconstructed
    convergence (projected mass) map.
    """
    if fov_arcmin is None:
        fov_arcmin = cluster.radius_deg * 60.0 * np.sqrt(2) * 0.85

    dx, dy = _tangent_plane(catalog["ra"], catalog["dec"], cluster.ra_deg, cluster.dec_deg)
    half = fov_arcmin / 2.0
    bins = np.linspace(-half, half, grid_size + 1)

    g1_sum, _, _ = np.histogram2d(dx, dy, bins=[bins, bins], weights=catalog["g1"])
    g2_sum, _, _ = np.histogram2d(dx, dy, bins=[bins, bins], weights=catalog["g2"])
    counts, _, _ = np.histogram2d(dx, dy, bins=[bins, bins])

    with np.errstate(invalid="ignore", divide="ignore"):
        g1_grid = np.where(counts > 0, g1_sum / counts, 0.0)
        g2_grid = np.where(counts > 0, g2_sum / counts, 0.0)

    if smoothing_sigma_arcmin > 0:
        from scipy.ndimage import gaussian_filter

        pixel_arcmin = fov_arcmin / grid_size
        sigma_pix = smoothing_sigma_arcmin / pixel_arcmin
        g1_grid = gaussian_filter(g1_grid, sigma=sigma_pix)
        g2_grid = gaussian_filter(g2_grid, sigma=sigma_pix)

    # The FFT treats the field as periodic, so real (non-periodic) data at
    # the edges wraps around and leaks into the inversion -- classically
    # showing up as a spurious high-|kappa| feature right at the border.
    # Zero-pad out to 2x the field before inverting, then crop back to the
    # original grid, so the wraparound lands in the padding instead of on
    # real data.
    pad = grid_size // 2
    n = grid_size + 2 * pad
    g1_padded = np.pad(g1_grid, pad)
    g2_padded = np.pad(g2_grid, pad)

    k = np.fft.fftfreq(n)
    k1, k2 = np.meshgrid(k, k, indexing="ij")
    k_sq = k1**2 + k2**2
    k_sq[0, 0] = 1.0  # avoid divide-by-zero at the DC mode; kappa there is unconstrained anyway

    gamma_hat = np.fft.fft2(g1_padded + 1j * g2_padded)
    d_conj = (k1**2 - k2**2 - 2j * k1 * k2) / k_sq
    kappa_hat = d_conj * gamma_hat
    kappa_padded = np.fft.ifft2(kappa_hat).real
    kappa_padded[0, 0] = 0.0
    kappa = kappa_padded[pad:pad + grid_size, pad:pad + grid_size]

    return {
        "x_arcmin": 0.5 * (bins[:-1] + bins[1:]),
        "y_arcmin": 0.5 * (bins[:-1] + bins[1:]),
        "kappa": kappa,
        "galaxy_counts": counts,
    }
