"""likelihood package exports for AETERNVM VACUVM

This module re-exports the core functions from likelihood_emulator
for convenient imports like `from likelihood import compute_log_likelihood`.
"""

from .likelihood_emulator import (
    window_stitching,
    vainshtein_suppression,
    combine_power_spectrum,
    compute_log_likelihood,
)

__all__ = [
    "window_stitching",
    "vainshtein_suppression",
    "combine_power_spectrum",
    "compute_log_likelihood",
]
