#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 15:30:21 2026

@author: ibu
"""

from __future__ import annotations

from cycler import cycler

import matplotlib.pyplot as plt


def politxe(
    ax: plt.Axes,
    *,
    with_grid: bool = False,
    minor_ticks: bool = False,
    spine_width: float = 1.5,
    tick_width: float = 1.5,
    spine_offset: float = 5,
    facecolor: str = "w",
    font_family: str = "serif",
    font_size: int = 14,
    label_size: int = 14,
    title_size: int = 14,
    legend_size: int = 14,
    line_width: float = 1.0,
    marker_size: float = 5,
) -> plt.Axes:
    """
    Style a Matplotlib Axes object for publication-style scientific plots.

    This version uses serif fonts and only modifies the provided Axes object.
    It does not change global Matplotlib rcParams.
    """


    # Set color cycle
    # Set line style as well for black and white graphs
    ax.set_prop_cycle(cycler(color=['0C5DA5', '00B945', 'FF9500', 'FF2C00', '845B97', '474747', '9e9e9e']))

    # ------------------------------------------------
    # Spines
    ax.spines["left"].set_position(("outward", spine_offset))
    ax.spines["bottom"].set_position(("outward", spine_offset))

    ax.spines["right"].set_visible(False)
    ax.spines["top"].set_visible(False)

    for spine in ax.spines.values():
        spine.set_linewidth(spine_width)

    # ------------------------------------------------
    # Ticks
    ax.yaxis.set_ticks_position("left")
    ax.xaxis.set_ticks_position("bottom")

    ax.tick_params(
        axis="both",
        which="both",
        width=tick_width,
        labelsize=font_size,
    )

    for tick_label in ax.get_xticklabels() + ax.get_yticklabels():
        tick_label.set_family(font_family)
        tick_label.set_fontsize(font_size)

    if minor_ticks:
        ax.minorticks_on()

    # ------------------------------------------------
    # Grid and background
    ax.grid(with_grid)
    ax.set_facecolor(facecolor)

    # ------------------------------------------------
    # Axis labels
    ax.xaxis.label.set_family(font_family)
    ax.yaxis.label.set_family(font_family)

    ax.xaxis.label.set_fontsize(label_size)
    ax.yaxis.label.set_fontsize(label_size)

    # ------------------------------------------------
    # Title
    ax.title.set_family(font_family)
    ax.title.set_fontsize(title_size)

    # ------------------------------------------------
    # Legend, if present
    legend = ax.get_legend()
    if legend is not None:
        for text in legend.get_texts():
            text.set_family(font_family)
            text.set_fontsize(legend_size)

        legend.get_frame().set_linewidth(spine_width)

    # ------------------------------------------------
    # Lines and markers
    for line in ax.lines:
        line.set_linewidth(line_width)
        line.set_markersize(marker_size)

    return ax