#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 16:01:32 2026

@author: ibu
"""
from politxe import politxe
from cycler import cycler

import matplotlib

#matplotlib.use('Qt5Agg')  # or 'Qt5Agg' if PyQt is installed


import matplotlib.pyplot as plt
import numpy as np
#fig, ax = plt.subplots(figsize=(3.5, 2.4), dpi=300)

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


    

# fig size

textwidth = 3.31314
aspect_ratio = 6/8
scale = 1.0
width = textwidth * scale
height = width * aspect_ratio
#fig, ax = plt.figure(figsize=(width, height), dpi=300)
fig, ax = plt.subplots(figsize=(width, height), dpi=300)


#ax.set_prop_cycle(cycler(color=['0C5DA5', '00B945', 'FF9500', 'FF2C00', '845B97', '474747', '9e9e9e']))

x = np.linspace(0, 10,100)
y = np.sin(x)

for phi in range(4):
    ax.plot(x, np.sin(x+phi), label=phi)

ax.set_xlabel(r"$\alpha$-axis")
ax.set_ylabel(r"$\beta$-axis")

#legend = ax.legend(fancybox=False, edgecolor="black")
#legend.get_frame().set_linewidth(0.1)

ax.legend()

politxe(
    ax,
    font_family="serif",
    font_size=12,
    label_size=12,
    title_size=12,
    legend_size=12,
    line_width=1.0,
    marker_size=5,
)


#plt.savefig('example.pdf', dpi=300)
plt.savefig('example.pdf', dpi=300, bbox_inches='tight')


plt.show()
