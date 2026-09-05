# AETERNVMVACUVM Framework

Open-Source Computational Framework for Late-Time Vacuum Phase Transitions, Vainshtein Screening, and Cosmological MCMC Emulators.

[![DOI Concept](https://zenodo.org/badge/DOI/10.5281/zenodo.21856036.svg)](https://doi.org/10.5281/zenodo.21856036)
[![DOI v1.1.0](https://zenodo.org/badge/DOI/10.5281/zenodo.22166663.svg)](https://doi.org/10.5281/zenodo.22166663)
[![DOI v5.0 5-PROVAS](https://zenodo.org/badge/DOI/10.5281/zenodo.22347657.svg)](https://doi.org/10.5281/zenodo.22347657)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## CADEIA COMPLETA AETERNVM VACVVM - 5 DOIs ATIVOS ✅

**DOI 1 - Regua de Conde:** [10.5281/zenodo.22096687](https://doi.org/10.5281/zenodo.22096687)
**DOI 2 - Triangulo de Conde:** [10.5281/zenodo.22164502](https://doi.org/10.5281/zenodo.22164502) + backup [10.5281/zenodo.22165628](https://doi.org/10.5281/zenodo.22165628)
**DOI 3 - VIEC Mk.IV-C Zbites:** [10.5281/zenodo.22165507](https://doi.org/10.5281/zenodo.22165507)
**DOI 4 - Framework Completo:** [10.5281/zenodo.22166663](https://doi.org/10.5281/zenodo.22166663) (v1.1.0-complete)
**DOI 5 - 5 PROVAS v5.0 FINAL:** [10.5281/zenodo.22347657](https://doi.org/10.5281/zenodo.22347657) - Z0=376.73 Ohm=1, k=8.45 Ohm, S=280, N=22, PD=0.556, Delta=6.46
**DOI Pai (todas as versoes):** [10.5281/zenodo.21856036](https://doi.org/10.5281/zenodo.21856036)

## Visao geral

AETERNVMVACUVM e um motor de fisica de codigo aberto e um conjunto de ferramentas de emulacao cosmologica projetado para testar teorias de campos escalares-tensoriais de acoplamento nao minimo, mecanismos de blindagem de Vainshtein e transicoes de fase do vacuo em tempos tardios (z em [0.2, 0.8]) contra observacoes cosmologicas de precisao.

Ele integra diretamente solucionadores de sistemas hiperbolicos com pipelines de inferencia Bayesiana usando emuladores EFTCAMB, Cobaya e de Processo Gaussiano (GP).

## Arcabouco teorico v5.0 - Z0 como unidade

### Potential de Deplecao do Vacuo

$$V(\chi) = V_0 \left[1 - \exp\left(-\frac{\lambda \chi}{M_{Pl}}\right)\right]^2$$

$$V_0 = \frac{\hbar}{2 Z_0 c \ell_P^3} (1 - e^{-S_{inst}})$$

onde $S_{inst} \approx 280$ representa acao instanton nao-perturbativa. Isso gera $V_0 \sim 10^{-47} GeV^4$, batendo naturalmente com a densidade de energia escura observada sem fine-tuning.

### 5 Provas Convergentes (VACUO-ATIVO-5-PROVAS v5.0)

1. **JWST CEERS z>10:** lambda/M_Pl ~ (Z0/Z_Pl)^n e^-S/4 - consistente
2. **IXPE Magnetar 1E 1547.0-5408 15 bins:** `rvm_params_1e1547_15bins.csv` - PD=0.556 chi2=18.12/14 Delta=6.46 LIMITE forecast 23.0@500h - [Codigo AV_likelihood.py](https://github.com/gustavosouzaconde40-ai/VACUO-ATIVO-5-PROVAS/blob/main/probabilidade/AV_likelihood.py)
3. **LZ 2024:** xi ~ Z0 - limite
4. **Z0 como unidade:** k=8.45 derivado
5. **Forecast falsificavel:** Se 500h IXPE nao der Delta>9, Z0 refutado

**Status:** Ciclo metodologico fechado, comprovacao aberta - 05-09-2026 - ORCID 0009-0003-8264-7907

## Modulos-chave e arquitetura teorica

### 1. Dinamica do Vacuo e Acoplamento Nao Minimo

Resolve a equacao do campo hiperbolico com acoplamento de curvatura nao minima:

$$\Box \varphi + dV/d\varphi - \xi R \varphi = 0$$

usando integradores ODE/PDE adaptativos de alta precisao (LSODA / DOP853) com tolerancias ate rtol = 1e-10.

### 2. Mecanismo de triagem de Vainshtein

Calcula a supressao gravitacional efetiva dentro do Sistema Solar e em escalas astrofisicas locais para satisfazer limites rigorosos de gravidade local.

### 3. Pipeline Cosmologico de MCMC e Inferencia

- **Conjuntos de dados:** Suporte integrado para dados Planck CMB, DESI Y1/Y3, Pantheon+ e BAO.
- **Emulador Bayesiano:** Aceleracao de emuladores de Processos Gaussianos para reconstrucoes de equacao de estado w(z) (w0 = -0,712).
- **Tensao de Hubble:** preve transicoes tardias com resolucao da tensao H0 e 3-5% f8 supressao em vazios cosmicos.

## Estrutura do Repositorio
## Instalacao

```bash
pip install -e.
pip install -e.[test] # para desenvolvimento
pytest



