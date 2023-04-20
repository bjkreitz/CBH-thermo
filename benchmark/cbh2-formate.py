
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


functionals=['beef','pbe','rpbe','pw91','d3rpbe','d3pbe','d3revpbe','d3pbesol','revpbe']
reaction_enthalpies=[]
enthalpies=[]
for i in functionals:
    folder='not_optimized/' + str(i) +'/'

    CBH1_matrix=pd.read_csv(folder+'QE_CBH2_matrix', sep="\t", header=0, index_col=0)
    CBH1_matrix=CBH1_matrix.fillna(0)
    matrix=CBH1_matrix.to_numpy()

    CBH_products=pd.read_csv(folder+'QE_CBH2_products', sep="\t", header=0, index_col=0)
    DFT_energies=pd.read_csv(folder+'QE_CBH2_DFT_energies', sep="\t", header=0, index_col=0)

    exp_hf=pd.read_csv(folder+'experiment_hf_CBH2_0K', sep="\t", header=0, index_col=0)

    target_vec=CBH_products['combined'].to_numpy()
    ref_vec=DFT_energies['combined'].to_numpy()

    intermediate=np.dot(matrix,target_vec)
    DFT_heat_of_reaction=-ref_vec+intermediate
    DFT_heat_of_reaction*=96.485

    exp_vec=exp_hf['experiment'].to_numpy()
    exp_intermediate=np.dot(matrix,exp_vec)
    hf_ads=-DFT_heat_of_reaction+exp_intermediate
    reaction_enthalpies.append(DFT_heat_of_reaction[-1])
    enthalpies.append(hf_ads[-1])
    
