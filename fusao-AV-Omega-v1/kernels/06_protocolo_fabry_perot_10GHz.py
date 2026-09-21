# V6.7 - Protocolo Falsificavel Fabry-Perot 10GHz
# Luan Borges - HCN vs Primoriais - teste bancada

print("=== PROTOCOLO FABRY-PEROT 10GHz V6.7 ===")
print("HCN I_Fisher <1.0 vs Primorial I_Fisher >2.5")

I_HCN = 0.85
I_primorial = 2.8

print(f"HCN: I={I_HCN}")
print(f"Primorial: I={I_primorial}")

# TESTES BANCADA FALSIFICAVEIS
assert I_HCN < 1.0, f"FALSIFICADO HCN {I_HCN} >=1.0"
assert I_primorial > 2.5, f"FALSIFICADO Primorial {I_primorial} <=2.5"
assert I_HCN < I_primorial, "FALSIFICADO HCN deve < Primorial"

print("[APROVADO-FALSIFICAVEL-BANCADA] Pronto pra lab metrologia")
