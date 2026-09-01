---
title: 'Aeternvm Vacuvm: A Computational Framework for Vacuum Depletion Physics, Vainshtein Screening, and Cosmological MCMC Emulators'
tags:
  - Python
  - cosmology
  - vacuum depletion
  - modified gravity
  - MCMC emulators
  - Vainshtein screening
authors:
  - name: Gustavo Alves Condé
    orcid: 0009-0000-0000-0000 # Substitua pelo seu ORCID seouver
    affiliation: Independent Researcher, Baixo Guandu, ES, Brazil
date: 26 August 2026
bibliography: paper.bib
---

# Summary

**Aeternvm Vacuvm** is an open-source computational framework designed to solve, emulate, and test modified gravity theories, late-time vacuum phase transitions, and Vainshtein screening mechanisms against high-precision cosmological datasets (such as Planck CMB, DESI Y1/Y3, and Pantheon+ BAO)[span_1](start_span)[span_1](end_span). Traditional cosmological pipelines often lack unified, accessible tools to couple non-linear scalar-tensor dynamics with fast Bayesian inference. *Aeternvm Vacuvm* bridges this gap by providing high-precision numerical solvers for hyperbolic field equations alongside integrated Gaussian Process (GP) emulators and MCMC pipelines.

# Statement of Need

In modern precision cosmology, testing dynamical dark energy models and vacuum depletion scenarios requires heavy numerical computations, involving the simultaneous solution of background evolution, perturbation equations, and local screening effects. Existing software libraries are either restricted to standard $\Lambda\text{CDM}$ or fragmented across specialized codes that are difficult to couple with modern Bayesian samplers. 

*Aeternvm Vacuvm* provides researchers and independent scientists with a self-contained, modular Python engine to:
1. Solve non-linear scalar field evolution and background dynamics deterministically.
2. Evaluate local gravitational suppression via Vainshtein screening mechanics.
3. Accelerate cosmological parameter inference using optimized Gaussian Process emulators integrated with frameworks like Cobaya and EFTCAMB.

# Mathematical and Physical Architecture

The framework is built upon rigorous theoretical foundations linking laboratory electromagnetism to late-time cosmic acceleration.

## Vacuum Depletion Potential and Impedance Coupling
The depletion field $\chi$ is governed by a potential of the form[span_2](start_span)[span_2](end_span):

$$V(\chi) = V_0 \left[1 - \exp\left(-\frac{\lambda \chi}{M_{\rm Pl}}\right)\right]^2$$

Crucially, the energy scale $V_0$ is not treated as a free tuning parameter. Instead, it is analytically constrained by the vacuum impedance $Z_0 = \sqrt{\mu_0 / \epsilon_0} \approx 376.73\,\Omega$[span_3](start_span)[span_3](end_span):

$$V_0 = \frac{\hbar}{2 Z_0 c \ell_P^3} \left(1 - e^{-S_{\rm inst}}\right)$$

where $S_{\rm inst} \approx 280$ represents a non-perturbative instanton-like action[span_4](start_span)[span_4](end_span). This yields $V_0 \sim 10^{-47}\,\text{GeV}^4$, naturally matching the observed dark energy density scale without fine-tuning[span_5](start_span)[span_5](end_span).

## Modified Friedmann and Field Equations
The background expansion dynamics including matter and the depletion field are governed by the modified Friedmann equations[span_6](start_span)[span_6](end_span):

$$H^2 = \frac{8\pi G}{3}\left( \rho_m + \frac{1}{2}\dot{\chi}^2 + V(\chi) \right), \quad \dot{H} = -4\pi G \left( \rho_m + \dot{\chi}^2 \right)$$

The Klein-Gordon equation describing the evolution of $\chi$ is solved numerically via high-precision adaptive ODE/PDE routines (such as LSODA and DOP853):

$$\ddot{\chi} + 3H\dot{\chi} + V'(\chi) = 0$$

# Software Design and Implementation

The repository is organized into modular packages under the `src/` directory:
* **`solver_isoda.py`**: High-precision hyperbolic PDE and background ODE integrators with strict error tolerances ($rtol \le 10^{-10}$)[span_7](start_span)[span_7](end_span).
* **`vainshtein_screening.py`**: Routines to evaluate local gravitational suppression within the Solar System and astrophysical scales, ensuring compatibility with local gravity tests[span_8](start_span)[span_8](end_span).
* **`mcmc_pipeline.py`**: Bayesian inference wrappers optimized with Cholesky decomposition and Woodbury matrix lemmas for fast likelihood evaluations.
### Quality control

AETERNVMVACUVM includes an automated test suite (pytest) covering Vainshtein screening solvers, vacuum depletion phase transitions, and cosmological MCMC emulator consistency. Tests include import checks, numerical consistency on synthetic data, and edge cases. Continuous integration via GitHub Actions runs the test suite on Python 3.9, 3.10, and 3.11 on every push and pull request. Example datasets are included; large simulation outputs are archived on Zenodo (DOI: 10.5281/zenodo.22166663).

### Availability

**Source code:** https://github.com/gustavosouzaconde40-ai/AETERNVMVACUVM
**License:** MIT
**Installation:** `pip install.` or `pip install -e.[test]` for development
**Supported Python versions:** 3.9, 3.10, 3.11
**Documentation:** See README.md and docstrings
**Archived release (Zenodo):** 10.5281/zenodo.22166663 (v1.1.0-complete) - Concept DOI (all versions): 10.5281/zenodo.21856036
# References
