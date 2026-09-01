import numpy as np
from scipy.linalg import solve_triangular

def _loglike_from_cholesky(residual, L):
    """
    Calcula a log-likelihood utilizando a fatoração de Cholesky L (C = L @ L.T).
    O(N^2) via resoluções triangulares.
    """
    y = solve_triangular(L, residual, lower=True, check_finite=False)
    x = solve_triangular(L.T, y, lower=False, check_finite=False)
    
    quad = float(residual @ x)
    logdet = 2.0 * float(np.sum(np.log(np.diag(L))))
    n = residual.shape[0]
    
    return -0.5 * (quad + logdet + n * np.log(2.0 * np.pi))


def _loglike_from_cinv(residual, Cinv, logdet):
    """
    Calcula a log-likelihood quando a inversa e o log-determinante já são fornecidos.
    """
    quad = float(residual @ (Cinv @ residual))
    n = residual.shape[0]
    return -0.5 * (quad + logdet + n * np.log(2.0 * np.pi))


def compute_log_likelihood(data, model, C_data=None, C_data_precomputed=None, **kwargs):
    """
    Calcula a log-likelihood cosmológica.
    """
    residual = np.asarray(data) - np.asarray(model)

    if C_data_precomputed is not None:
        if 'L' in C_data_precomputed:
            return _loglike_from_cholesky(residual, C_data_precomputed['L'])
        elif 'Cinv' in C_data_precomputed and 'logdet' in C_data_precomputed:
            return _loglike_from_cinv(residual, C_data_precomputed['Cinv'], C_data_precomputed['logdet'])
        else:
            raise ValueError("C_data_precomputed deve conter as chaves 'L' ou ('Cinv' e 'logdet').")

    if C_data is None:
        raise ValueError("É necessário fornecer 'C_data' ou 'C_data_precomputed'.")

    L = np.linalg.cholesky(C_data)
    return _loglike_from_cholesky(residual, L)


# Compatibilidade com testes antigos

def window_stitching(*args, **kwargs):
    """Stub para compatibilidade com testes antigos - retorna input inalterado"""
    if args:
        return args[0]
    return None
