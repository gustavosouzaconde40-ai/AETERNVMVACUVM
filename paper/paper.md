---
title: 'Aeternvm Vacuvm: A Computational Framework for Vacuum Depletion Physics, Vainshtein Screening, and Cosmological MCMC Emulators'
tags: [Python, cosmology, vacuum depletion, modified gravity, MCMC emulators, Vainshtein screening]
authors:
- name: Gustavo Alves CondÃ©
  orcid: 0009-0003-8264-7907
  affiliation: 1
affiliations:
- name: Independent Researcher, Baixo Guandu, ES, Brazil
  index: 1
date: 26 August 2026
bibliography: paper.bib
---

# Summary

**Aeternvm Vacuvm** is an open-source computational framework designed to solve, emulate, and test modified gravity theories, late-time vacuum phase transitions, and Vainshtein screening mechanisms against high-precision cosmological datasets (such as Planck CMB, DESI Y1/Y3, and Pantheon+ BAO). Traditional cosmological pipelines often lack unified, accessible tools to couple non-linear scalar-tensor dynamics with fast Bayesian inference. *Aeternvm Vacuvm* bridges this gap by providing high-precision numerical solvers for hyperbolic field equations alongside integrated Gaussian Process (GP) emulators and MCMC pipelines.

# Statement of Need

In modern precision cosmology, testing dynamical dark energy models and vacuum depletion scenarios requires heavy numerical computations, involving the simultaneous solution of background evolution, perturbation equations, and local screening effects. Existing software libraries are either restricted to standard $\Lambda\text{CDM}$ or fragmented across specialized codes that are difficult to couple with modern Bayesian samplers.

*Aeternvm Vacuvm* provides researchers and independent scientists with a self-contained, modular Python engine to:
1. Solve non-linear scalar field evolution and background dynamics deterministically.
2. Evaluate local gravitational suppression via Vainshtein screening mechanics.
3. Accelerate cosmological parameter inference using optimized Gaussian Process emulators integrated with frameworks like Cobaya and EFTCAMB.

# Mathematical and Physical Architecture

The framework is built upon rigorous theoretical foundations linking laboratory electromagnetism to late-time cosmic acceleration.

## Vacuum Depletion Potential and Impedance Coupling
The depletion field $\chi$ is governed by a potential of the form:

$$V(\chi) = V_0 \left[1 - \exp\left(-\frac{\lambda \chi}{M_{\rm Pl}}\right)\right]^2$$

Crucially, the energy scale $V_0$ is not treated as a free tuning parameter. Instead, it is analytically constrained by the vacuum impedance $Z_0 = \sqrt{\mu_0 / \epsilon_0} \approx 376.73\,\Omega$:

$$V_0 = \frac{\hbar}{2 Z_0 c \ell_P^3} \left(1 - e^{-S_{\rm inst}}\right)$$

where $S_{\rm inst} \approx 280$ represents a non-perturbative instanton-like action. This yields $V_0 \sim 10^{-47}\,\text{GeV}^4$, naturally matching the observed dark energy density scale without fine-tuning.

## Modified Friedmann and Field Equations
The background expansion dynamics including matter and the depletion field are governed by the modified Friedmann equations:

$$H^2 = \frac{8\pi G}{3}\left( \rho_m + \frac{1}{2}\dot{\chi}^2 + V(\chi) \right), \quad \dot{H} = -4\pi G \left( \rho_m + \dot{\chi}^2 \right)$$

The Klein-Gordon equation describing the evolution of $\chi$ is solved numerically via high-precision adaptive ODE/PDE routines (such as LSODA and DOP853):

$$\ddot{\chi} + 3H\dot{\chi} + V'(\chi) = 0$$

# Software Design and Implementation

The repository is organized into modular packages under the `src/` directory:
* **`solver_lsoda.py`**: High-precision hyperbolic PDE and background ODE integrators with strict error tolerances ($rtol \le 10^{-10}$).
* **`vainshtein_screening.py`**: Routines to evaluate local gravitational suppression within the Solar System and astrophysical scales, ensuring compatibility with local gravity tests.
* **`mcmc_pipeline.py`**: Bayesian inference wrappers optimized with Cholesky decomposition and Woodbury matrix lemmas for fast likelihood evaluations.

### Quality control

AETERNVMVACUVM includes an automated test suite (pytest) covering Vainshtein screening solvers, vacuum depletion phase transitions, and cosmological MCMC emulator consistency. Tests include import checks, numerical consistency on synthetic data, and edge cases. Continuous integration via GitHub Actions runs the test suite on Python 3.9, 3.10, and 3.11 on every push and pull request. Example datasets are included; large simulation outputs are archived on Zenodo (DOI: 10.5281/zenodo.22166663).

### Availability

**Source code:** https://github.com/gustavosouzaconde40-ai/AETERNVMVACUVM
**License:** MIT
**Installation:** `pip install .` or `pip install -e .[test]` for development
**Supported Python versions:** 3.9, 3.10, 3.11
**Documentation:** See README.md and docstrings
**Archived release (Zenodo):** 10.5281/zenodo.22166663 (v1.1.0-complete) - Concept DOI (all versions): 10.5281/zenodo.21856036

# References

## State of the field

Cosmological parameter inference for screened modified gravity and vacuum decay models typically relies on computationally expensive Boltzmann solvers (e.g., CLASS, CAMB) and N-body simulations. Existing Python tools for Vainshtein screening focus on specific models (e.g., `hi_class`, `MG-CAMB`) but lack a unified framework for vacuum depletion physics and fast likelihood evaluation. MCMC sampling in these high-dimensional spaces remains prohibitive without emulation.

`AETERNVM VACUVM` bridges this gap by providing a computational structure that integrates (i) analytical models for vacuum depletion and Vainshtein screening, (ii) a likelihood module with `mu_eff` corrections, and (iii) cosmological emulators trained to accelerate MCMC. Compared to existing emulators that target only $\Lambda$CDM or $w_0w_a$CDM, this package is designed for screening mechanisms where the effective gravitational coupling $\mu_{\rm eff}(k,a)$ is scale and time dependent.

## Research impact statement

The software enables reproducible research in alternative gravity and vacuum physics, areas relevant to DESI, Euclid and LSST analyses. By providing a tested likelihood (`likelihood/probabilidade_mu_eff.py`) and emulator interface, it lowers the barrier for cosmologists to test Vainshtein-screened models against data without reimplementing screening formulas. The modular design also serves as a pedagogical tool for graduate courses in cosmological data analysis.

Early adoption includes use in the author's MCMC analyses of void deplecao do vacuo, with potential impact on constraints for modified gravity theories.

## AI usage disclosure

During the preparation of this work, generative AI tools (GitHub Copilot and ChatGPT) were used for:

- Correction of Python indentation and flake8 E999 errors
- Drafting of docstrings and boilerplate for CI workflow `.github/workflows/python-package.yml`
- Suggestions for structuring this paper to meet JOSS requirements

All scientific content, derivations of the vacuum depletion model, Vainshtein screening implementation, and validation tests were authored and verified by the human author. No AI was used to generate scientific results or figures.
