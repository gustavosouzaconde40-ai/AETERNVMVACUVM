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
