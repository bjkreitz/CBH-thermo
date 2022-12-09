
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.rc('axes', labelsize=16)
plt.rc('legend', fontsize=16)
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
plt.rcParams['hatch.linewidth'] = 3.0  # previous svg hatch linewidth

CBH1_matrix=pd.read_csv('QE_CBH1_matrix', sep="\t", header=0, index_col=0)
CBH1_matrix=CBH1_matrix.fillna(0)


CBH2_matrix=pd.read_csv('QE_CBH2_matrix', sep="\t", header=0, index_col=0)
CBH2_matrix=CBH2_matrix.fillna(0)

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

#replace the existing species with the CBH2 level
for i in range(len(CBH2_matrix.index)):
    for k in range(len(combined_2nd.index)):
        if CBH2_matrix.index[i] == combined_2nd.index[k]:
            #print(combined_2nd.index[k])
            combined_2nd.iloc[k,:]=0     
            for j in range(len(CBH2_matrix.columns)):
                for l in range(len(combined_2nd.columns)):
                    if CBH2_matrix.index[i] == combined_2nd.index[k]:
                        if CBH2_matrix.columns[j] == combined_2nd.columns[l]:
                            combined_2nd.iloc[k,l]=CBH2_matrix.iloc[i,j]    


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

#Create the graph          
G = nx.MultiGraph()

for i in range(len(df.columns)):
    G.add_node(df.columns[i])
    
for j in range(len(df_transposed.index)):
    for i in range(len(df_transposed.columns)):
        if combined_2nd.iloc[j,i]!=0:
            key = G.add_edge(str(df.columns[i]), str(df.index[j]))
            #key = G.add_edge(str(df.columns[i]), str(df.index[j]), weight=df.iloc[j,i])
            
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
#G.add_edge('$\mathbf{^*OH}$', '$\mathbf{OH}$')

CBH2_names=(string_before + pd.Series(CBH2_matrix.index.to_list()) + string_end).tolist()
gas_names=['$\mathbf{CH_4}$','$\mathbf{CH_3OH}$','$\mathbf{CH_2I_2}$','$\mathbf{CH_3I}$',
          '$\mathbf{C_2H_4}$','$\mathbf{C_2H_6}$','$\mathbf{H_2O}$','$\mathbf{H_2CO}$']
exp_names=['$\mathbf{CH_4^*}$','$\mathbf{CH_3OH^*}$','$\mathbf{^*CH}$','$\mathbf{^*CH_2}$',
            '$\mathbf{^*CH_3}$','$\mathbf{C_2H_4^*}$','$\mathbf{C_2H_6^*}$','$\mathbf{H_2O^*}$',
            '$\mathbf{H_2CO^*}$','$\mathbf{^*OH}$']

color_map = []
labels={}
for node in G: 
    if node in CBH2_names:
        color_map.append('b')
    elif node in gas_names:
            color_map.append('y')
            labels[node]=node
    elif node in exp_names:
        color_map.append('r')
        labels[node]=node
    else:
        color_map.append('g')

anchors=np.ones(8)*50
new_nodesize=np.append(nodesize,anchors)

# Generate layout for visualization
pos = nx.spring_layout(G,seed=1008)

fig, ax = plt.subplots(figsize=(12, 12))
# Visualize graph components
nx.draw_networkx_edges(G, pos,connectionstyle="arc3", arrows=False, width=0.4)
nx.draw_networkx_nodes(G, pos,node_size=new_nodesize*25,node_color=color_map)
nx.draw_networkx_labels(G, pos,labels,font_size=20,verticalalignment='top')

patch_gas = mpatches.Patch( facecolor='y', edgecolor='k', label='$\mathrm{gas\u2010 phase\, thermochemistry\ (ATcT)}$')
patch_exp = mpatches.Patch(facecolor='r', edgecolor='k', label='$\mathrm{exp.\, adsorbate\, thermochemistry}$')
patch_CBH1 = mpatches.Patch(facecolor='g', edgecolor='k', label='$\mathrm{CBH\u2010 1\, adsorbate\, thermochemistry}$')
patch_CBH2 = mpatches.Patch(facecolor='b', edgecolor='k', label='$\mathrm{CBH\u2010 2\, adsorbate\, thermochemistry}$')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=[patch_gas, patch_exp, patch_CBH1,patch_CBH2], loc='lower right',bbox_to_anchor=(1,-0.05), ncol=2)

plt.axis('off')
plt.savefig('CBH_network.png',dpi=600, bbox_inches='tight')