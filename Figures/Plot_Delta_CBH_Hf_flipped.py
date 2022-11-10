import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

plt.rcParams['figure.figsize'] = (30, 10)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)
plt.rc('axes', labelsize=22)
plt.rc('legend', fontsize=20)
plt.rcParams['lines.markersize'] = 10
plt.rcParams['lines.linewidth'] = 2
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
plt.rcParams['hatch.linewidth'] = 3.0  # previous svg hatch linewidth

results=pd.read_csv('../CBH_results_CH4_corrected.txt', sep="\t", header=0, index_col=0)
#CBH1_matrix=CBH1_matrix.fillna(0)

binding_o=['^*OCH_3','H_2C^*O_2CH_3','^*OCH_2CH_3','HCOO^*','^*OCH_2OH']

binding_c3=['^*CCHCH_2','^*CHCHCH_2','^*CHCHCH_3','^*CH_2CH_2CH_3',
           'CH_2^*CCH_3','CH_3^*CHCH_3','^*CCCH_2',
           '^*CCH_2CH_3','CH_3CH_2^*CO','CH_3^*CHOH',
           '^*CHCCH_2','^*CHCH_2CH_3','CH_3^*CCH_3']

binding_c=['^*CCH_2','^*CCH_3','^*COH','^*CH_2CH_3','H_2^*COH','^*CHCH_3',
           'H^*CO','H^*COH','^*COOH','CH_3^*CO','^*CHCO','^*CCH_2OH','^*CCHO','^*CCO','CH_3^*CHOH',
           'CH_3^*COH','^*CHCH_2']

binding_vdW=['CO_2^*','CH_2CO^*','CH_3CHCH_2^*','CH_3CH_2CH_3^*','HCOOH^*',
             'HCO_2CH_3^*','CH_3CH_2OH^*','CH_3CHO^*','CH_2CCH_2^*',
             'CH_3OCH_3^*','H_2CO_2H_2^*','OCO_2H_2^*','CH_3OCH_2OH^*']

bidentate=['^*C^*C','^*CH^*CH','^*CH_2^*CH_2','^*CH_2^*CH','^*CH^*C','H^*C^*O',
           'H_2^*C^*O','^*CH_2^*CH^*CH_2','H_2C^*O^*O','OC^*O^*O','HC^*O_3','^*C^*CCH_2',
           'CH_3^*CH^*CH_2']


results_o=[]
for no,spcs in enumerate(binding_o):
    results_o.append(results.loc[spcs].T)

results_o=pd.DataFrame(results_o)

results_vdW=[]
for no,spcs in enumerate(binding_vdW):
    results_vdW.append(results.loc[spcs].T)

results_vdW=pd.DataFrame(results_vdW)

results_bidentate=[]
for no,spcs in enumerate(bidentate):
    results_bidentate.append(results.loc[spcs].T)

results_bidentate=pd.DataFrame(results_bidentate)

results_c=[]
for no,spcs in enumerate(binding_c):
    results_c.append(results.loc[spcs].T)

results_c=pd.DataFrame(results_c)

results_c3=[]
for no,spcs in enumerate(binding_c3):
    results_c3.append(results.loc[spcs].T)

results_c3=pd.DataFrame(results_c3)

colormap = plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 4)]

ax = []
fig, axs = plt.subplots(nrows=1, ncols=5)
fig.subplots_adjust(hspace=0.5, wspace=0.5)
for i, row in enumerate(axs):
        ax.append(i)

o_space=np.arange(len(binding_o))
c_space=np.arange(len(binding_c))
vdW_space=np.arange(len(binding_vdW))
bidentate_space=np.arange(len(bidentate))

string_before="$\mathbf{"
string_end="}$"


font_label={'fontsize': 16,
 'fontweight': 'bold'}
box={'facecolor':'w'}

plots=[binding_o,binding_vdW,bidentate, binding_c,binding_c3]
results=[results_o,results_vdW,results_bidentate, results_c,results_c3]
titles=['$\mathbf{Pt-O}$','$\mathbf{physisorbed}$','$\mathbf{bidentate}$','$\mathbf{Pt-C}$','$\mathbf{Pt-C}$']

props=dict(facecolor='w')

import string 

for i, ax in enumerate(ax):
    axs[i].set_xlim([-100,100])
    axs[i].set_xlabel('$\mathrm{\Delta\Delta_fH\ (kJ\,mol^{-1})}$')    
    axs[i].set_ylim([-0.5,len(plots[i])])
    
    axs[i].plot((0,0),(-1,len(plots[i])),linestyle='solid',color='k')
    axs[i].plot((30,30),(-1,len(plots[i])),linestyle='dashed',color='k')
    axs[i].plot((-30,-30),(-1,len(plots[i])),linestyle='dashed',color='k')
    axs[i].set_yticks([])
    axs[i].set_title(titles[i], fontsize=22)
    axs[i].text(-0.15, 1.05, string.ascii_lowercase[i], transform=axs[i].transAxes, size=24, weight='bold')
    
    for no,spcs in enumerate(plots[i]):
        axs[i].barh(no,results[i].iloc[no,1]-results[i].iloc[no,0] , height=0.5, color=colors[1], edgecolor='k', linewidth=3)
        
        if results[i].iloc[no,1]-results[i].iloc[no,0] <0:    
            axs[i].text(15, no, string_before+spcs+string_end, ha='left',va='center',bbox=props, fontsize='18')
        else:
            axs[i].text(-15, no, string_before+spcs+string_end, ha='right',va='center',bbox=props, fontsize='18')

#Create the legend for one of the plots
axs[0].barh(no-0.3+100,results_o.iloc[0,0] , height=0.3, color=colors[1], edgecolor='k', linewidth=3,label='$\mathrm{CBH\u2010 1}$')
axs[0].plot((-30,-30),(-1,len(binding_o)),linestyle='dashed',color='k',label='$\mathrm{\pm 30\, kJ\,mol^{-1}}$')
handles, labels = axs[0].get_legend_handles_labels()

axs[0].legend(handles=[handles[1],handles[0]],loc='upper right')

plt.savefig('Delta_CBH_flipped_corrected.pdf', bbox_inches='tight',transparent=False)