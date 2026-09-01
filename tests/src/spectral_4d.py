# AETERNVM VACUVM - 4D Spectral Grids & FFT Helpers
import numpy as np
from numpy.fft import fftfreq

def build_k_arrays(N, L, adv_vec=np.array([1.0, 0.0, 0.0, 0.0])):
    freqs = fftfreq(N, d=L / N)
    ang = 2.0 * np.pi * freqs
    k0, k1, k2, k3 = np.meshgrid(ang, ang, ang, ang, indexing='ij')
    ksq = k0**2 + k1**2 + k2**2 + k3**2
    adv_mult = adv_vec[0]*k0 + adv_vec[1]*k1 + adv_vec[2]*k2 + adv_vec[3]*k3
    return ksq, adv_mult


def compute_Khat_from_ksq(ksq, kappa0=2.0, s=1.5, q0=1e-3, eps_regular=1e-12):
    kpow = np.power(ksq + eps_regular, 0.5 * s)
    Khat = kappa0 / (kpow + q0)
    return Khat
