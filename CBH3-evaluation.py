
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


CBH_matrix=pd.read_csv('data/QE_CBH3_matrix', sep="\t", header=0, index_col=0)
CBH_matrix=CBH_matrix.fillna(0)

CBH_products=pd.read_csv('data/QE_CBH3_products', sep="\t", header=0, index_col=0)
DFT_energies=pd.read_csv('data/QE_CBH3_DFT_energies', sep="\t", header=0, index_col=0)

exp_hf=pd.read_csv('data/experiment_hf_CBH3_0K', sep="\t", header=0, index_col=0)

check=CBH_matrix.dot(CBH_products['combined'].to_numpy())

DFT_heat_of_reaction=-DFT_energies['combined'].to_numpy()+check
DFT_heat_of_reaction*=96.485

exp_check=CBH_matrix.dot(exp_hf['experiment'].to_numpy())

hf_ads=-DFT_heat_of_reaction+exp_check
reasonable_hrxn=[]

for i in range(len(check)):
    if DFT_heat_of_reaction[i]<1e3:
       reasonable_hrxn.append(abs(DFT_heat_of_reaction[i]))

average_hrxn=np.mean(reasonable_hrxn)

zpe_intermediate=CBH_matrix.dot(CBH_products['ZPE'].to_numpy()).to_numpy()
zpe_heat_of_reaction=-DFT_energies['ZPE']+zpe_intermediate
zpe_heat_of_reaction*=96.485

average_zpe_hrxn=np.mean(abs(zpe_heat_of_reaction))