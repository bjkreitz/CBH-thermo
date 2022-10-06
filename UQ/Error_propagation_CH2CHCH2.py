"""This will be a very hacky attempt to propagate the uncertainty through the different CBH rungs
The example molecule here is CH3*CHCH3. 
All rungs will be in one script. Hope it's not getting too messy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


CBH1_matrix = pd.read_csv("QE_CBH1_matrix", sep="\t", header=0, index_col=0)
CBH1_matrix = CBH1_matrix.fillna(0)

CBH1_matrix.loc["CH3*CHCH3"].to_numpy()

#####CBH1 level

CBH_products = pd.read_csv("QE_CBH1_products", sep="\t", header=0, index_col=0)
DFT_energies = pd.read_csv("QE_DFT_energies", sep="\t", header=0, index_col=0)

dft_ch3chch3 = DFT_energies["combined"].loc["CH3*CHCH3"]
dft_ch4 = CBH_products["combined"].loc["CH4_vdW"]
dft_c2h6 = CBH_products["combined"].loc["C2H6_vdW"]
dft_ch3 = CBH_products["combined"].loc["*CH3"]

dft_hrxn = dft_ch3 + 2 * dft_c2h6 - 2 * dft_ch4 - dft_ch3chch3
dft_hrxn *= 96.485

exp_hf = pd.read_csv("experiment_hf", sep="\t", header=0, index_col=0)

exp_ch4 = exp_hf["experiment"].loc["CH4_vdW"]
exp_c2h6 = exp_hf["experiment"].loc["C2H6_vdW"]
exp_ch3 = exp_hf["experiment"].loc["*CH3"]

hf_ads = -dft_hrxn - 2 * exp_ch4 + 2 * exp_c2h6 + exp_ch3

bee_ch4 = pd.read_csv("BEE/CH4.dat", sep=",", header=None)
bee_ch3 = pd.read_csv("BEE/CH3.dat", sep=",", header=None)
bee_c2h6 = pd.read_csv("BEE/CH3CH3.dat", sep=",", header=None)
bee_ch2chch2 = pd.read_csv("BEE/CH2CHCH2.dat", sep=",", header=None)
bee_ch2ch3 = pd.read_csv("BEE/CH2CH3.dat", sep=",", header=None)
bee_ch3chch3 = pd.read_csv("BEE/CH3CHCH3.dat", sep=",", header=None)
bee_ch3chch2 = pd.read_csv("BEE/CH3CHCH2-bi.dat", sep=",", header=None)

########CBH2 level
CBH2_products = pd.read_csv("QE_CBH2_products", sep="\t", header=0, index_col=0)
DFT_CBH2_energies = pd.read_csv("QE_CBH2_DFT_energies", sep="\t", header=0, index_col=0)

dft_ch3chch2 = DFT_CBH2_energies["combined"].loc["CH3*CH*CH2"]
dft_ch2ch3 = CBH2_products["combined"].loc["*CH2CH3"]
dft_c2h6 = CBH2_products["combined"].loc["C2H6_vdW"]
dft_ch3chch3= CBH2_products["combined"].loc["CH3*CHCH3"]

dft_hrxn_cbh2 = dft_ch3chch3 + dft_ch2ch3 - dft_c2h6 - dft_ch3chch2
dft_hrxn_cbh2 *= 96.485

exp_hf_cbh2 = pd.read_csv("experiment_hf_CBH2", sep="\t", header=0, index_col=0)

exp_c2h6 = exp_hf_cbh2["experiment"].loc["C2H6_vdW"]
exp_ch2ch3 = exp_hf_cbh2["experiment"].loc["*CH2CH3"]
exp_ch3chch3 = exp_hf_cbh2["experiment"].loc["CH3*CHCH3"]

hf_ads_cbh2 = -dft_hrxn_cbh2 - exp_c2h6 + exp_ch2ch3 + exp_ch3chch3

#####*CH2CH3

dft_hrxn = dft_ch3 + dft_c2h6 - dft_ch4 - dft_ch2ch3
dft_hrxn *= 96.485
hf_ads = -dft_hrxn - exp_ch4 +  exp_c2h6 + exp_ch3

# Now subject everything to an uncertainty from the BEE
rydberg_to_eV = 13.6056980659  # convert Ry/molecule to eV/molecule

N_bee = 2000
uq_dft_hrxn_ch3chch3 = np.zeros(N_bee)
uq_hf_ads_ch3chch3 = np.zeros(N_bee)

uq_dft_hrxn_ch3chch2 = np.zeros(N_bee)
uq_hf_ads_ch3chch2 = np.zeros(N_bee)

uq_dft_hrxn_ch2ch3 = np.zeros(N_bee)
uq_hf_ads_ch2ch3 = np.zeros(N_bee)

for i in range(N_bee):
    uq_dft_hrxn_ch3chch3[i] = (
         (dft_ch3 - bee_ch3[i] * rydberg_to_eV)
        + 2 * (dft_c2h6 - bee_c2h6[i] * rydberg_to_eV)
        - 2 * (dft_ch4 - bee_ch4[i] * rydberg_to_eV)
        - (dft_ch3chch3 - bee_ch3chch3[i] * rydberg_to_eV)
    )
    uq_dft_hrxn_ch3chch3[i] *= 96.485

    uq_hf_ads_ch3chch3[i] = -uq_dft_hrxn_ch3chch3[i] - 2 * exp_ch4 + 2 * exp_c2h6 + exp_ch3

    uq_dft_hrxn_ch2ch3[i] = (
         (dft_ch3 - bee_ch3[i] * rydberg_to_eV)
        + (dft_c2h6 - bee_c2h6[i] * rydberg_to_eV)
        - (dft_ch4 - bee_ch4[i] * rydberg_to_eV)
        - (dft_ch2ch3 - bee_ch2ch3[i] * rydberg_to_eV)
    )
    uq_dft_hrxn_ch2ch3[i] *= 96.485

    uq_hf_ads_ch2ch3[i] = -uq_dft_hrxn_ch2ch3[i] - exp_ch4 + exp_c2h6 + exp_ch3
    
    uq_dft_hrxn_ch3chch2[i] = (
         (dft_ch2ch3 - bee_ch2ch3[i] * rydberg_to_eV)
        - (dft_c2h6 - bee_c2h6[i] * rydberg_to_eV)
        +  (dft_ch3chch3 - bee_ch3chch3[i] * rydberg_to_eV)
        - (dft_ch3chch2 - bee_ch3chch2[i] * rydberg_to_eV)
    )
    uq_dft_hrxn_ch3chch2[i] *= 96.485

    uq_hf_ads_ch3chch2[i] = -uq_dft_hrxn_ch3chch2[i] - exp_c2h6 + uq_hf_ads_ch2ch3[i] + uq_hf_ads_ch3chch3[i] 
    
df=pd.DataFrame(np.array([uq_hf_ads_ch3chch3, uq_hf_ads_ch3chch2, uq_hf_ads_ch2ch3]).T, columns=['hf_ch3chch3', 'hf_ch3chch2', 'hf_ch2ch3'])
df.to_csv('uq_hf_test.txt', sep='\t', index=False)
  

