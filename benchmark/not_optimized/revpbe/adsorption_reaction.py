
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

stoich_matrix=pd.read_csv('old_approach/stoich_matrix.txt', sep="\t", header=0, index_col=0)
ref_data=pd.read_csv('old_approach/energies_vec.txt', sep="\t", header=0, index_col=0)
ref_enthalpy=pd.read_csv('old_approach/enthalpy_vec.txt', sep="\t", header=0, index_col=0)

dft_data=pd.read_csv('old_approach/dft_vec.txt', sep="\t", header=0, index_col=0)

slab_energy=-366375.2378
eV_to_kJmol=96.485
E=np.ones(len(stoich_matrix['CH_4^*']))

slab_vec=E*slab_energy

ref_energy=ref_data['spe'].to_numpy()+ref_data['zpe'].to_numpy()
dft_energy=dft_data['spe'].to_numpy()+dft_data['zpe'].to_numpy()
enthalpy_ATcT=np.array([-66.557,-238.929,0])

nu=stoich_matrix.to_numpy()
hf=(dft_energy-slab_vec-np.dot(nu,ref_energy))*eV_to_kJmol+np.dot(nu,enthalpy_ATcT)
