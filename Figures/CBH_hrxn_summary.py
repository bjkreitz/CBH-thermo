#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:33:25 2022

@author: bkr
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

plt.rcParams['figure.figsize'] = (7, 6)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.rc('axes', labelsize=18)
plt.rc('legend', fontsize=18)
plt.rcParams['lines.markersize'] = 10
plt.rcParams['lines.linewidth'] = 2
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.size'] = 0
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['ytick.major.size'] = 10
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['legend.edgecolor'] = 'k'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8
plt.rcParams['legend.handletextpad'] = 0.4
plt.rcParams['legend.columnspacing'] = 0.8
plt.rcParams['legend.labelspacing'] = 0.3
plt.rcParams['legend.title_fontsize'] = 14
plt.rcParams['axes.formatter.limits'] = (-3, 6)
plt.rcParams['hatch.linewidth'] = 3.0  # previous svg hatch linewidth

colormap = plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 4)]

gs = gridspec.GridSpec(nrows=1, ncols=1)
gs.update(wspace=0.4, hspace=0.4)

ax0 = plt.subplot(gs[0, 0])

abs_average_hrxn=[199.00175978180815,80.8621488024708,42.27287967740341,20.194310495069754]
cbh_rung=[0,1,2,3]

ax0.bar(cbh_rung,abs_average_hrxn, width=0.25,color=colors[0], edgecolor='k')
#ax0.bar(1-0.125,error_c_all[1], width=0.25,color=colors[0], edgecolor='k')
#ax0.bar(2-0.125,error_bidentate[1], width=0.25,color=colors[0], edgecolor='k')
#ax0.bar(3-0.125,error_vdW[1], width=0.25,color=colors[0], edgecolor='k')

ax0.set_xlim([-0.5,3.5])
ax0.set_ylim([0,250])
ax0.set_ylabel('$\mathrm{mean\ absolute\ \Delta H_{rxn}\ (kJ\,mol^{-1})}$') 
ax0.set_xticks([0,1,2,3])
ax0.set_xticklabels(['$\mathrm{CBH\u2010 0}$','$\mathrm{CBH\u2010 1}$','$\mathrm{CBH\u2010 2}$', '$\mathrm{CBH\u2010 3}$'])
#ax0.legend()


ax0.arrow(0.2,150,3.1,0, length_includes_head=True, head_length=0.2, head_width=10, color='k')
ax0.text(1.6,150,'$\mathrm{Increasing\ conservation\ of}$\n$\mathrm{bonding\ environment\ and\ hybridization}$',va='bottom',ha='center',size=14,color='k')