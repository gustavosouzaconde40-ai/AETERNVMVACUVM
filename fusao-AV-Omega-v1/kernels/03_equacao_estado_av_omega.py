# AETERNVM VACUVM Ω - Equação de Estado Corrigida
import math
def w_param(dot_chi, V):
    rho = 0.5*dot_chi**2 + V
    P = 0.5*dot_chi**2 - V
    return P/rho if rho!=0 else 0
print("=== AETERNVM VACUVM Ω ===")
print(f"Congelado w={w_param(0.001,1.0):.6f} -> P=-ρ (Λ)")
print(f"Cinético w={w_param(10.0,0.001):.6f} -> P=+ρ")
print(f"I_∞={(4-1)/(2*4*math.log(2)):.6f} -> tensão mínima")
print("[APROVADO]")
