title: 'AETERNVMVACUVM: A Computational Framework for Vacuum Phase Transitions, Vainshtein Screening and Cosmological MCMC Emulators'
tags:

cosmology
vacuum decay
Vainshtein screening
MCMC
EFT
DESI
authors:
name: Gustavo Alves Conde
orcid: 0009-0003-8264-7907
affiliation: 1
email: gustavo.conde@example.com
affiliations:
name: Independent Researcher, Colatina-ES, Brazil
index: 1
date: 5 September 2026
bibliography: papel.bib
Summary
AETERNVMVACUVM is an open-source computational framework for late-time vacuum phase transitions, Vainshtein screening, and cosmological MCMC emulators. It integrates hyperbolic PDE solvers with Bayesian inference pipelines using EFTCAMB, Cobaya and Gaussian Process emulators.

The framework is designed to test non-minimally coupled scalar-tensor theories, Vainshtein screening mechanisms and late-time vacuum phase transitions (z in [0.2,0.8]) against precision cosmological observations (Planck CMB, DESI Y1/Y3, Pantheon+ and BAO).

Statement of need
Current cosmological tensions (H0 tension and S8 suppression in cosmic voids) require tools that can test screening mechanisms while satisfying local gravity constraints. AETERNVMVACUVM provides:

Vacuum dynamics and non-minimal coupling: Solves hyperbolic field equation Box phi + dV/dphi - xi R phi = 0 using adaptive ODE/PDE integrators (LSODA/DOP853) with rtol=1e-10.
Vainshtein screening: Calculates effective gravitational suppression inside Solar System and local astrophysical scales.
MCMC pipeline: Integrated support for Planck CMB, DESI Y1/Y3, Pantheon+ and BAO. GP emulators for w(z) (w0=-0.712). Predicts late-time transitions with H0 tension resolution and 3-5% f_sigma8 suppression in voids.
Related chain - 5 PROVAS v5.0
This framework is part of the chain:

DOI 1 - Conde-Ruler: 10.5281/zenodo.22096687 (prime gaps ruler)
DOI 2 - Conde-Triangle: 10.5281/zenodo.22164502 + backup 10.5281/zenodo.22165628
DOI 3 - VIEC Mk.IV-C Zbites: 10.5281/zenodo.22165507
DOI 4 - Full Framework: 10.5281/zenodo.22166663 (v1.1.0-complete)
DOI Parent (all versions): 10.5281/zenodo.21856036
NEW v5.0 5-PROVAS: 10.5281/zenodo.22347657 - Z0=376.73 Ohm as unit, k=8.45 Ohm, S_inst=280, N_inst=22, PD=0.556, Delta=6.46 LIMIT forecast 23.0@500h (IXPE 1E 1547.0-5408)
The 5 provas convergent framework (JWST CEERS z>10, IXPE magnetar 1E 1547 15 bins rvm_params_1e1547_15bins.csv with AV_likelihood.py, LZ 2024, Z0 as unit, falsifiable forecast) closes the methodological cycle.

References
See papel.bib for full bibliography including Planck 2020, DESI Y1, and Vainshtein screening literature.

