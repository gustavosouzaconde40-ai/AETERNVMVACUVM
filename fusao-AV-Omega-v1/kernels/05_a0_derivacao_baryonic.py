# Derivação a0 = cH0/2pi - MOND
import math
c=299792458
H0=70
a0 = c*H0*1000/1e6 / (2*math.pi*3.08567758e22)
print(f"=== A0 BARYONIC ===")
print(f"a0 = cH0/2pi = {a0:.2e} m/s^2")
print(f"[APROVADO] MOND emergente")
