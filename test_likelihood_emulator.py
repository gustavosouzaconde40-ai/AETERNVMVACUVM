import numpy as np
from scipy.linalg import cholesky
import pytest
from probabilidade.likelihood_emulator import compute_log_likelihood

def _make_spd_matrix(n, seed=42):
    rng = np.random.default_rng(seed)
    A = rng.normal(size=(n, n))
    return A @ A.T + n * np.eye(n)

def test_loglike_precomputed_cholesky_matches_direct():
    n = 10
    C = _make_spd_matrix(n, seed=1)
    L = cholesky(C, lower=True)
    
    data = np.linspace(0.1, 1.0, n)
    model = np.zeros(n)
    
    ll_direct = compute_log_likelihood(data, model, C_data=C)
    ll_precomp = compute_log_likelihood(data, model, C_data_precomputed={'L': L})
    
    assert np.isclose(ll_direct, ll_precomp, atol=1e-10)

def test_loglike_precomputed_cinv_matches_direct():
    n = 10
    C = _make_spd_matrix(n, seed=2)
    Cinv = np.linalg.inv(C)
    _, logdet = np.linalg.slogdet(C)
    
    data = np.linspace(0.1, 1.0, n)
    model = np.zeros(n)
    
    ll_direct = compute_log_likelihood(data, model, C_data=C)
    ll_precomp = compute_log_likelihood(data, model, C_data_precomputed={'Cinv': Cinv, 'logdet': logdet})
    
    assert np.isclose(ll_direct, ll_precomp, atol=1e-10)

def test_invalid_precomputed_dict_raises_error():
    data = np.ones(5)
    model = np.zeros(5)
    with pytest.raises(ValueError, match="C_data_precomputed deve conter"):
        compute_log_likelihood(data, model, C_data_precomputed={'invalid_key': None})
