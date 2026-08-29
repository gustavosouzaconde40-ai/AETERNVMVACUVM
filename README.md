# AETERNVMVACUVM Framework

**Open-Source Computational Framework for Late-Time Vacuum Phase Transitions, Vainshtein Screening, and Cosmological MCMC Emulators.**

[[DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21856036.svg)](https://doi.org/10.5281/zenodo.21856036)
[[DOI v1.1.0-completo](https://zenodo.org/badge/DOI/10.5281/zenodo.22166663.svg)](https://doi.org/10.5281/zenodo.22166663)
[[License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

### ☕ APOIE A PESQUISA - PIX
**PIX (CPF): 022.818.517-37**
**PIX (Celular): 27 99817 4350**

### CADEIA COMPLETA AETERNVM VACVVM - 4 DOIs ATIVOS ✅

**DOI 1 - Régua de Condé:** [10.5281/zenodo.22096687](https://doi.org/10.5281/zenodo.22096687)
**DOI 2 - Triângulo de Condé:** [10.5281/zenodo.22164502](https://doi.org/10.5281/zenodo.22164502) + backup [10.5281/zenodo.22165628](https://doi.org/10.5281/zenodo.22165628)
**DOI 3 - VIEC Mk.IV-C Zbites:** [10.5281/zenodo.22165507](https://doi.org/10.5281/zenodo.22165507) - 10 arquivos com correção Crouzeix-Jin ||p(A)||≤2
**DOI 4 - Framework Completo:** [10.5281/zenodo.22166663](https://doi.org/10.5281/zenodo.22166663) (v1.1.0-completo - REPOSITÓRIO CORRIGIDO COM papel.bib, papel.md, pyproject.toml, setup.py)
**DOI Pai (todas as versões):** [10.5281/zenodo.21856036](https://doi.org/10.5281/zenodo.21856036)

## Visão geral

AETERNVMVACUVM é um motor de física de código aberto e um conjunto de ferramentas de emulação cosmológica projetado para testar teorias de campos escalares-tensoriais de acoplamento não mínimo, mecanismos de blindagem de Vainshtein e transições de fase do vácuo em tempos tardios (z ∈ [0.2, 0.8]) contra observações cosmológicas de precisão.

Ele integra diretamente solucionadores de sistemas hiperbólicos com pipelines de inferência Bayesiana usando emuladores EFTCAMB, Cobaya e de Processos Gaussianos (GP).

---

## Módulos-chave e arquitetura teórica

### 1. Dinâmica do Vácuo e Acoplamento Não Mínimo
Resolve a equação do campo hiperbólico com acoplamento de curvatura não mínima:
□φ + dV/dφ - 2ξRφ = 0 usando integradores ODE/PDE adaptativos de alta precisão (LSODA / DOP853) com tolerâncias até rtol = 1e-10.

### 2. Mecanismo de triagem de Vainshtein
Calcula a supressão gravitacional efetiva dentro do Sistema Solar e em escalas astrofísicas locais para satisfazer limites rigorosos de gravidade local, permitindo ao mesmo tempo desvios cosmológicos.

### 3. Pipeline Cosmológico de MCMC e Inferência
* **Conjuntos de dados:** Suporte integrado para dados Planck CMB, DESI Y1/Y3, Pantheon+ e BAO.
* **Emulador Bayesiano:** Aceleração de emuladores de Processos Gaussianos para reconstruções de equação de estado w(z) (w0 = -0,712).
* **Tensão de Hubble e estrutura em grande escala:** prevê transições tardias com resolução da tensão H0 e 3-5% fσ8 supressão em vazios cósmicos.

---

## Estrutura do Repositório

```text
AETERNVMVACUVM/
├── docs/                       # Monograph versions (V1-V8) & Manuscripts
│   ├── treatises_V1-V8/        # Root Zenodo DOI 10.5281/zenodo.21856036
│   └── manuscripts/            # PRD (DV13843) & PRL (es2026aug07_880) drafts
├── src/                        # Core Solvers and Emulators
│   ├── solver_lsoda.py         # Hyperbolic PDE integration
│   ├── vainshtein_screening.py # Local screening functions
│   └── mcmc_pipeline.py        # Cobaya/EFTCAMB wrapper & GP emulators
└── data/                       # Pre-computed MCMC chains and void residuals
