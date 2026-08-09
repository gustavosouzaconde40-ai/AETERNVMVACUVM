# AETERNVMVACUVM Framework

**Open-Source Computational Framework for Late-Time Vacuum Phase Transitions, Vainshtein Screening, and Cosmological MCMC Emulators.**

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21398974.svg)](https://doi.org/10.5281/zenodo.21398974)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Overview

`AETERNVMVACUVM` is an open-source physics engine and cosmological emulation toolkit designed to test non-minimal coupling scalar-tensor field theories, Vainshtein screening mechanisms, and late-time vacuum phase transitions ($z \in [0.2, 0.8]$) against precision cosmological observations.

It directly integrates hyperbolic system solvers with Bayesian inference pipelines using **EFTCAMB**, **Cobaya**, and Gaussian Process (GP) emulators.

---

## Key Modules & Theoretical Architecture

### 1. Vacuum Dynamics & Non-Minimal Coupling
Solves the hyperbolic field equation with non-minimal curvature coupling:
$$\Box\phi + \frac{dV}{d\phi} - 2\xi R\phi = 0$$
using high-precision adaptive ODE/PDE integrators (`LSODA` / `DOP853`) with tolerances down to `rtol = 1e-10`.

### 2. Vainshtein Screening Mechanism
Calculates effective gravitational suppression within Solar System and local astrophysical scales to satisfy stringent local gravity bounds while allowing cosmological deviations.

### 3. Cosmological MCMC & Inference Pipeline
* **Datasets:** Integrated support for Planck CMB, DESI Y1/Y3, Pantheon+, and BAO data.
* **Bayesian Emulator:** Gaussian Process emulators acceleration for $w(z)$ equation-of-state reconstructions ($w_0 = -0.712$).
* **Hubble Tension & Large Scale Structure:** Predicts late-time transition resolving $H_0$ tension and 3–5% $f\sigma_8$ suppression in cosmic voids.

---

## Repository Structure

```text
AETERNVMVACUVM/
├── docs/                       # Monograph versions (V1-V8) & Manuscripts
│   ├── treatises_V1-V8/        # Root Zenodo DOI 10.5281/zenodo.21398974
│   └── manuscripts/            # PRD (DV13843) & PRL (es2026aug07_880) drafts
├── src/                        # Core Solvers and Emulators
│   ├── solver_lsoda.py         # Hyperbolic PDE integration
│   ├── vainshtein_screening.py # Local screening functions
│   └── mcmc_pipeline.py        # Cobaya/EFTCAMB wrapper & GP emulators
└── data/                       # Pre-computed MCMC chains and void residuals

---

## ☕ Apoie a Pesquisa / Support

Se você deseja apoiar o desenvolvimento e a manutenção deste framework e das pesquisas:

* **PIX (CPF):** `022.818.517-37`
* **PIX (Celular):** `27 99817 4350`
* **DOI Zenodo:** [10.5281/zenodo.21398974](https://doi.org/10.5281/zenodo.21398974)
## Teoria e Formulação da Likelihood

A função de verificação da *Likelihood* Gaussiana para a análise cosmológica é dada por:

$$\mathcal{L}(\theta) = -\frac{1}{2} \left[ \mathbf{d}^T \mathbf{C}^{-1} \mathbf{d} + \log |\mathbf{C}| + N \log(2\pi) \right]$$

Onde $\mathbf{d} = \mathbf{y}_{\text{data}} - \mathbf{y}_{\text{model}}(\theta)$ é o vetor de resíduos.

### Otimização para MCMC (Decomposição de Cholesky)

Para acelerar a amostragem MCMC quando a matriz de covariância dos dados $\mathbf{C}$ não varia a cada iteração, utilizamos a fatoração de Cholesky $\mathbf{C} = \mathbf{L}\mathbf{L}^T$, onde $\mathbf{L}$ é uma matriz triangular inferior.

1. **Sistemas Triangulares ($O(N^2)$):** O termo quadrático $\mathbf{d}^T \mathbf{C}^{-1} \mathbf{d}$ é resolvido em duas etapas eficientes:
   $$\mathbf{L}\mathbf{y} = \mathbf{d} \quad \implies \quad \mathbf{L}^T \mathbf{x} = \mathbf{y}$$
2. **Determinante Eficiente:** O log-determinante é reduzido à soma dos elementos da diagonal:
   $$\log |\mathbf{C}| = 2 \sum_{i=1}^{N} \log(L_{ii})$$

### Ramo PCA / Woodbury Lemma

Quando a incerteza do emulador é de baixa dimensão ($\mathbf{C}_{\text{emu}} = \mathbf{U}\mathbf{S}\mathbf{U}^T$), aplicamos o *Matrix Inversion Lemma* (Identidade de Woodbury) e o *Matrix Determinant Lemma*:

$$(\mathbf{A} + \mathbf{U}\mathbf{S}\mathbf{U}^T)^{-1} = \mathbf{A}^{-1} - \mathbf{A}^{-1}\mathbf{U}(\mathbf{S}^{-1} + \mathbf{U}^T\mathbf{A}^{-1}\mathbf{U})^{-1}\mathbf{U}^T\mathbf{A}^{-1}$$

$$\log|\mathbf{A} + \mathbf{U}\mathbf{S}\mathbf{U}^T| = \log|\mathbf{S}^{-1} + \mathbf{U}^T \mathbf{A}^{-1} \mathbf{U}| + \log|\mathbf{S}| + \log|\mathbf{A}|$$
