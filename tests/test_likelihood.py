import numpy as np
import pytest
from likelihood.likelihood_emulator import (
    window_stitching,
    vainshtein_suppression,
    combine_power_spectrum,
    compute_log_likelihood
)

def test_pipeline_execution():
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
    np.random.seed(42)
    d = P_model + 0.02 * P_model * np.random.normal(size=k.size)
    
    # 5. Covariâncias de observação e do emulador
    C_data = np.diag((0.02 * P_model) ** 2)
    sigma_R2 = (0.01 * np.ones_like(k)) ** 2  # 1% de incerteza do emulador
    
    # 6. Avaliação da Log-Verossimilhança
    lnL = compute_log_likelihood(d, P_model, C_data, sigma_R2, P_LCDM)
    
    # Validações
    assert np.isfinite(lnL), "lnL deve retornar um valor finito válido."
    assert lnL < 0, "Log-likelihood gaussiana deve ser um número real."
    print(f"\nTeste concluído com sucesso! Log-likelihood computada: {lnL:.4f}")

if __name__ == "__main__":
    test_pipeline_execution()
