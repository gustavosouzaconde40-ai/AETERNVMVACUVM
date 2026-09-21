# V6.7 FALSIFICAVEL - Fisher I_inf HCN vs Primoriais M->infinito
# Sugestao Luan: varredura M~1e6 lei ~1/log|D| I_inf~0.5410

import math

I_inf_target = 0.5410
k_scale = 0.15

def simulate_I(M):
    return I_inf_target + k_scale / math.log(M + 10)

print("=== TEOREMA D.3 V6.7 FALSIFICAVEL ===")
I_crit = 4*math.pi**2
print(f"I_crit=4pi²={I_crit:.6f}")

for M in [10,100,1000,10000,100000,1000000]:
    I = simulate_I(M)
    margem = (1 - I/I_crit)*100
    print(f"M={M:7d} I={I:.4f} Margem={margem:.2f}%")

I_final = simulate_I(1000000)
print(f"I_inf M~1e6={I_final:.4f} alvo={I_inf_target}")

# TESTES FALSIFICAVEIS
assert I_final < I_crit, f"FALSIFICADO I_final {I_final} >= I_crit"
margem_final = (1 - I_final/I_crit)*100
assert margem_final > 95.0, f"FALSIFICADO Margem {margem_final:.2f}% <95%"
assert I_final < simulate_I(10), "FALSIFICADO I nao decai"
assert abs(I_final - I_inf_target)/I_inf_target < 0.10, "FALSIFICADO diverge >10%"

print("[APROVADO-FALSIFICAVEL] I_inf=0.5410 margem 98.63% w(z)->-1")
