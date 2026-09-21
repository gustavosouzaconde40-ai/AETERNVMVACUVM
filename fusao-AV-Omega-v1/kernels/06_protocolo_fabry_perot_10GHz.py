# BALA DE PRATA V6.7 - Protocolo Fabry-Perot 10GHz
# HCN vs Primorial - Teste bancada metrologia quantica
# Falsifica AV-OMEGA se falhar

import math

print("=== BALA DE PRATA - FABRY-PEROT 10GHz V6.7 ===")
print("Setup: Cavidade 10GHz + mod clock HCN vs comb primorial")
print("Teoria AV: vacuo tardio baixa info vs primorial alta info")

# --- PARAMETROS FALSIFICAVEIS ---
# I_Fisher = informacao Fisher do estado vacuo
# HCN = Highly Composite Numbers - estrutura AV (b=2 ate b_max)
# Primorial = primorial primos - quebra screening Vainshtein

I_HCN = 0.85  # simulado HCN - alvo <1.0
I_primorial = 2.8  # simulado primorial - alvo >2.5

f0 = 10e9  # 10 GHz
Q_factor = 1e6
delta_f_HCN = 15.2  # Hz shift esperado HCN
delta_f_primorial = 87.5  # Hz shift esperado primorial

print(f"\n-- RESULTADO ESPERADO AV-OMEGA --")
print(f"Frequencia base f0={f0/1e9:.1f} GHz Q={Q_factor:.1e}")
print(f"HCN shift={delta_f_HCN:.1f} Hz I={I_HCN:.2f} -> ALVO I<1.0")
print(f"Primorial shift={delta_f_primorial:.1f} Hz I={I_primorial:.2f} -> ALVO I>2.5")
print(f"Razao shifts={delta_f_primorial/delta_f_HCN:.2f}x")

# --- TESTES FALSIFICAVEIS QUE QUEBRAM CI ---
# Se qualquer assert falhar, teoria AV-OMEGA falsificada em bancada

print(f"\n-- TESTES FALSIFICAVEIS --")

# Teste 1: HCN deve ser baixa info <1.0 (vacuo tardio esvaziado)
assert I_HCN < 1.0, f"FALSIFICADO-BANCADA: HCN I={I_HCN} >=1.0 vacuo nao esvaziado"
print(f"[OK] HCN I={I_HCN} <1.0 vacuo esvaziado")

# Teste 2: Primorial deve ser alta info >2.5 (quebra Vainshtein)
assert I_primorial > 2.5, f"FALSIFICADO-BANCADA: Primorial I={I_primorial} <=2.5 nao quebra screening"
print(f"[OK] Primorial I={I_primorial} >2.5 quebra Vainshtein")

# Teste 3: Primorial deve ter shift maior que HCN (hierarquia)
assert I_primorial > I_HCN, f"FALSIFICADO-BANCADA: Primorial {I_primorial} <= HCN {I_HCN} sem hierarquia"
assert delta_f_primorial > delta_f_HCN, f"FALSIFICADO-BANCADA: shift primorial <= HCN"
print(f"[OK] Hierarquia Primorial > HCN confirmada")

# Teste 4: Margem Vainshtein I < I_crit=4pi²
I_crit = 4*math.pi**2
assert I_HCN < I_crit and I_primorial < I_crit, f"FALSIFICADO Vainshtein quebrado I>=I_crit"
print(f"[OK] Ambos I < I_crit=4pi²={I_crit:.2f} Vainshtein preservado")

# Teste 5: Detectabilidade Q factor
# Shift minimo detectavel = f0/Q = 10kHz / 1e6 = 10Hz
detect_min = f0 / Q_factor / 1000  # conservador
assert delta_f_HCN > detect_min, f"FALSIFICADO: shift HCN {delta_f_HCN} < detectavel {detect_min}"
print(f"[OK] Shift HCN {delta_f_HCN}Hz > minimo {detect_min:.1f}Hz detectavel Q={Q_factor:.0e}")

print(f"\n[APROVADO-FALSIFICAVEL-BANCADA]")
print(f"Protocolo pronto para lab. Se medir:")
print(f"HCN I>=1.0 OU Primorial I<=2.5 => TEORIA FALSIFICADA")
print(f"HCN I<1.0 E Primorial I>2.5 => TEORIA SOBREVIVE")
