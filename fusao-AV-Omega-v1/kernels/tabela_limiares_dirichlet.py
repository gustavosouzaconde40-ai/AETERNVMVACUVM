"""
Tabela Canônica - Resolução π² vs 4π² (NOVO V6.7)
λ1 = π² = ρ* = colapso de fase χk -> χk+1
λ2 = 4π² = I_crit = ruptura T² Cb=[1,b)
Teste: assert λ2 == 4*λ1
DOI: 10.5281/zenodo.22866184
"""
import math

def get_tabela_canonica():
    pi = math.pi
    lambda1 = pi**2
    lambda2 = 4 * pi**2
    return {
        "lambda1": lambda1,
        "lambda2": lambda2,
        "rho_star": lambda1,
        "I_crit": lambda2,
        "pi2": pi**2,
        "4pi2": 4*pi**2
    }

def test_tabela():
    t = get_tabela_canonica()
    assert abs(t["lambda2"] - 4*t["lambda1"]) < 1e-12
    assert abs(t["rho_star"] - 9.869604401089358) < 1e-6
    return True
