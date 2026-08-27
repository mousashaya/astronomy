"""Stage 5 of the SN Ia pipeline: turn a SALT2 fit into a standardized
distance modulus via the Tripp (1998) / Phillips formula. This is the
actual dark-energy measurement everything upstream has been building
toward — paired with redshift, it's one point on the Hubble diagram.

    mu = m_B - M_B + alpha * x1 - beta * c

m_B, x1, c come from Stage 4's fit. alpha, beta, and M_B below do NOT
come from our own data — they're fixed literature calibration constants,
derived by other analyses from much larger SN Ia samples (with
independent, e.g. Cepheid-based, distances). We're using them as given
external inputs, not deriving them ourselves — that's a real limitation
worth being upfront about, not something this pipeline currently solves.
Values roughly match what large low-z-anchored analyses (e.g. Betoule et
al. 2014, JLA) report; different analyses land on somewhat different
numbers, so these should be read as "a reasonable literature choice,"
not a universal constant.
"""
import math
from dataclasses import dataclass

from desc_demo.sn_fitting import FitResult

ALPHA = 0.14   # stretch-luminosity coefficient (brighter SNe decline slower)
BETA = 3.1     # color-luminosity coefficient (redder SNe are fainter/dustier)
M_B = -19.3    # fiducial SN Ia absolute B-band magnitude at peak


@dataclass
class DistanceResult:
    m_b: float
    mu: float
    mu_err: float


def standardize(fit: FitResult) -> DistanceResult:
    """Compute m_B from the fitted model (sncosmo's own synthetic
    photometry, not a hand-derived formula — see the module this was
    verified against in development) and apply the Tripp formula.
    """
    m_b = fit.model.source_peakmag("bessellb", "ab")

    x1 = fit.params["x1"]
    c = fit.params["c"]
    mu = m_b - M_B + ALPHA * x1 - BETA * c

    # m_B's own uncertainty, propagated from x0's fit error (verified
    # empirically against sncosmo's model during development — see
    # project notes): d(m_B)/d(x0) = -2.5 / (ln(10) * x0).
    x0 = fit.params["x0"]
    m_b_err = (2.5 / math.log(10)) * (fit.errors["x0"] / x0)

    # Standard quadrature sum, treating m_B, x1, c as independent. Real
    # analyses use the fit's full covariance matrix here (x1 and c are
    # not actually independent of each other or of x0) — this is a
    # simplification, consistent with everything else in this project
    # being a first-pass pipeline rather than a publication-grade one.
    mu_err = math.sqrt(
        m_b_err**2
        + (ALPHA * fit.errors["x1"]) ** 2
        + (BETA * fit.errors["c"]) ** 2
    )

    return DistanceResult(m_b=m_b, mu=mu, mu_err=mu_err)


def distance_modulus_to_gly(mu: float) -> float:
    """Convert a distance modulus to billions of light-years — purely
    for human-readable display (e.g. comparing against
    sn_discovery.naive_distance_gly's redshift-only estimate). The
    actual Hubble diagram stage will work in mu directly, the standard
    convention, not light-years — this is a grounding aid, same role as
    naive_distance_gly plays for raw redshift.

    mu = 5*log10(d_pc) - 5  =>  d_pc = 10^((mu+5)/5)
    """
    distance_pc = 10 ** ((mu + 5) / 5)
    distance_mpc = distance_pc / 1e6
    return distance_mpc * 3.2616e-3  # Mpc -> Gly, same constant as naive_distance_gly
