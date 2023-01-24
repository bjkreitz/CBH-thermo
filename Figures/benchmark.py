
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

hf_OCH3=-2.4

hf_CH3CH2CH3=1.9

hf_HCOOH=-8.5

hf_HCOO=-32.7

no=[0,1,2,3]

ax0.set_xlim([-0.5,3.5])
ax0.set_ylim([-40,40])
ax0.set_ylabel('$\mathrm{\Delta\Delta_fH\ (kJ\,mol^{-1})}$') 
ax0.set_xticks([ ])
#ax0.set_xticklabels(['$\mathrm{^*OCH_3}$','$\mathrm{CH_3CH_2CH_3^*}$','$\mathrm{HC(O)OH^*}$','$\mathrm{HC(O)^*O}$'])
#ax0.legend()
props=dict(facecolor='w')
ax0.plot((-0.5,5),(0,0),linestyle='solid',color='k')
ax0.plot((-0.5,5),(10,10),linestyle='dashed',color='k',linewidth=2)
ax0.plot((-0.5,5),(-10,-10),linestyle='dashed',color='k',linewidth=2)

ax0.bar(no[0],hf_OCH3, width=0.5,color=colors[0], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')

ax0.text(no[0], hf_OCH3-1, '$\mathrm{^*OCH_3}$', ha='center',va='top', fontsize='16')

ax0.bar(no[1],hf_CH3CH2CH3, width=0.5,color=colors[1], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax0.text(no[1], hf_CH3CH2CH3+1, '$\mathrm{CH_3CH_2CH_3^*}$', ha='center',va='bottom', fontsize='16')

ax0.bar(no[2],hf_HCOOH, width=0.5,color=colors[2], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax0.text(no[2], hf_HCOOH-2, '$\mathrm{HC(O)OH^*}$', ha='center',va='top', fontsize='16')

ax0.bar(no[3],hf_HCOO, width=0.5,color=colors[3], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax0.text(no[3], hf_HCOO-1, '$\mathrm{HC(O)^*O}$', ha='center',va='top', fontsize='16')

plt.savefig('benchmark.png', dpi=300, bbox_inches='tight',transparent=False)