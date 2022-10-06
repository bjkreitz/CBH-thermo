
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


CBH1_matrix=pd.read_csv('QE_CBH1_matrix', sep="\t", header=0, index_col=0)
CBH1_matrix=CBH1_matrix.fillna(0)

CBH_products=pd.read_csv('QE_CBH1_products', sep="\t", header=0, index_col=0)
DFT_energies=pd.read_csv('QE_CBH1_DFT_energies', sep="\t", header=0, index_col=0)

exp_hf=pd.read_csv('experiment_hf', sep="\t", header=0, index_col=0)


#print(CBH1_matrix.iloc[0:5,:])
#print(CBH_products['combined'])

#a=CBH1_matrix.iloc[0:5,:]

intermediate=CBH1_matrix.dot(CBH_products['combined'].to_numpy())
#print(intermediate)
#intermediate=check.sum(axis=1)
#print(DFT_energies["combined"])
DFT_heat_of_reaction=-DFT_energies['combined']+intermediate
DFT_heat_of_reaction*=96.485

exp_intermediate=CBH1_matrix.dot(exp_hf['experiment'].to_numpy())
#exp_intermediate=exp_check.sum(axis=1)

hf_ads=-DFT_heat_of_reaction+exp_intermediate
#hf_ads/=4.184
