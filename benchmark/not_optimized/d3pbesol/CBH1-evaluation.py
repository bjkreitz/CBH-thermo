
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


CBH1_matrix=pd.read_csv('QE_CBH1_matrix', sep="\t", header=0, index_col=0)
CBH1_matrix=CBH1_matrix.fillna(0)
matrix=CBH1_matrix.to_numpy()

CBH_products=pd.read_csv('QE_CBH1_products', sep="\t", header=0, index_col=0)
DFT_energies=pd.read_csv('QE_CBH1_DFT_energies', sep="\t", header=0, index_col=0)

exp_hf=pd.read_csv('experiment_hf_CBH1_0K', sep="\t", header=0, index_col=0)

target_vec=CBH_products['combined'].to_numpy()
ref_vec=DFT_energies['combined'].to_numpy()

intermediate=np.dot(matrix,target_vec)
#intermediate=CBH1_matrix.dot().to_numpy()
DFT_heat_of_reaction=-ref_vec+intermediate
DFT_heat_of_reaction*=96.485

exp_vec=exp_hf['experiment'].to_numpy()
#exp_intermediate=CBH1_matrix.dot()
exp_intermediate=np.dot(matrix,exp_vec)
hf_ads=-DFT_heat_of_reaction+exp_intermediate

# reasonable_hrxn=[]

# for i in range(len(intermediate)):
#     if DFT_heat_of_reaction[i]<1e3:
#        reasonable_hrxn.append(abs(DFT_heat_of_reaction[i]))

# average_hrxn=np.mean(reasonable_hrxn)

# #Cancellation of zero point energies

# zpe_intermediate=CBH1_matrix.dot(CBH_products['ZPE'].to_numpy()).to_numpy()
# zpe_heat_of_reaction=-DFT_energies['ZPE']+zpe_intermediate
# zpe_heat_of_reaction*=96.485


# average_zpe_hrxn=np.mean(abs(zpe_heat_of_reaction))