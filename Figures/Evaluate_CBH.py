import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as mpatches

plt.rcParams['figure.figsize'] = (14, 6)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=22)
plt.rc('ytick', labelsize=22)
plt.rc('axes', labelsize=24)
plt.rc('legend', fontsize=24)
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

results=pd.read_csv('../CBH_results.txt', sep="\t", header=0, index_col=0)
#CBH1_matrix=CBH1_matrix.fillna(0)

species=['^*CH_2^*CH^*CH_2','H_2C^*O_2CH_3','H_2C^*O^*O']


results_hf=[]
for no,spcs in enumerate(species):
    results_hf.append(results.loc[spcs].T)

results_hf=pd.DataFrame(results_hf)

colormap = plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 4)]


gs = gridspec.GridSpec(nrows=1, ncols=2)
gs.update(wspace=0.4, hspace=0.4)

ax0 = plt.subplot(gs[0, 0])
ax1 = plt.subplot(gs[0, 1])


space_hf=np.arange(len(results_hf.columns)-4)
space_hrxn=np.arange(len(results_hf.columns)-4)+1

def get_hf_cbh3(a):
        
    hf=[]
    hrxn=[]
    for i in range(len(results_hf.index)):
        if results_hf.index[i]==str(a):
            #hf.append(results_hf.iloc[i,0]-results_hf.iloc[i,-2])
            hf.append(results_hf.iloc[i,1]-results_hf.iloc[i,-2])
            hf.append(results_hf.iloc[i,3]-results_hf.iloc[i,-2])
            hf.append(results_hf.iloc[i,5]-results_hf.iloc[i,-2])
            
            hrxn.append(results_hf.iloc[i,2])
            hrxn.append(results_hf.iloc[i,4])
            hrxn.append(results_hf.iloc[i,6])
            
            #print(results_hf.index[i])
    #x.append(results_hf.index[species[a]])
    
    return hf,hrxn

#print(get_hf('^*CH_2^*CH^*CH_2')[0])

#print("'$\mathrm{" + results_o.index.to_list() + "}$'")
string_before="$\mathbf{"
string_end="}$"

ax0.plot(space_hf,get_hf_cbh3('^*CH_2^*CH^*CH_2')[0], linestyle='solid', marker='o',color=colors[0], markeredgecolor='w', markeredgewidth=2)
ax0.plot(space_hf,get_hf_cbh3('H_2C^*O_2CH_3')[0], linestyle='solid', marker='o',color=colors[1], markeredgecolor='w', markeredgewidth=2)
ax0.plot(space_hf,get_hf_cbh3('H_2C^*O^*O')[0], linestyle='solid', marker='o',color=colors[2], markeredgecolor='w', markeredgewidth=2)
ax0.plot(space_hf,get_hf_cbh3('H_2C^*O^*O')[0], linestyle='solid', marker='o',color=colors[2], markeredgecolor='w', markeredgewidth=2)

#ax0.plot(space_hf,get_hf_cbh3('H_2C^*O^*O')[0], linestyle='solid', marker='o',color=colors[2], markeredgecolor='w', markeredgewidth=2)

ax0.set_ylabel('$\mathrm{\Delta\Delta_fH\ (kJ\,mol^{-1})}$')
ax0.set_ylim([-4,4])

ax1.plot(space_hrxn,get_hf_cbh3('^*CH_2^*CH^*CH_2')[1])
ax1.plot(space_hrxn,get_hf_cbh3('H_2C^*O_2CH_3')[1])
ax1.plot(space_hrxn,get_hf_cbh3('H_2C^*O^*O')[1])
ax1.set_ylabel('$\mathrm{\Delta H_{rxn}\ (kJ\,mol^{-1})}$')



#ax0.xaxis.set_label_position('top') 
#ax0.xaxis.tick_top()
# ax0.set_xticks(list(np.arange(len(binding_o))))
# font_label={'fontsize': 16,
#  'fontweight': 'bold'}
# box={'facecolor':'w'}
# ax0.set_xticklabels((string_before + pd.Series(results_o.index.to_list()) + string_end).tolist(), rotation=40,va='center',  fontdict=font_label,bbox=box)
# 
# ax0.set_title('$\mathbf{^*O-binding\ adsorbates}$', fontsize=26)

# 

# ax0.bar(no-0.3+100,results_o.iloc[0,0] , width=0.3, color=colors[0], edgecolor='k', linewidth=3,label='$\mathrm{original}$')
# ax0.bar(no+100,results_o.iloc[0,1] , width=0.3, color=colors[1], edgecolor='k', linewidth=3,label='$\mathrm{CBH-1}$')
# ax0.bar(no+0.3+100,results_o.iloc[0,3] , width=0.3, color=colors[2], edgecolor='k', linewidth=3,label='$\mathrm{CBH-2}$')
# ax0.legend(loc='upper right')

# #ax0.plot((-2,5),(0,0),linestyle='solid',color='k')
# ax0.plot((-1,len(binding_o)),(0,0),linestyle='solid',color='k')
# ax0.plot((-1,len(binding_o)),(30,30),linestyle='dashed',color='k')
# ax0.plot((-1,len(binding_o)),(-30,-30),linestyle='dashed',color='k')

# ax0.set_xlim([-0.5,len(binding_o)])

# for no,spcs in enumerate(binding_o):
#     #ax0.bar(no-0.3,results_o.iloc[no,0] , width=0.3, color=colors[0], edgecolor='k', linewidth=3)
#     ax0.bar(no,results_o.iloc[no,1]-results_o.iloc[no,0] , width=0.3, color=colors[1], edgecolor='k', linewidth=3)
#     #ax0.bar(no+0.3,results_o.iloc[no,3]-results_o.iloc[no,1] , width=0.3, color=colors[2], edgecolor='k', linewidth=3)


#plt.savefig('Delta_CBH.pdf', bbox_inches='tight',transparent=False)