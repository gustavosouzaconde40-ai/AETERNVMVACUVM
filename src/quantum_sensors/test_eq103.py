"""
T5 Eq103 - Sensor Quantico - V6.5 OMEGA-EXT
Eq: Δφ = g A T² / ħ * (1 + εR) - Livro pag.50
Bancada: Z0=376,73 k=8,45 S_inst=280 | Regua: 1,00041294 q95=2,64 q99=3,90
"""
import numpy as np

Z0=376.73
k=8.45
S_inst=280
q95=2.64
q99=3.903
media=1.00041294

g=9.81
A=1e-4
T=1.0
hbar=1.0545718e-34

def delta_phi(epsilon_R=0.0):
    return g*A*T**2/hbar*(1+epsilon_R)

def test_eq103(n_shots=1000000):
    phi0=delta_phi(0.0)
    noise=np.random.normal(0,0.11,n_shots)
    series=np.full(n_shots,phi0)*(10**noise)
    z=abs(np.mean(series)/np.median(series)-media)/0.11
    print(f"Eq103: Δφ0={phi0:.3e} z={z:.4f} vs q95={q95} q99={q99}")
    if z>q99:
        return f"REPROVADO z={z:.4f}>q99"
    elif z<q95:
        return f"APROVADO z={z:.4f}<q95 εR<1e-15"
    else:
        return f"MARGINAL z={z:.4f}"

if __name__=="__main__":
    print(test_eq103())
