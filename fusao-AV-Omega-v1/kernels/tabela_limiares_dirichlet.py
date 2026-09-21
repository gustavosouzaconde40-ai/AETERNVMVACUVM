import math
def lambda_n(b, n):
    return (n**2 * math.pi**2) / ((b-1)**2)

print("=== TABELA CANONICA DIRICHLET ===")
for b in [2,3,10]:
    l1 = lambda_n(b,1)
    l2 = lambda_n(b,2)
    print(f"b={b}: λ1={l1:.6f} | λ2={l2:.6f}")

b=2
lam1 = lambda_n(b,1)
lam2 = lambda_n(b,2)
assert lam2 == 4*lam1, "Falsificado"
assert abs(lam1 - math.pi**2) < 1e-9
assert abs(lam2 - 4*math.pi**2) < 1e-9
print("[APROVADO-FALSIFICAVEL] λ1=π² colapso fase, λ2=4π² ruptura T²")
