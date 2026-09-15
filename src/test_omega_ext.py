"""
Teste Mestre V6.5 OMEGA-EXT - Roda T5+T6+T7
AETERNVMVACUVM Framework Completo
"""
import sys
sys.path.append('.')

print("="*60)
print("AETERNVMVACUVM V6.5 OMEGA-EXT - VALIDAÇÃO COMPLETA")
print("="*60)

# T5 - Sensores Quânticos Eq103
print("\n[T5] Sensores Quânticos - Eq103 k=8,45")
try:
    from sensores_quânticos.test_eq103 import test_eq103
    result_t5 = test_eq103()
    print(f" -> {result_t5}")
    t5_ok = "APROVADO" in result_t5
except Exception as e:
    print(f" ERRO T5: {e}")
    t5_ok = False

# T6 - Cosmologia f_NL
print("\n[T6] Cosmologia - f_NL=0,02%")
try:
    from cosmologia.test_fnl import test_fnl
    result_t6 = test_fnl()
    print(f" -> {result_t6}")
    t6_ok = "APROVADO" in result_t6
except Exception as e:
    print(f" ERRO T6: {e}")
    t6_ok = False

# T7 - Energia do Vácuo Eq105
print("\n[T7] Energia do Vácuo - Eq105 ρ_Λ exp(-280)")
try:
    # tenta com acento e sem acento
    try:
        from energia_do_vácuo.test_eq105 import test_eq105
    except:
        import importlib
        mod = importlib.import_module("energia_do_vácuo.test_eq105")
        test_eq105 = mod.test_eq105
    result_t7 = test_eq105()
    print(f" -> {result_t7}")
    t7_ok = "APROVADO" in result_t7
except Exception as e:
    print(f" ERRO T7: {e}")
    t7_ok = False

print("\n" + "="*60)
total = sum([t5_ok, t6_ok, t7_ok])
if total == 3:
    print(f"V6.5 OMEGA-EXT: {total}/3 APROVADOS - RELEASE LIBERADA! 🚀")
else:
    print(f"V6.5 OMEGA-EXT: {total}/3 APROVADOS - REVISAR")
print("="*60)
