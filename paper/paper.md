---
title: 'AETERNVMVACUVM: A Computational Framework for Late-Time Vacuum Phase Transitions, Vainshtein Screening, and Cosmological MCMC Emulators'
tags:
    - cosmology
    - vacuum depletion
    - modified gravity
    - MCMC emulators
    - Vainshtein screening
    - Z0 unit
authors:
    - name: Gustavo Alves Conde
    orcid: 0009-0003-8264-7907
    affiliation: 1
affiliations:
    - name: Independent Researcher, Colatina-ES, Brazil
    index: 1
date: 5 September 2026
bibliography: papel.bib
---

# Summary

AETERNVMVACUVM is an open-source computational framework designed to solve, emulate, and test modified gravity theories, late-time vacuum phase transitions, and Vainshtein screening mechanisms against high-precision cosmological datasets (Planck CMB, DESI Y1/Y3, Pantheon+ BAO). Traditional pipelines lack unified tools to couple non-linear scalar-tensor dynamics with fast Bayesian inference.

AETERNVMVACUVM bridges this gap by providing high-precision numerical solvers for hyperbolic field equations alongside integrated Gaussian Process emulators and MCMC pipelines, now with Z0 = 376.73 Ohm as natural unit (v5.0 5-PROVAS).

# Statement of Need

In modern precision cosmology, testing dynamical dark energy and vacuum depletion requires heavy numerical computations involving background evolution, perturbation equations, and local screening. Existing libraries are restricted to ΛCDM or fragmented.

AETERNVMVACUVM provides a modular Python engine to:

1. Solve non-linear scalar field evolution deterministically
2. Evaluate local gravitational suppression via Vainshtein screening
3. Accelerate inference using optimized Gaussian Process emulators integrated with Cobaya and EFTCAMB

# Mathematical and Physical Architecture v5.0 - Z0 as unit

## Vacuum Depletion Potential and Impedance Coupling

The depletion field χ is governed by:

$$V(\\chi) = V_0 \\left[1 - \\exp\\left(-\\frac{\\lambda \\chi}{M_{Pl}}\\right)\\right]^2$$

Crucially, V0 is not free. It is constrained by vacuum impedance Z0 = sqrt(mu0/epsilon0) ≈ 376.73 Ohm = 1:

$$V_0 = \\frac{\\hbar}{2 Z_0 c \\ell_P^3}(1 - e^{-S_{inst}})$$

where S_inst ≈ 280 is non-perturbative instanton action. This yields V0 ~ 10^-47 GeV4, matching observed dark energy without fine-tuning.

$$Z_0 = 376.730313668\\,Ohm = 1$$
$$S_{inst}=280 \\rightarrow e^{-S}=10^{-121.6}$$
$$\\rho_\\Lambda = M_{Pl}^4 e^{-S}=10^{-47}\\,GeV^4$$
$$k = 2\\pi Z_0 / S = 8.45\\,Ohm$$
$$S/2\\pi=44.56\\,windings, N_{inst}=S/4\\pi=22$$
$$R_K/k=3053.6$$

## 5 Convergent Proofs (VACUO-ATIVO-5-PROVAS v5.0 FINAL)

1. **JWST CEERS z>10:** lambda/M_Pl ~ (Z0/Z_Pl)^n exp(-S/4) - consistent
2. **IXPE Magnetar 1E 1547.0-5408 15 bins:** rvm_params_1e1547_15bins.csv - PD=0.556, chi2_QED=18.12/14=1.29, Delta=6.46 LIMITE forecast 23.0@500h - code probabilidade/AV_likelihood.py
3. **LZ 2024:** xi ~ Z0 - limit
4. **Z0 as unit:** k=8.45 Ohm derived, N_inst=22
5. **Falsifiable forecast:** If 500h IXPE does not give Delta>9, Z0-unit refuted

Status: Ciclo metodologico fechado, comprovacao aberta - 05-09-2026 - ORCID 0009-0003-8264-7907

## Modified Friedmann and Field Equations

$$H^2 = \\frac{8\\pi G}{3}(\\rho_m + \\frac{1}{2}\\dot{\\chi}^2 + V(\\chi))$$

$$\\dot{H} = -4\\pi G(\\rho_m + \\dot{\\chi}^2)$$

Klein-Gordon:

$$\\ddot{\\chi} + 3H\\dot{\\chi} + V'(\\chi)=0$$

Solved via LSODA/DOP853 rtol ≤ 1e-10.

# Software Design

- solver_lsoda.py: High-precision hyperbolic PDE and ODE integrators
- vainshtein_screening.py: Evaluate local suppression
- mcmc_pipeline.py: Bayesian wrappers with Cholesky and Woodbury

# Quality control

Automated pytest covering screening solvers, vacuum depletion, and MCMC emulator consistency. CI via GitHub Actions on Python 3.9, 3.10, 3.11. Large outputs archived Zenodo 10.5281/zenodo.22166663.

# Availability

Source: https://github.com/gustavosouzaconde40-ai/AETERNVMVACUVM
License: MIT
Installation: pip install. or pip install -e.[test]
Supported Python: 3.9, 3.10, 3.11
Archived release (Zenodo): 10.5281/zenodo.22166663 (v1.1.0-complete)
NEW v5.0 5-PROVAS: 10.5281/zenodo.22347657
Concept DOI: 10.5281/zenodo.21856036
Chain: 22096687, 22164502, 22165507, 22166663, 22347657

# References

State of the field: Cosmological inference for screened modified gravity relies on CLASS, CAMB and N-body. Existing Python tools (hi_class, MG-CAMB) lack unified vacuum depletion and fast likelihood. MCMC remains prohibitive without emulation.

AETERNVMVACUVM bridges gap by integrating (i) analytical models for vacuum depletion and Vainshtein, (ii) likelihood module with mu_eff(k,a), (iii) emulators for screening.

Research impact: Enables reproducible research in alternative gravity and vacuum physics relevant to DESI, Euclid and LSST. Provides tested likelihood and emulator interface. Modular design serves as pedagogical tool.

Early adoption: Use in author's MCMC analyses of vacuo deplecao, potential impact on modified gravity constraints.

# AI usage disclosure

During preparation, generative AI (Copilot and ChatGPT) were used for correction of Python indentation and flake8 E999 errors, drafting docstrings and boilerplate for CI.github/workflows/python-package.yml, suggestions for structuring paper to meet JOSS requirements. All scientific content, derivations of vacuum depletion model, Vainshtein screening implementation, and validation tests were authored and verified by human author. No AI was used to generate scientific results or figures.
