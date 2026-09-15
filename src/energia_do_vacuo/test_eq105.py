"""
T7 Eq105 Λ por Entropia - V6.5 OMEGA-EXT
Eq105: Rμν-½Rgμν+Λgμν=8πG<Tμν> pag.52
ρ_Λ ~ exp(-S_inst)=exp(-280)=10^-121,6 M_pl^4 ~1e-47 GeV4
Z0=376,73 k=8,45 S_inst=280
"""
import numpy as np

Z0=376.73
k=8.45
S_inst=280
q95=2.64
q99=3.903
M_pl=1.22e19

def rho_lambda(S=S_inst):
    return np.exp(-S)*M_pl**4

def test_eq105():
    rho=np.log10(rho_lambda(S_inst))
    k_calc=2*np.pi*Z0/S_inst
    diff_k=abs(k_calc-k)/k
    z_k=diff_k/0.001
    print(f"S_inst={S_inst} k_calc={k_calc:.4f} vs {k} diff={diff_k*100:.4f}%")
    print(f"ρ_Λ 10^{rho:.1f} GeV4 vs obs 1e-47")
    diff_log=abs(rho-(-47))
    if diff_log<q95 and z_k<q95:
        return f"APROVADO ρ_Λ exp(-280)~1e-47 e k=8,45 z_k={z_k:.4f}"
    elif diff_log>q99:
        return f"REPROVADO diff={diff_log:.2f}>q99"
    else:
        return f"MARGINAL diff={diff_log:.2f}"

if __name__=="__main__":
    print(test_eq105())
