
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


CBH_matrix=pd.read_csv('QE_CBH2_matrix', sep="\t", header=0, index_col=0)
CBH_matrix=CBH_matrix.fillna(0)

CBH_products=pd.read_csv('QE_CBH2_products', sep="\t", header=0, index_col=0)
DFT_energies=pd.read_csv('QE_CBH2_DFT_energies', sep="\t", header=0, index_col=0)

exp_hf=pd.read_csv('experiment_hf_CBH2_0K', sep="\t", header=0, index_col=0)

check=CBH_matrix.dot(CBH_products['combined'].to_numpy()).to_numpy()

#print(CBH_products["combined"])
#print(CBH_products['combined'])
#intermediate=check.sum(axis=1)
#print(CBH1_matrix['C2H4_vdW'])
#print(intermediate)

#print(DFT_energies['combined'])

DFT_heat_of_reaction=-DFT_energies['combined'].to_numpy()+check
DFT_heat_of_reaction*=96.485

exp_check=CBH_matrix.dot(exp_hf['experiment'].to_numpy())
#exp_intermediate=exp_check.sum(axis=1)

hf_ads=-DFT_heat_of_reaction+exp_check
#hf_ads/=4.184


reasonable_hrxn=[]

for i in range(len(check)):
    if DFT_heat_of_reaction[i]<1e3:
       reasonable_hrxn.append(abs(DFT_heat_of_reaction[i]))

average_hrxn=np.mean(reasonable_hrxn)


zpe_intermediate=CBH_matrix.dot(CBH_products['ZPE'].to_numpy()).to_numpy()
#print(intermediate)
#intermediate=check.sum(axis=1)
#print(DFT_energies["combined"])
zpe_heat_of_reaction=-DFT_energies['ZPE']+zpe_intermediate
zpe_heat_of_reaction*=96.485

average_zpe_hrxn=np.mean(abs(zpe_heat_of_reaction))