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

matrix=pd.read_csv('Old_approach_matrix.txt', sep="\t", header=0, index_col=0)
matrix=matrix.fillna(0)

node_count=matrix.sum(axis=0).to_numpy()

nodesize=np.zeros(len(node_count))
for i in range(len(nodesize)):
    nodesize[i]=(max(node_count[i],1))

#Create the graph          
G = nx.MultiGraph()

for i in range(len(matrix.columns)):
    G.add_node(matrix.columns[i])
    
for j in range(len(matrix.index)):
    for i in range(len(matrix.columns)):
            key = G.add_edge(str(matrix.columns[i]), str(matrix.index[j]))

gas_names=['$\mathbf{CH_4}$','$\mathbf{H_2}$','$\mathbf{H_2O}$']

color_map = []
nodesize=[]
labels={}
for node in G: 
    if node in gas_names:
        color_map.append('r')
        nodesize.append(600)
        labels[node]=node
    else:
        color_map.append('b')
        nodesize.append(10)

pos = nx.spring_layout(G, seed=500)
a=0.15
for x in pos:
    if x in gas_names[0]:
        pos[x]=[-a,a]
    if x in gas_names[1]:
        pos[x]=[a,a]
    if x in gas_names[2]:
        pos[x]=[0,-a]
        
        
#print(pos['$\mathbf{CH_4}$'])   
#,node_size=new_nodesize*25,node_color=color_map
fig, ax = plt.subplots(figsize=(7, 7))
# Visualize graph components
nx.draw_networkx_edges(G, pos,connectionstyle="arc3", arrows=False, width=0.2)
nx.draw_networkx_nodes(G, pos, node_size=nodesize,node_color=color_map,)
#label_options = {"ec": "k", "fc": "white", "alpha": 0.7}
nx.draw_networkx_labels(G, pos,labels, font_size=12,verticalalignment='center')

patch_gas = mpatches.Patch( facecolor='r', edgecolor='k', label='$\mathrm{gas\ thermochemistry\ (ATcT)}$')
patch_adsorbate = mpatches.Patch(facecolor='b', edgecolor='k', label='$\mathrm{DFT\ adsorbate\ thermochemistry}$')

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles=[patch_gas, patch_adsorbate], loc='lower right',bbox_to_anchor=(1,-0.1), ncol=1)

#plt.legend()
plt.axis('off')
plt.savefig('old_network.png',dpi=600)