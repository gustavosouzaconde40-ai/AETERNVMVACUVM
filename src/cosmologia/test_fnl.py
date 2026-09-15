"""
T6 f_NL CMB - V6.5 OMEGA-EXT
Livro pag.55 7.3.1 Non-Gaussianity
Predicao f_NL^Omega=0,02% = erro centroide 1/ln2
"""
import numpy as np

q95=2.64
q99=3.903
f_NL_omega=0.0002

def test_fnl(obs=-0.9,sigma=5.1):
    diff=abs(obs-f_NL_omega)
    z=diff/sigma if sigma>0 else 0
    print(f"f_NL Omega={f_NL_omega*100:.3f}% obs={obs}±{sigma} z={z:.4f}")
    if z<1.0:
        return f"APROVADO f_NL 0,02% z={z:.4f}<q95"
    elif z>q99:
        return f"REPROVADO z={z:.4f}>q99"
    else:
        return f"MARGINAL z={z:.4f}"

if __name__=="__main__":
    print(test_fnl())
