import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

plt.rcParams['figure.figsize'] = (20, 30)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)
plt.rc('axes', labelsize=24)
plt.rc('legend', fontsize=24)
plt.rcParams['lines.markersize'] = 10
plt.rcParams['lines.linewidth'] = 4
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

results=pd.read_csv('CBH_results.txt', sep="\t", header=0, index_col=0)
#CBH1_matrix=CBH1_matrix.fillna(0)

binding_o=['^*OOH','^*OCH_3','H_2C^*O_2CH_3','^*OCH_2CH_3','HCOO^*','^*OCH_2OH']

binding_c3=['^*CCHCH_2','^*CHCHCH_2','^*CHCHCH_3','^*CH_2CH_2CH_3',
           'CH_2^*CCH_3','CH_3^*CHCH_3','^*CCCH_2',
           '^*CCH_2CH_3','CH_3CH_2^*CO','CH_3^*CHOH',
           '^*CHCCH_2','^*CHCH_2CH_3','CH_3^*CCH_3']

binding_c=['^*CCH_2','^*CCH_3','^*COH','^*CH_2CH_3','H_2^*COH','^*CHCH_3',
           'H^*CO','H^*COH','^*COOH','CH_3^*CO','^*CHCO','^*CCH_2OH','^*CCHO','^*CCO','CH_3^*CHOH',
           'CH_3^*COH','^*CHCH_2']

binding_vdW=['CO_2^{phys}','CH_2CO^{phys}','CH_3CHCH_2^{phys}','CH_3CH_2CH_3^{phys}','HCOOH^{phys}',
             'HCO_2CH_3^{phys}','CH_3CH_2OH^{phys}','CH_3CHO^{phys}','CH_2CCH_2^{phys}',
             'CH_3OCH_3^{phys}','H_2CO_2H_2^{phys}','OCO_2H_2^{phys}','CH_3OCH_2OH^{phys}']
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


gs = gridspec.GridSpec(nrows=5, ncols=1)
gs.update(wspace=0.4, hspace=0.8)

ax0 = plt.subplot(gs[0, 0])
ax1 = plt.subplot(gs[1, 0])
ax2 = plt.subplot(gs[2, 0])
ax3 = plt.subplot(gs[3, 0])
ax4 = plt.subplot(gs[4, 0])

o_space=np.arange(len(binding_o))
c_space=np.arange(len(binding_c))
vdW_space=np.arange(len(binding_vdW))
bidentate_space=np.arange(len(bidentate))


#print("'$\mathrm{" + results_o.index.to_list() + "}$'")
string_before="$\mathbf{"
string_end="}$"

#ax0.xaxis.set_label_position('top') 
#ax0.xaxis.tick_top()
ax0.set_xticks(list(np.arange(len(binding_o))))
font_label={'fontsize': 16,
 'fontweight': 'bold'}
box={'facecolor':'w'}
ax0.set_xticklabels((string_before + pd.Series(results_o.index.to_list()) + string_end).tolist(), rotation=70,  fontdict=font_label,bbox=box)
ax0.set_ylabel('$\mathrm{\Delta_fH\ (kJ\,mol^{-1})}$')
ax0.set_title('$\mathbf{^*O-binding\ adsorbates}$', fontsize=26)
ax0.set_xlim([-0.5,7])

ax0.bar(no-0.3+100,results_o.iloc[0,0] , width=0.3, color=colors[0], edgecolor='k', linewidth=3,label='$\mathrm{original}$')
ax0.bar(no+100,results_o.iloc[0,1] , width=0.3, color=colors[1], edgecolor='k', linewidth=3,label='$\mathrm{CBH-1}$')
ax0.bar(no+0.3+100,results_o.iloc[0,3] , width=0.3, color=colors[2], edgecolor='k', linewidth=3,label='$\mathrm{CBH-2}$')
ax0.legend(loc='upper right')

ax0.plot((-2,7),(0,0),linestyle='solid',color='k')

for no,spcs in enumerate(binding_o):
    ax0.bar(no-0.3,results_o.iloc[no,0] , width=0.3, color=colors[0], edgecolor='k', linewidth=3)
    ax0.bar(no,results_o.iloc[no,1] , width=0.3, color=colors[1], edgecolor='k', linewidth=3)
    ax0.bar(no+0.3,results_o.iloc[no,3] , width=0.3, color=colors[2], edgecolor='k', linewidth=3)

#ax1.xaxis.set_label_position('top') 
#ax1.xaxis.tick_top()
ax1.set_xticks(list(np.arange(len(binding_vdW))))
ax1.set_xticklabels((string_before + pd.Series(results_vdW.index.to_list()) + string_end).tolist(), rotation=70, fontdict=font_label,bbox=box)    
ax1.set_ylabel('$\mathrm{\Delta_fH\ (kJ\,mol^{-1})}$')
ax1.set_title('$\mathbf{physisorbed\  species}$', fontsize=26)

ax1.plot((-1,len(binding_vdW)),(0,0),linestyle='solid',color='k')
ax1.set_xlim([-1,len(binding_vdW)])

for no,spcs in enumerate(binding_vdW):
    ax1.bar(no-0.3,results_vdW.iloc[no,0] , width=0.3, color=colors[0], edgecolor='k', linewidth=3)
    ax1.bar(no,results_vdW.iloc[no,1] , width=0.3, color=colors[1], edgecolor='k', linewidth=3)
    ax1.bar(no+0.3,results_vdW.iloc[no,3] , width=0.3, color=colors[2], edgecolor='k', linewidth=3)
    
#ax2.xaxis.set_label_position('top') 
#ax2.xaxis.tick_top()
ax2.set_xticks(list(np.arange(len(bidentate))))
ax2.set_xticklabels((string_before + pd.Series(results_bidentate.index.to_list()) + string_end).tolist(), rotation=70,  fontdict=font_label,bbox=box)    
ax2.set_ylabel('$\mathrm{\Delta_fH\ (kJ\,mol^{-1})}$')
ax2.set_title('$\mathbf{bidentate\ adsorbates}$', fontsize=26)
ax2.plot((-1,len(bidentate)),(0,0),linestyle='solid',color='k')
ax2.set_xlim([-1,len(bidentate)])


for no,spcs in enumerate(bidentate):
    ax2.bar(no-0.3,results_bidentate.iloc[no,0] , width=0.3, color=colors[0], edgecolor='k', linewidth=3)
    ax2.bar(no,results_bidentate.iloc[no,1] , width=0.3, color=colors[1], edgecolor='k', linewidth=3)
    ax2.bar(no+0.3,results_bidentate.iloc[no,3] , width=0.3, color=colors[2], edgecolor='k', linewidth=3)
    #ax2.bar(no+0.9,results_bidentate.iloc[no,5] , width=0.3, color=colors[3], edgecolor='k', linewidth=3)

#ax3.xaxis.set_label_position('top') 
#ax3.xaxis.tick_top()
ax3.set_xticks(list(np.arange(len(binding_c))))
ax3.set_xticklabels((string_before + pd.Series(results_c.index.to_list()) + string_end).tolist(), rotation=70,  fontdict=font_label,bbox=box) 
ax3.set_ylabel('$\mathrm{\Delta_fH\ (kJ\,mol^{-1})}$')
ax3.set_title('$\mathbf{^*C-binding\ adsorbates\ <C_3}$', fontsize=26)
ax3.plot((-1,len(binding_c)),(0,0),linestyle='solid',color='k')
ax3.set_xlim([-1,len(binding_c)])
  
for no,spcs in enumerate(binding_c):
    ax3.bar(no-0.3,results_c.iloc[no,0] , width=0.3, color=colors[0], edgecolor='k', linewidth=3)
    ax3.bar(no,results_c.iloc[no,1] , width=0.3, color=colors[1], edgecolor='k', linewidth=3)
    ax3.bar(no+0.3,results_c.iloc[no,3] , width=0.3, color=colors[2], edgecolor='k', linewidth=3)
    #ax3.bar(no+0.6,results_c.iloc[no,5] , width=0.2, color=colors[3], edgecolor='k', linewidth=3)

#ax4.xaxis.set_label_position('top') 
#ax4.xaxis.tick_top()
ax4.set_xticks(list(np.arange(len(binding_c3))))
ax4.set_xticklabels((string_before + pd.Series(results_c3.index.to_list()) + string_end).tolist(), rotation=70, fontdict=font_label,bbox=box)
ax4.set_ylabel('$\mathrm{\Delta_fH\ (kJ\,mol^{-1})}$')
ax4.set_title('$\mathbf{^*C-binding\ adsorbates\ \u2265 C_3}$', fontsize=26)
ax4.plot((-1,len(binding_c3)),(0,0),linestyle='solid',color='k')
ax4.set_xlim([-1,len(binding_c3)])


for no,spcs in enumerate(binding_c3):
    ax4.bar(no-0.3,results_c3.iloc[no,0] , width=0.3, color=colors[0], edgecolor='k', linewidth=3)
    ax4.bar(no,results_c3.iloc[no,1] , width=0.3, color=colors[1], edgecolor='k', linewidth=3)
    ax4.bar(no+0.3,results_c3.iloc[no,3] , width=0.3, color=colors[2], edgecolor='k', linewidth=3)
    #ax4.bar(no+0.7,results_c3.iloc[no,5] , width=0.2, color=colors[3], edgecolor='k', linewidth=3)

plt.savefig('CBH.pdf', bbox_inches='tight',transparent=False)