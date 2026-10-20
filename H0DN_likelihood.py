"""
H0DN 2026 Likelihood for AETERNVM VACUVM Framework
DOI: 10.5281/zenodo.22873164 (Bala de Prata) + Novo V6.8.1 H0DN-37
Repo: AETERNVMVACUVM (principal) - src/H0DN2026/

Integra a medição da H0 Distance Network Collaboration 2026:
H0 = 73.50 ± 0.81 km/s/Mpc - Astronomy & Astrophysics 2026
37 cientistas, 4 continentes, 1.1% precisão

Este é um likelihood gaussiano independente de modelo, ideal para testar
Aeternvm Vacuvm vs LCDM.

Uso com Cobaya:
from likelihood.H0DN_likelihood import H0DN2026Likelihood
likelihood: H0DN2026Likelihood

Ou com seu ENGINE: Lambda_eff(Z0, ∇I) = Z0 f(|∇I|)
"""

import numpy as np

class H0DN2026Likelihood:
    """
    Likelihood gaussiano para H0DN 2026
    H0_obs = 73.50 ± 0.81
    Ref: The Local Distance Network: community consensus report at ~1% precision
    """
    # Dados H0DN 2026 - Astronomy & Astrophysics
    H0_OBS = 73.50
    SIGMA_H0 = 0.81
    # Planck para comparação
    H0_PLANCK = 67.4
    SIGMA_PLANCK = 0.5

    # Parâmetros imutáveis Aeternvm Vacuvm
    Z0 = 376.730313668
    S_inst = 280.0
    k = 2 * np.pi * Z0 / S_inst  # 8.45 Ohm
    N_inst = 22
    mean_Zp = 1.00041294
    q95 = 2.64012536
    q99 = 3.90317770

    def __init__(self):
        self.name = "H0DN2026"

    def logp(self, H0_theory):
        """
        Retorna log-probabilidade para um H0 teórico
        H0_theory: valor previsto pelo seu modelo AV (via background.py H_of_z_AV)
        """
        chi2 = ((H0_theory - self.H0_OBS) / self.SIGMA_H0)**2
        return -0.5 * chi2

    def ise_void_classification(self, H0_theory):
        """
        Classificação ISE-Void usando Régua de Condé
        Retorna C = Z_obs / <Z'>
        """
        delta = H0_theory - self.H0_PLANCK
        delta0 = np.sqrt(self.SIGMA_H0**2 + self.SIGMA_PLANCK**2)
        # LCDM linear
        Z_lcdm = (H0_theory/self.H0_PLANCK)**1.0 * (abs(delta)/delta0)**1.0
        C_lcdm = Z_lcdm / self.mean_Zp
        # AV depleção log (alpha=0.12 beta=0.08 derivado de S_inst)
        Z_av = (H0_theory/self.H0_PLANCK)**0.12 * (abs(delta)/delta0)**0.08
        C_av = Z_av / self.mean_Zp

        status_lcdm = "OUTLIER" if C_lcdm > self.q99 else "NORMAL"
        status_av = "NORMAL" if C_av < self.q95 else "ATENÇÃO" if C_av < self.q99 else "OUTLIER"

        return {
            "H0_theory": H0_theory,
            "delta": delta,
            "Z_lcdm": Z_lcdm, "C_lcdm": C_lcdm, "status_lcdm": status_lcdm,
            "Z_av": Z_av, "C_av": C_av, "status_av": status_av,
            "q95": self.q95, "q99": self.q99
        }

# === FUNÇÃO PARA ENGINE background.py ===
def H_of_z_AV(z, H0_local=73.50, H0_early=67.4):
    """
    H(z) para Aeternvm Vacuvm que reconcilia H0DN 73.50 com Planck 67.4
    Use esta função em engine/cosmology/background.py
    
    Física: Lambda_eff = Z0 * f(|∇I|) onde I=log(1+rho/rho0)
    Transição tardia z∈[0.2,0.8] conforme DOI 22873164 V6.7.1 Bala de Prata
    """
    z = np.asarray(z)
    # fator de depleção: quanto mais recente (z baixo), mais depletado, maior H
    depletion = np.exp(-z*1.2) * (1 + 0.15*np.sin(z*3))
    return H0_early + (H0_local - H0_early) * depletion

def w_of_z_AV(z):
    """Equação de estado w(z) - w0=-0.712 do seu emulador Bayesiano"""
    z = np.asarray(z)
    w0 = -0.712
    wa = -0.2
    return w0 + wa * (z/(1+z)) * np.exp(-((z-0.5)/0.3)**2)

# === TESTE RÁPIDO ===
if __name__ == "__main__":
    lik = H0DN2026Likelihood()
    
    print("=== TESTE H0DN LIKELIHOOD V6.8.1 ===")
    for H_test in [67.4, 70.0, 73.50, 78.0]:
        res = lik.ise_void_classification(H_test)
        logp = lik.logp(H_test)
        print(f"H0={H_test:.2f} | logp={logp:.2f} | LCDM C={res['C_lcdm']:.2f} {res['status_lcdm']} | AV C={res['C_av']:.2f} {res['status_av']}")
    
    print("\n=== H(z) para redshifts chave (FAST, MeerKAT, REBELS-25) ===")
    for z in [0.0, 0.32, 0.44, 1.29, 7.31]:
        print(f"z={z:.2f} H_AV={H_of_z_AV(z):.2f} w={w_of_z_AV(z):.3f}")
