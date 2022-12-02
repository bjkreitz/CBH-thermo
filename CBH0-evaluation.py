
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


CBH0_matrix=pd.read_csv('QE_CBH0_matrix', sep="\t", header=0, index_col=0)
CBH0_matrix=CBH0_matrix.fillna(0)

CBH_products=pd.read_csv('QE_CBH0_products', sep="\t", header=0, index_col=0)
DFT_energies=pd.read_csv('QE_CBH0_DFT_energies', sep="\t", header=0, index_col=0)

#exp_hf=pd.read_csv('experiment_hf', sep="\t", header=0, index_col=0)


#print(CBH1_matrix.iloc[0:5,:])
#print(CBH_products['combined'])

#a=CBH1_matrix.iloc[0:5,:]

intermediate=CBH0_matrix.dot(CBH_products['combined'].to_numpy()).to_numpy()
#print(intermediate)
#intermediate=check.sum(axis=1)
#print(DFT_energies["combined"])
#print(intermediate.)
#for i in range(len(intermediate[:,0])):
#    print(i)
    
DFT_heat_of_reaction=-DFT_energies['combined']+intermediate
DFT_heat_of_reaction*=96.485

#exp_intermediate=CBH1_matrix.dot(exp_hf['experiment'].to_numpy())
#exp_intermediate=exp_check.sum(axis=1)

#hf_ads=-DFT_heat_of_reaction+exp_intermediate
#hf_ads/=4.184

reasonable_hrxn=[]

for i in range(len(intermediate)):
    if DFT_heat_of_reaction[i]<1e3:
       reasonable_hrxn.append(abs(DFT_heat_of_reaction[i]))


average_hrxn=np.mean(reasonable_hrxn)

zpe_intermediate=CBH0_matrix.dot(CBH_products['ZPE'].to_numpy()).to_numpy()
#print(intermediate)
#intermediate=check.sum(axis=1)
#print(DFT_energies["combined"])
zpe_heat_of_reaction=-DFT_energies['ZPE']+zpe_intermediate
zpe_heat_of_reaction*=96.485

average_zpe_hrxn=np.mean(abs(zpe_heat_of_reaction))