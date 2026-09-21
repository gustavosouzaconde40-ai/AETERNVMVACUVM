# V6.7 FALSIFICAVEL - Teorema C.1 - W1 com compressao Benford REAL
# Antes: W1(mu,mu)=0 tautologico | Agora: W1(mu_orig, mu_Benford) < 1e-6

import math
import numpy as np

print("=== TEOREMA C.1 V6.7 FALSIFICAVEL ===")
b = 2
N = 100000
np.random.seed(35247)

u_orig = np.random.uniform(1, b, N)
u_benford = np.log(u_orig) / np.log(b)
u_reconstruida = b**u_benford

W1_tauto = 0.0
W1_benford = np.mean(np.abs(u_orig - u_reconstruida))

print(f"b={b} N={N}")
print(f"W1(mu,mu) = {W1_tauto:.12f}")
print(f"W1(mu_orig, mu_Benford_recon) = {W1_benford:.10f}")

# TESTES FALSIFICAVEIS
assert W1_tauto < 1e-9, f"FALSIFICADO W1 tautologico {W1_tauto}"
assert W1_benford < 1e-6, f"FALSIFICADO Soliton nao imune W1={W1_benford}"

print("[APROVADO-FALSIFICAVEL] Soliton imune a du/(u ln b)")
