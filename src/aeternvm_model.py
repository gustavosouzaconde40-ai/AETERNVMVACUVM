# AETERNVM VACUVM - Model & SPDE Core Components
import numpy as np
import math
from scipy.optimize import brentq

eps_regular = 1e-12

def psi_profile_func(Psi, eps=eps_regular):
    return -Psi * np.log(Psi + eps)


def solve_Psi0_from_I(I, Psi_upper_guess=None, n_grid=400):
    if I < 0:
        raise ValueError("I must be nonnegative.")
    if Psi_upper_guess is None:
        Psi_upper = max(1.0, I * 10.0 + 10.0)
    else:
        Psi_upper = Psi_upper_guess
    xs = np.linspace(0.0, Psi_upper, n_grid)
    fvals = psi_profile_func(xs)
    imax = int(np.argmax(fvals))
    Psi_star = xs[imax]
    fmax = fvals[imax]
    if I > fmax + 1e-14:
        return None, (Psi_star, fmax)

    def g(Psi):
        return psi_profile_func(Psi) - I

    a = 0.0 + 1e-16
    b = max(Psi_star, 1e-8)
    if g(b) < 0:
        b_search = Psi_upper * 10
        xs2 = np.linspace(Psi_star, b_search, n_grid)
        fvals2 = psi_profile_func(xs2)
        imax2 = int(np.argmax(fvals2))
        Psi_star2 = xs2[imax2]
        fmax2 = fvals2[imax2]
        if I > fmax2 + 1e-14:
            return None, (Psi_star2, fmax2)
        b = Psi_star2

    Psi0 = brentq(g, a, b)
    return float(Psi0), (Psi_star, fmax)


def mu_eff_of_I(I, mu0=0.8, gamma=1.0, Lambda0=0.0, alpha=2.0, beta=1.0):
    arg = 1.0 + beta * max(I, 0.0)
    return mu0 + gamma * (Lambda0 + alpha * math.log(arg))
