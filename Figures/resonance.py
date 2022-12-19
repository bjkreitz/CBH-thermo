
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.rcParams['figure.figsize'] = (7, 6)
plt.rcParams['axes.linewidth'] = 3
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.rc('axes', labelsize=18)
plt.rc('legend', fontsize=16)
plt.rcParams['lines.markersize'] = 10
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


colormap = plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 4)]

gs = gridspec.GridSpec(nrows=1, ncols=1)
gs.update(wspace=0.4, hspace=0.4)

ax0 = plt.subplot(gs[0, 0])

old_hf_CHCH=12.8
hf_CH_singlebond_CH=np.array([97.3,62.3])
hf_CH_doublebond_CH=np.array([10.5,79.8])

old_hf_CCH=128.0
hf_C_doublebond_CH=np.array([173.5, 10.5])
hf_C_singlebond_CH=np.array([156.9,-79.6])

old_hf_CC=210.4
hf_C_doublebond_C=np.array([303.7,-26.0])
hf_C_singlebond_C=np.array([183.5,-188.5])

no=[0,1,2]

ax0.set_xlim([-0.5,2.5])
ax0.set_ylim([-40,100])
ax0.set_ylabel('$\mathrm{\Delta\Delta_fH\ (kJ\,mol^{-1})}$') 
ax0.set_xticks([0,1,2])
ax0.set_xticklabels(['$\mathrm{^*CH^*CH}$','$\mathrm{^*C^*CH}$','$\mathrm{^*C^*C}$'])
#ax0.legend()

ax0.plot((-0.5,3),(0,0),linestyle='solid',color='k')

#ax0.bar(no[0],old_hf_CHCH, width=0.2,color=colors[0], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax0.bar(no[0]-0.1,hf_CH_singlebond_CH[0]-old_hf_CHCH, width=0.2,color=colors[0], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax0.bar(no[0]+0.1,hf_CH_doublebond_CH[0]-old_hf_CHCH, width=0.2,color=colors[0], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')



#ax0.bar(no[1],old_hf_CCH, width=0.2,color=colors[1], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax0.bar(no[1]-0.1,hf_C_doublebond_CH[0]-old_hf_CCH, width=0.2,color=colors[1], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax0.bar(no[1]+0.1,hf_C_singlebond_CH[0]-old_hf_CCH, width=0.2,color=colors[1], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')

#ax0.bar(no[2],old_hf_CC, width=0.2,color=colors[2], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax0.bar(no[2]-0.1,hf_C_doublebond_C[0]-old_hf_CC, width=0.2,color=colors[2], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax0.bar(no[2]+0.1,hf_C_singlebond_C[0]-old_hf_CC, width=0.2,color=colors[2], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')

plt.savefig('resonance.pdf', bbox_inches='tight',transparent=False)