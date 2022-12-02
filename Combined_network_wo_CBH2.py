import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

plt.rcParams['figure.figsize'] = (20, 10)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.rc('axes', labelsize=16)
plt.rc('legend', fontsize=18)
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
plt.rcParams['legend.handletextpad'] = 0.4
plt.rcParams['legend.columnspacing'] = 0.5
plt.rcParams['legend.labelspacing'] = 0.3
plt.rcParams['legend.title_fontsize'] = 14
plt.rcParams['axes.formatter.limits'] = (-3, 6)

matrix=pd.read_csv('Old_approach_matrix.txt', sep="\t", header=0, index_col=0)
matrix=matrix.fillna(0)

node_count=matrix.sum(axis=0).to_numpy()

nodesize=np.zeros(len(node_count))
for i in range(len(nodesize)):
    nodesize[i]=(max(node_count[i],1))

#Create the graph          
H = nx.MultiGraph()

for i in range(len(matrix.columns)):
    H.add_node(matrix.columns[i])
    
for j in range(len(matrix.index)):
    for i in range(len(matrix.columns)):
            key = H.add_edge(str(matrix.columns[i]), str(matrix.index[j]))

gas_names=['$\mathbf{CH_4}$','$\mathbf{H_2}$','$\mathbf{H_2O}$']

color_map = []
nodesize=[]
labels={}
for node in H: 
    if node in gas_names:
        color_map.append('r')
        nodesize.append(800)
        labels[node]=node
    else:
        color_map.append('k')
        nodesize.append(30)

pos = nx.spring_layout(H, seed=500)
a=0.15
for x in pos:
    if x in gas_names[0]:
        pos[x]=[-a,a]
    if x in gas_names[1]:
        pos[x]=[a,a]
    if x in gas_names[2]:
        pos[x]=[0,-a]
        
import matplotlib.gridspec as gridspec        
gs = gridspec.GridSpec(nrows=1, ncols=2)
gs.update(wspace=0.2, hspace=0.4)

ax0 = plt.subplot(gs[0, 0])

nx.draw_networkx_edges(H, pos,connectionstyle="arc3", arrows=False, width=0.15)
nx.draw_networkx_nodes(H, pos, node_size=nodesize,node_color=color_map)

patch_gas = mpatches.Patch( facecolor='r', edgecolor='k', label='$\mathrm{\Delta_f H_{gas\, phase}^{ATcT}}$')
patch_adsorbate = mpatches.Patch(facecolor='k', edgecolor='k', label='$\mathrm{\Delta_f H_{adsorbate}^{direct}}$')

handles, labels = ax0.get_legend_handles_labels()
ax0.legend(handles=[patch_gas, patch_adsorbate], loc='center',bbox_to_anchor=(0.5,-0.05), ncol=2)
ax0.axis('off')

ax1 = plt.subplot(gs[0, 1])  

CBH1_matrix=pd.read_csv('QE_CBH1_matrix', sep="\t", header=0, index_col=0)
CBH1_matrix=CBH1_matrix.fillna(0)


diag=np.zeros((len(CBH1_matrix.columns),len(CBH1_matrix.columns)))
np.fill_diagonal(diag,0)

new=pd.DataFrame(diag,
                 columns=list(CBH1_matrix.columns),
                 index=list(CBH1_matrix.columns)
                 )

combined=pd.concat([new,CBH1_matrix])

empty=np.zeros((len(CBH1_matrix.index),len(combined.index)))
df_empty=pd.DataFrame(empty,
                 columns=list(combined.index),
                 index=list(CBH1_matrix.index),
                 )
df_transposed=df_empty.T

for j in range(len(df_transposed.index)):
    for i in range(len(df_transposed.columns)):
        if str(df_transposed.columns[i])==str(df_transposed.index[j]):
            df_transposed.iloc[j,i]=0
            
combined_2nd=pd.concat([combined,df_transposed],axis=1)  

abs_combined_2nd=combined_2nd.abs()
node_count=abs_combined_2nd.sum(axis=0).to_numpy()

nodesize=np.zeros(len(node_count))
for i in range(len(nodesize)):
    nodesize[i]=(max(node_count[i],1))

string_before="$\mathbf{"
string_end="}$"

mathrm_names=pd.Series(combined_2nd.index.to_list())

df=combined_2nd.rename(columns={x: string_before+x+string_end for x in mathrm_names},
                       index={x: string_before+x+string_end for x in mathrm_names})

def graph(a):
    
    #Create the graph          
    G = nx.MultiGraph()

    for i in range(len(df.columns)):
        G.add_node(df.columns[i])
        
    for j in range(len(df_transposed.index)):
        for i in range(len(df_transposed.columns)):
            if combined_2nd.iloc[j,i]!=0:
                key = G.add_edge(str(df.columns[i]), str(df.index[j]))
                
    #add some manual nodes for the gas phase anchors
    G.add_edge('$\mathbf{CH_4^*}$', '$\mathbf{CH_4}$')
    G.add_edge('$\mathbf{CH_3OH^*}$', '$\mathbf{CH_3OH}$')
    G.add_edge('$\mathbf{^*CH}$', '$\mathbf{CH_2I_2}$')
    G.add_edge('$\mathbf{^*CH_2}$', '$\mathbf{^*CH_3}$')
    G.add_edge('$\mathbf{^*CH_3}$', '$\mathbf{CH_3I}$')
    G.add_edge('$\mathbf{C_2H_4^*}$', '$\mathbf{C_2H_4}$')
    G.add_edge('$\mathbf{C_2H_6^*}$', '$\mathbf{C_2H_6}$')
    G.add_edge('$\mathbf{H_2O^*}$', '$\mathbf{H_2O}$')
    G.add_edge('$\mathbf{H_2CO^*}$', '$\mathbf{H_2CO}$')

    
    gas_names=['$\mathbf{CH_4}$','$\mathbf{CH_3OH}$','$\mathbf{CH_2I_2}$','$\mathbf{CH_3I}$',
              '$\mathbf{C_2H_4}$','$\mathbf{C_2H_6}$','$\mathbf{H_2O}$','$\mathbf{H_2CO}$']
    exp_names=['$\mathbf{CH_4^*}$','$\mathbf{CH_3OH^*}$','$\mathbf{^*CH}$','$\mathbf{^*CH_2}$',
               '$\mathbf{^*CH_3}$','$\mathbf{C_2H_4^*}$','$\mathbf{C_2H_6^*}$','$\mathbf{H_2O^*}$',
               '$\mathbf{H_2CO^*}$','$\mathbf{^*OH}$']

    color_map = []
    labels={}
    for node in G: 
        if node in gas_names:
                color_map.append('r')
                labels[node]=node
        elif node in exp_names:
            color_map.append('b')
            labels[node]=node
        else:
            color_map.append('k')

    anchors=np.ones(8)*5
    new_nodesize=np.append(nodesize,anchors)
    
    # Generate layout for visualization
    pos = nx.spring_layout(G,seed=a)

    # Visualize graph components
    nx.draw_networkx_edges(G, pos,connectionstyle="arc3", arrows=False, width=0.2)
    nx.draw_networkx_nodes(G, pos,node_size=new_nodesize*20,node_color=color_map)
    #nx.draw_networkx_labels(G, pos,labels, font_size=16,verticalalignment='top')
    
    patch_gas = mpatches.Patch( facecolor='r', edgecolor='k', label='$\mathrm{\Delta_f H_{gas\, phase}^{ATcT}}$')
    patch_exp = mpatches.Patch(facecolor='b', edgecolor='k', label='$\mathrm{\Delta_f H_{adsorbate}^{exp}}$')
    patch_CBH1 = mpatches.Patch(facecolor='k', edgecolor='k', label='$\mathrm{\Delta_f H_{adsorbate}^{CBH\u2010 1}}$')

    handles, labels = ax1.get_legend_handles_labels()
    ax1.legend(handles=[patch_gas, patch_exp, patch_CBH1], loc='center',bbox_to_anchor=(0.5,-0.05), ncol=4)
    
    ax1.axis('off')
    
    import string 
    ax0.text(0.0, 0.98, string.ascii_lowercase[0], transform=ax0.transAxes, size=20, weight='bold')
    ax1.text(0.0, 0.98, string.ascii_lowercase[1], transform=ax1.transAxes, size=20, weight='bold')
    plt.savefig('network_empty.png',dpi=600, bbox_inches='tight')
    plt.show()
    return 

graph(1056)
