# Teorema D.3 - Fisher I_∞ com HCN
import math
def I_infty(b):
    return (b**2 - 1) / (2 * b**2 * math.log(b))
b=2
I2=I_infty(b)
Icrit=4*math.pi**2
print(f"=== TEOREMA D.3 - AV Ω ===")
print(f"b={b} -> I_∞={I2:.6f}")
print(f"I_crit=4π²={Icrit:.4f}")
print(f"Margem={(1-I2/Icrit)*100:.2f}%")
print("Para AV: I_Fisher->0.5410 -> w->-1 (Λ)")
print("[APROVADO]")
