#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:01:32 2026

@author: ibu
"""
from pathlib import Path

from politxe import politxe

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from cycler import cycler


paper_export = False

if paper_export:
    matplotlib.use("pgf")
    matplotlib.rcParams.update(
        {
            "pgf.texsystem": "pdflatex",
            "font.family": "serif",
            "text.usetex": True,
            "pgf.rcfonts": False,
        }
    )
else:
    matplotlib.rcParams.update(matplotlib.rcParamsDefault)


#%% fig 1
textwidth = 3.31314
aspect_ratio = 6/8
scale = 1.0
width = textwidth * scale
height = width * aspect_ratio
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

color_scale = [
    '#d73027', '#f46d43', '#fdae61', '#fee090', '#ffffbf',
    '#e0f3f8', '#abd9e9', '#74add1', '#4575b4'
]


ax.set_prop_cycle(cycler(color=color_scale))
x = np.linspace(0, 10, 100)

for phi in range(3):
    ax.plot(x, np.sin(x + phi), label=phi)


ax.set_xlabel(r"$\alpha$-axis")
ax.set_ylabel(r"$\beta$-axis")
ax.legend()

politxe(
    ax,
    font_family="serif",
    font_size=10,
    label_size=10,
    title_size=10,
    legend_size=10,
    line_width=1.0,
    marker_size=5,
)


output_path = Path(__file__).with_suffix(".pdf")
plt.savefig(output_path, dpi=300, bbox_inches="tight")

#%% fig 2

fig, ax = plt.subplots(figsize=(width, height), dpi=300)

color_scale = ['#4477AA', '#EE6677', '#228833', '#CCBB44', 
               '#66CCEE', '#AA3377', '#BBBBBB']
ax.set_prop_cycle(cycler(color=color_scale))
x = np.linspace(-10, 10, 100)

for phi in range(8):
    ax.plot(x, phi*x**3-3*x+2, label=phi)

ax.set_yscale('log')

ax.set_xlabel(r"$\alpha$-axis")
ax.set_ylabel(r"$\beta$-axis")
#ax.legend()
politxe(
    ax,
    font_family="serif")
output_path = 'politxe_example_2.pdf'
plt.savefig(output_path, dpi=300, bbox_inches="tight")
