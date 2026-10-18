"""Shared plot style for the project, using a Nubank-inspired purple palette.

Import and call `set_plot_style()` once at the top of each notebook so every
chart uses the same colors and readable defaults.
"""
import matplotlib as mpl
from cycler import cycler

NU_PURPLE = "#820AD1"  # Nubank's primary brand purple: main series
NU_PURPLE_LIGHT = "#C38CEB"  # lighter shade: third series, fills
NU_GRAY = "#8A8984"  # neutral: comparison series, baselines
NU_INK = "#1F1F1F"  # near-black: reference lines and text

# Fixed order for categorical series: purple first, then a clearly different neutral.
PALETTE = [NU_PURPLE, NU_GRAY, NU_PURPLE_LIGHT]


def set_plot_style() -> None:
    """Apply the project palette and readable defaults to matplotlib and seaborn plots."""
    mpl.rcParams.update({
        "axes.prop_cycle": cycler(color=PALETTE),
        "figure.figsize": (10, 5),
        "figure.facecolor": "white",  # opaque background keeps plots readable in dark themes
        "axes.facecolor": "white",
        "axes.edgecolor": NU_INK,
        "axes.labelcolor": NU_INK,
        "axes.titlesize": 13,
        "axes.titleweight": "bold",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "xtick.color": NU_INK,
        "ytick.color": NU_INK,
        "text.color": NU_INK,
        "legend.frameon": False,
    })
