import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

plt.rcParams['figure.figsize'] = (7, 13)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.rc('axes', labelsize=18)
plt.rc('legend', fontsize=16)
plt.rcParams['lines.markersize'] = 15
plt.rcParams['lines.markeredgewidth'] = 3
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
plt.rcParams['xtick.major.size'] = 10
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['ytick.major.size'] = 10
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['legend.edgecolor'] = 'k'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams['xtick.major.pad'] = 8
plt.rcParams['ytick.major.pad'] = 8
plt.rcParams['legend.handletextpad'] = 0.2
plt.rcParams['legend.columnspacing'] = 0.1
plt.rcParams['legend.labelspacing'] = 0.1
plt.rcParams['legend.title_fontsize'] = 14
plt.rcParams['axes.formatter.limits'] = (-3, 6)

ch2ch2ch3=np.array([[-156.6,15.5,-4.7],[0,1,2]])
ch3ch2ch3=np.array([[-104.6,10.1],[0,1]])
ch3chch3=np.array([[-152.2,19.9],[0,1]])
ch2chch2=np.array([[-221.4,65.8,25.5,-31.6],[0,1,2,3]])

colormap = plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 4)]

gs = gridspec.GridSpec(nrows=2, ncols=1)
gs.update(wspace=0.4, hspace=0.4)

ax0 = plt.subplot(gs[0, 0])
ax1 = plt.subplot(gs[1, 0])

ax0.plot((-0.5,3.5), (0,0), linestyle='dashed',color='k')
ax0.plot(ch2ch2ch3[1],ch2ch2ch3[0], linestyle='solid',color=colors[0], marker='o', markeredgecolor='w', label='$\mathrm{^*CH_2CH_2CH_3}$')
ax0.plot(ch3ch2ch3[1],ch3ch2ch3[0], linestyle='solid',color=colors[1], marker='^', markeredgecolor='w', label='$\mathrm{CH_3CH_2CH_3^*}$')
ax0.plot(ch2chch2[1],ch2chch2[0], linestyle='solid',color=colors[2], marker='s', markeredgecolor='w', label='$\mathrm{^*CH_2^*CH^*CH_2}$')
ax0.plot(ch3chch3[1],ch3chch3[0], linestyle='solid',color=colors[3], marker='p', markeredgecolor='w', label='$\mathrm{CH_3^*CHCH_3}$')



ax0.set_xticks([0, 1, 2, 3])
ax0.set_xlim([-0.2, 3.2])
ax0.set_ylim([-250, 100])
ax0.set_ylabel('$\mathrm{\Delta H_{rxn}\ (kJ\,mol^{-1}) }$')
ax0.set_xticklabels(['$\mathrm{CBH\u2010 0}$', '$\mathrm{CBH\u2010 1}$', '$\mathrm{CBH\u2010 2}$','$\mathrm{CBH\u2010 3}$' ])
ax0.legend()


abs_average_hrxn=[199.00175978180815,80.8621488024708,42.27287967740341,20.194310495069754]
abs_average_zpe_hrxn=[85.98553393442624,10.978384916666652,2.51794725806452,0.9970116666666641]
cbh_rung=np.array([0,1,2,3])

ax1.bar(cbh_rung-0.15,abs_average_hrxn, width=0.3,color=colors[0], edgecolor='k', label='$\mathrm{\overline{|\Delta H_{rxn}|}}$')
ax1.bar(cbh_rung+0.15,abs_average_zpe_hrxn, width=0.3,color=colors[1], edgecolor='k', label='$\mathrm{\overline{|\Delta ZPE_{rxn}|}}$')

ax1.set_xlim([-0.5,3.5])
ax1.set_ylim([0,250])
ax1.set_ylabel('$\mathrm{energy\ (kJ\,mol^{-1})}$') 
ax1.set_xticks([0,1,2,3])
ax1.set_xticklabels(['$\mathrm{CBH\u2010 0}$','$\mathrm{CBH\u2010 1}$','$\mathrm{CBH\u2010 2}$', '$\mathrm{CBH\u2010 3}$'])
ax1.legend()
ax1.arrow(0.2,140,3.1,0, length_includes_head=True, head_length=0.2, head_width=10, color='k')
ax1.text(1.6,145,'$\mathrm{Increasing\ conservation\ of}$\n$\mathrm{bonding\ environment\ and\ hybridization}$',va='bottom',ha='center',size=14,color='k')

import string 
ax0.text(-0.25, 1.05, string.ascii_lowercase[0], transform=ax0.transAxes, size=20, weight='bold')
ax1.text(-0.25, 1.05, string.ascii_lowercase[1], transform=ax1.transAxes, size=20, weight='bold')

plt.savefig('cbh-hrxn.pdf',bbox_inches='tight',transparent=False)