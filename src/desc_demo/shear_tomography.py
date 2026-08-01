"""Dark energy side: tomographic cosmic shear correlation functions.

Measures xi+/xi- in photo-z tomographic bins with TreeCorr, and compares
against LCDM theory curves (varying Omega_m and the dark energy equation of
state w0) generated with CCL -- LSST DESC's own Core Cosmology Library.
This is the same two-point-function approach behind DESC's 3x2pt cosmic
shear analysis; the growth-of-structure signal it measures is what
constrains dark energy.

Known simplification for this demo: the tomography field is centered on
the same cluster field used for the mass-mapping analysis (Phase 2) rather
than a cluster-masked "blank" field. A single moderate-mass cluster's extra
shear over a small patch is a minor, localized contaminant relative to the
degree-scale cosmic shear signal, but a production analysis would mask it.
"""
import numpy as np
import treecorr
from astropy.table import Table

from desc_demo.config import ClusterTarget


def assign_tomographic_bins(catalog: Table, z_edges) -> list:
    """Split a catalog into photo-z tomographic bins. Returns a list of sub-tables."""
    bins = []
    for z_lo, z_hi in zip(z_edges[:-1], z_edges[1:]):
        mask = (catalog["mean_z"] >= z_lo) & (catalog["mean_z"] < z_hi)
        bins.append(catalog[mask])
    return bins


def measure_shear_correlation(cat_i: Table, cat_j: Table, min_sep=2.0, max_sep=60.0,
                               nbins=12, flip_g2=False):
    """xi+/xi- between two tomographic bins (or the same bin for auto-correlation)."""
    tc_i = treecorr.Catalog(ra=cat_i["ra"], dec=cat_i["dec"], ra_units="deg", dec_units="deg",
                             g1=cat_i["g1"], g2=cat_i["g2"], flip_g2=flip_g2)
    tc_j = treecorr.Catalog(ra=cat_j["ra"], dec=cat_j["dec"], ra_units="deg", dec_units="deg",
                             g1=cat_j["g1"], g2=cat_j["g2"], flip_g2=flip_g2)

    gg = treecorr.GGCorrelation(min_sep=min_sep, max_sep=max_sep, nbins=nbins, sep_units="arcmin")
    gg.process(tc_i, tc_j)
    return {
        "theta_arcmin": np.exp(gg.meanlogr),
        "xip": gg.xip,
        "xim": gg.xim,
        "xip_err": np.sqrt(gg.varxip),
        "xim_err": np.sqrt(gg.varxim),
        "npairs": gg.npairs,
    }


def ccl_theory_xip(z_i, nz_i, z_j, nz_j, theta_deg, Omega_c=0.25, Omega_b=0.045,
                    h=0.7, n_s=0.965, sigma8=0.81, w0=-1.0, wa=0.0):
    """Predicted xi+(theta) for a bin pair, for a given LCDM/wCDM cosmology.

    dn/dz for each bin is the *measured* photo-z distribution of the
    catalog itself (not an idealized model), so the theory curve is a
    genuine prediction for this exact sample.
    """
    import pyccl as ccl

    cosmo = ccl.Cosmology(Omega_c=Omega_c, Omega_b=Omega_b, h=h, n_s=n_s, sigma8=sigma8,
                           w0=w0, wa=wa, transfer_function="eisenstein_hu")
    tracer_i = ccl.WeakLensingTracer(cosmo, dndz=(z_i, nz_i))
    tracer_j = ccl.WeakLensingTracer(cosmo, dndz=(z_j, nz_j))

    ell = np.geomspace(2, 20000, 300)
    cl = ccl.angular_cl(cosmo, tracer_i, tracer_j, ell)
    xip = ccl.correlation(cosmo, ell=ell, C_ell=cl, theta=theta_deg, type="GG+")
    return xip


def redshift_distribution(catalog: Table, n_hist_bins=30):
    """Histogram of mean_z for a catalog -- used as the CCL tracer's dn/dz."""
    counts, edges = np.histogram(catalog["mean_z"], bins=n_hist_bins, range=(0.0, 1.5))
    z_centers = 0.5 * (edges[:-1] + edges[1:])
    return z_centers, counts.astype(float)
