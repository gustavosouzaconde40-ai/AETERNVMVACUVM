import numpy as np
import pytest

from likelihood.likelihood_emulator import (
    window_stitching,
    vainshtein_suppression,
    combine_power_spectrum,
    compute_log_likelihood
)


def test_pipeline_execution_basic_and_noise_monotonicity():
    """Teste de integridade do pipeline com dados sintéticos (mock)."""
    # 1. Escalas k simuladas (h/Mpc)
    k = np.logspace(-3, 1, 50)

    # 2. Janela e Supressão de Vainshtein
    W = window_stitching(k, k_match=0.1, delta_lnk=0.3)
    T = vainshtein_suppression(k, k_V=0.5, A=0.4, n=2.0)

    # 3. Espectro de potência mock (LCDM vs Modelo)
    P_LCDM = 1000.0 * (k / 0.05) ** (-2.0) / (1.0 + (k / 0.1) ** 2)
    R_em = T  # Razão simulada
    P_model = combine_power_spectrum(k, P_LCDM, R_em, W)

    # 4. Dados sintéticos com ruído de 2%
    rng = np.random.default_rng(seed=42)
    d = P_model + 0.02 * P_model * rng.normal(size=k.size)

    # 5. Covariâncias de observação e do emulador
    C_data = np.diag((0.02 * P_model) ** 2)
    sigma_R2 = (0.01 * np.ones_like(k)) ** 2  # 1% de incerteza do emulador (variância)

    # 6. Avaliação da Log-Verossimilhança
    lnL = compute_log_likelihood(d, P_model, C_data, sigma_R2, P_LCDM)

    # Validações
    assert isinstance(lnL, float)
    assert np.isfinite(lnL), "lnL deve retornar um valor finito válido."

    # Check monotonicity: adicionando ruído observacional esperamos lnL aumentar (menos negativo)
    C_data_noisier = np.diag((0.04 * P_model) ** 2)  # 4% noise
    lnL_noisier = compute_log_likelihood(d, P_model, C_data_noisier, sigma_R2, P_LCDM)
    assert lnL_noisier > lnL, "Com ruído maior a log-likelihood deve aumentar (valor menos informativo)."


def test_pipeline_pca_low_rank_branch():
    """Testa o caminho PCA / low-rank (Woodbury) na computação da verossimilhança."""
    k = np.logspace(-3, 1, 60)
    W = window_stitching(k, k_match=0.12, delta_lnk=0.25)
    T = vainshtein_suppression(k, k_V=0.4, A=0.5, n=3.0)
    P_LCDM = 800.0 * (k / 0.05) ** (-1.9) / (1.0 + (k / 0.12) ** 1.8)
    P_model = combine_power_spectrum(k, P_LCDM, T, W)

    rng = np.random.default_rng(seed=123)
    d = P_model + 0.015 * P_model * rng.normal(size=k.size)

    C_data = np.diag((0.015 * P_model) ** 2)

    # Construir uma aproximação low-rank para C_emu_R:
    r = 5
    X = rng.normal(size=(k.size, r))
    Q, _ = np.linalg.qr(X)
    pca_components = Q[:, :r]
    pca_var = np.logspace(-4, -6, r)

    lnL_pca = compute_log_likelihood(d, P_model, C_data,
                                     C_emu_R=None, D_diag=P_LCDM,
                                     pca_components=pca_components,
                                     pca_var=pca_var)

    assert isinstance(lnL_pca, float)
    assert np.isfinite(lnL_pca)


def test_full_covariance_and_error_handling():
    """Cobre o ramo de covariância full 2D e casos de erro de input."""
    k = np.logspace(-3, 1, 40)
    W = window_stitching(k, k_match=0.08, delta_lnk=0.28)
    T = vainshtein_suppression(k, k_V=0.6, A=0.35, n=2.5)
    P_LCDM = 900.0 * (k / 0.05) ** (-2.05) / (1.0 + (k / 0.11) ** 2)
    P_model = combine_power_spectrum(k, P_LCDM, T, W)

    rng = np.random.default_rng(seed=7)
    d = P_model + 0.01 * P_model * rng.normal(size=k.size)
    C_data = np.diag((0.01 * P_model) ** 2)

    # Construir C_emu_R full (simples SPD matriz com decaimento exponencial)
    N = k.size
    base = np.exp(-0.5 * (np.subtract.outer(np.log(k), np.log(k)))**2 / (0.5**2))
    # escalar para variâncias pequenas
    C_emu_R_full = 1e-4 * base
    # garantir SPD (valores na diagonal maiores)
    C_emu_R_full.flat[::N+1] += 1e-6

    lnL_full = compute_log_likelihood(d, P_model, C_data, C_emu_R_full, P_LCDM)
    assert isinstance(lnL_full, float)
    assert np.isfinite(lnL_full)

    # Teste de erro: comprimento incompatível para C_emu_R 1D
    sigma_bad = np.ones(N - 1)
    with pytest.raises(ValueError):
        _ = compute_log_likelihood(d, P_model, C_data, sigma_bad, P_LCDM)

    # Teste de erro: C_data com shape errado
    with pytest.raises(ValueError):
        _ = compute_log_likelihood(d, P_model, np.zeros((N-1, N-1)), sigma_bad, P_LCDM)
        

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
