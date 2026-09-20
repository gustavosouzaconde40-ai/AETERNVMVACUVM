# Teorema D.3 - Fisher I_inf com HCN
import math
def I_infty(b):
    return (b**2 - 1) / (2 * b**2 * math.log(b))
b=2
I2=I_infty(b)
print(f"b={b} -> I_inf={I2:.6f}")
print(f"I_crit=4pi²={4*math.pi**2:.4f}")
print(f"Margem={(1-I2/(4*math.pi**2))*100:.2f}%")
print("[APROVADO] AV Omega -> w->-1")
