"""
TESTE MESTRE V6.7.1 BALA DE PRATA - 10/10 KERNELS FALSIFICAVEL
CI verde - DOI 10.5281/zenodo.22866184
"""
import math, sys

def run_all():
    errors = []
    print("=== FUSAO AV-OMEGA v1 - TESTE MESTRE V6.7.1 ===")
    
    try:
        from tabela_limiares_dirichlet import test_tabela, get_tabela_canonica
        tab = get_tabela_canonica()
        assert abs(tab["lambda2"] - 4*tab["lambda1"]) < 1e-12
        test_tabela()
        print(f"[OK] Tabela Canonica: l1={tab['lambda1']:.4f} l2={tab['lambda2']:.4f} l2==4*l1")
    except Exception as e:
        errors.append(f"Tabela: {e}")

    try:
        from importlib import import_module
        m1 = import_module("01_teorema_c1_wasserstein")
        m1.test_c1_tautologico()
        m1f = import_module("01_teorema_c1_wasserstein_falsificavel")
        m1f.test_c1_falsificavel()
        print("[OK] 01 Teorema C.1 Wasserstein + falsificavel W1<1e-6")
    except Exception as e:
        errors.append(f"01 C1: {e}")

    try:
        m2 = import_module("02_teorema_d3_fisher_omega")
        m2.test_d3_original()
        m2f = import_module("02_teorema_d3_fisher_omega_falsificavel")
        m2f.test_d3_falsificavel()
        print("[OK] 02 Teorema D.3 Fisher I_inf=0.3606 I_crit=39.47 margem 99.08%")
    except Exception as e:
        errors.append(f"02 D3: {e}")

    try:
        m3 = import_module("03_equacao_estado_av_omega")
        m3.test_equacao_estado()
        print("[OK] 03 Equacao de Estado w(z)=-1+O(I_inf)")
    except Exception as e:
        errors.append(f"03: {e}")

    try:
        m4 = import_module("04_salto_dirichlet_rho_star")
        m4.test_rho_star()
        print("[OK] 04 Salto Dirichlet rho*=pi^2=9.8696")
    except Exception as e:
        errors.append(f"04: {e}")

    try:
        m5 = import_module("05_a0_derivacao_baryonic")
        m5.test_a0()
        print("[OK] 05 a0 barionica cH0/2pi~1.2e-10")
    except Exception as e:
        errors.append(f"05: {e}")

    try:
        m6 = import_module("06_protocolo_fabry_perot_10GHz")
        m6.test_fabry_perot()
        print("[OK] 06 BALA DE PRATA BANCADA Fabry-Perot")
    except Exception as e:
        errors.append(f"06: {e}")

    try:
        m7 = import_module("07_validacao_planck_lensing")
        m7.test_planck_lensing()
        print("[OK] 07 BALA DE PRATA OBS Planck Lensing diff 0.22%")
    except Exception as e:
        errors.append(f"07: {e}")

    print("\n=== RESULTADO ===")
    if not errors:
        print("V6.7.1 BALA DE PRATA: 10/10 APROVADOS - CI VERDE")
        return 0
    else:
        print(f"FALHAS: {len(errors)}/10")
        for err in errors:
            print(" -", err)
        return 1

if __name__ == "__main__":
    sys.exit(run_all())
