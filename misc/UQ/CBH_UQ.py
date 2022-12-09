"""This will be a very hacky attempt to propagate the uncertainty through the different CBH rungs
The example molecule here is *CH2*CH*CH2. 
All rungs will be in one script. Hope it's not getting too messy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

CBH1_matrix = pd.read_csv("QE_CBH1_matrix", sep="\t", header=0, index_col=0)
CBH1_matrix = CBH1_matrix.fillna(0)

CBH1_matrix.loc["*CH2*CH*CH2"].to_numpy()

#####CBH1 level

CBH_products = pd.read_csv("QE_CBH1_products", sep="\t", header=0, index_col=0)
DFT_energies = pd.read_csv("QE_DFT_energies", sep="\t", header=0, index_col=0)

dft_ch2chch2 = DFT_energies["combined"].loc["*CH2*CH*CH2"]
dft_ch4 = CBH_products["combined"].loc["CH4_vdW"]
dft_c2h6 = CBH_products["combined"].loc["C2H6_vdW"]
dft_ch3 = CBH_products["combined"].loc["*CH3"]

dft_hrxn = 3 * dft_ch3 + 2 * dft_c2h6 - 4 * dft_ch4 - dft_ch2chch2
dft_hrxn *= 96.485

exp_hf = pd.read_csv("experiment_hf", sep="\t", header=0, index_col=0)

exp_ch4 = exp_hf["experiment"].loc["CH4_vdW"]
exp_c2h6 = exp_hf["experiment"].loc["C2H6_vdW"]
exp_ch3 = exp_hf["experiment"].loc["*CH3"]

hf_ads = -dft_hrxn - 4 * exp_ch4 + 2 * exp_c2h6 + 3 * exp_ch3

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

dft_ch2chch2 = DFT_CBH2_energies["combined"].loc["*CH2*CH*CH2"]
dft_ch2ch3 = CBH2_products["combined"].loc["*CH2CH3"]
dft_c2h6 = CBH2_products["combined"].loc["C2H6_vdW"]
dft_ch3chch3= CBH2_products["combined"].loc["CH3*CHCH3"]

dft_hrxn_cbh2 = dft_ch3chch3 + 2 * dft_ch2ch3 - 2 * dft_c2h6 - dft_ch2chch2
dft_hrxn_cbh2 *= 96.485

exp_hf_cbh2 = pd.read_csv("experiment_hf_CBH2", sep="\t", header=0, index_col=0)

exp_c2h6 = exp_hf_cbh2["experiment"].loc["C2H6_vdW"]
exp_ch2ch3 = exp_hf_cbh2["experiment"].loc["*CH2CH3"]
exp_ch3chch3 = exp_hf_cbh2["experiment"].loc["CH3*CHCH3"]

hf_ads_cbh2 = -dft_hrxn_cbh2 - 2 * exp_c2h6 + 2 * exp_ch2ch3 + exp_ch3chch3

#######CBH3 level
CBH3_products = pd.read_csv("QE_CBH3_products", sep="\t", header=0, index_col=0)
DFT_CBH3_energies = pd.read_csv("QE_CBH3_DFT_energies", sep="\t", header=0, index_col=0)

dft_ch2chch2 = DFT_CBH3_energies["combined"].loc["*CH2*CH*CH2"]
dft_ch3chch3= CBH3_products["combined"].loc["CH3*CHCH3"]
dft_ch3chch2 = CBH3_products["combined"].loc["CH3*CH*CH2"]

dft_hrxn_cbh3 = 2*dft_ch3chch2- dft_ch3chch3 - dft_ch2chch2
dft_hrxn_cbh3 *= 96.485

exp_hf_cbh3 = pd.read_csv("experiment_hf_CBH3", sep="\t", header=0, index_col=0)

exp_ch3chch3 = exp_hf_cbh3["experiment"].loc["CH3*CHCH3"]
exp_ch3chch2 = exp_hf_cbh3["experiment"].loc["CH3*CH*CH2"]

hf_ads_cbh3 = -dft_hrxn_cbh3 - exp_ch3chch3 + 2* exp_ch3chch2

# Now subject everything to an uncertainty from the BEE
rydberg_to_eV = 13.6056980659  # convert Ry/molecule to eV/molecule

N_bee = 2000
uq_dft_hrxn = np.zeros(N_bee)
uq_hf_ads = np.zeros(N_bee)

uq_dft_hrxn_cbh2 = np.zeros(N_bee)
uq_hf_ads_cbh2 = np.zeros(N_bee)

uq_dft_hrxn_cbh3 = np.zeros(N_bee)
uq_hf_ads_cbh3 = np.zeros(N_bee)

uq_lower_rung = pd.read_csv("uq_hf_test.txt", sep="\t", header=0)

for i in range(N_bee):
    uq_dft_hrxn[i] = (
        3 * (dft_ch3 - bee_ch3[i] * rydberg_to_eV)
        + 2 * (dft_c2h6 - bee_c2h6[i] * rydberg_to_eV)
        - 4 * (dft_ch4 - bee_ch4[i] * rydberg_to_eV)
        - (dft_ch2chch2 - bee_ch2chch2[i] * rydberg_to_eV)
    )
    uq_dft_hrxn[i] *= 96.485

    uq_hf_ads[i] = -uq_dft_hrxn[i] - 4 * exp_ch4 + 2 * exp_c2h6 + 3 * exp_ch3
    
    uq_dft_hrxn_cbh2[i] = (
        2 * (dft_ch2ch3 - bee_ch2ch3[i] * rydberg_to_eV)
        - 2* (dft_c2h6 - bee_c2h6[i] * rydberg_to_eV)
        +  (dft_ch3chch3 - bee_ch3chch3[i] * rydberg_to_eV)
        - (dft_ch2chch2 - bee_ch2chch2[i] * rydberg_to_eV)
    )
    uq_dft_hrxn_cbh2[i] *= 96.485

    uq_hf_ads_cbh2[i] = -uq_dft_hrxn_cbh2[i] - 2 * exp_c2h6 + 2 * uq_lower_rung['hf_ch2ch3'][i] + uq_lower_rung['hf_ch3chch3'][i]
    
    uq_dft_hrxn_cbh3[i] = (
        2 * (dft_ch3chch2 - bee_ch3chch2[i] * rydberg_to_eV)
        -  (dft_ch3chch3 - bee_ch3chch3[i] * rydberg_to_eV)
        - (dft_ch2chch2 - bee_ch2chch2[i] * rydberg_to_eV)
    )
    uq_dft_hrxn_cbh3[i] *= 96.485

    uq_hf_ads_cbh3[i] = -uq_dft_hrxn_cbh3[i] - uq_lower_rung['hf_ch3chch3'][i] +2 *uq_lower_rung['hf_ch3chch2'][i]

import matplotlib.gridspec as gridspec

# Makes the diagrams look nice and shiny
plt.rcParams["figure.figsize"] = (7, 6)
plt.rcParams["axes.linewidth"] = 2
plt.rc("xtick", labelsize=14)
plt.rc("ytick", labelsize=14)
plt.rc("axes", labelsize=16)
plt.rc("legend", fontsize=14)
plt.rcParams["lines.markersize"] = 10
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams["xtick.major.size"] = 10
plt.rcParams["xtick.major.width"] = 2
plt.rcParams["ytick.major.size"] = 10
plt.rcParams["ytick.major.width"] = 2
plt.rcParams["legend.edgecolor"] = "k"
plt.rcParams["axes.unicode_minus"] = False
plt.rcParams["legend.framealpha"] = 1
plt.rcParams["xtick.major.pad"] = 8
plt.rcParams["ytick.major.pad"] = 8
plt.rcParams["legend.handletextpad"] = 0.4
plt.rcParams["legend.columnspacing"] = 0.5
plt.rcParams["legend.labelspacing"] = 0.3
plt.rcParams["legend.title_fontsize"] = 14
plt.rcParams["axes.formatter.limits"] = (-3, 6)

original = pd.read_csv("h-CH2CHCH2_ads_bee.txt", sep="\t", header=0)

gs = gridspec.GridSpec(nrows=1, ncols=1)
gs.update(wspace=0.3, hspace=0.2)

ax0 = plt.subplot(gs[0, 0])

zero = np.zeros(N_bee)
one = np.zeros(N_bee) + 1
two = np.zeros(N_bee) + 2
three = np.zeros(N_bee) + 3

ax0.plot(zero,original["Hf"], color="b", marker="o", linestyle="None",  markersize=5,  alpha=0.05)
ax0.plot( one, uq_hf_ads, color="b", marker="o", linestyle="None",  markersize=5,  alpha=0.05)
ax0.plot(two, uq_hf_ads_cbh2, color="b", marker="o", linestyle="None",  markersize=5,  alpha=0.05)
ax0.plot(three, uq_hf_ads_cbh3, color="b", marker="o", linestyle="None",  markersize=5,  alpha=0.05)

ax0.plot(0,-53.17345373055372, color="r", marker="o", linestyle="None",  markersize=10, label='$\mathrm{\Delta_fH}$')
ax0.plot(1,hf_ads, color="r", marker="o", linestyle="None",  markersize=10)
ax0.plot(2,hf_ads_cbh2, color="r", marker="o", linestyle="None",  markersize=10)
ax0.plot(3,hf_ads_cbh3, color="r", marker="o", linestyle="None",  markersize=10)

patch = mpatches.Patch(facecolor='b',alpha=0.5, edgecolor='k', label='$\mathrm{BEEF\ UQ}$')

ax0.set_xticks([0, 1, 2, 3])
ax0.set_xticklabels(['$\mathrm{original}$\n$\mathrm{-53.2\, kJ\,mol^{-1}}$', '$\mathrm{CBH1}$\n$\mathrm{-128.5\, kJ\,mol^{-1}}$', '$\mathrm{CBH2}$\n$\mathrm{-123.6\, kJ\,mol^{-1}}$','$\mathrm{CBH3}$\n$\mathrm{-123.6\, kJ\,mol^{-1}}$' ])
ax0.set_ylabel('$\mathrm{heat\ of\ formation\ (kJ\,mol^{-1}) }$')
ax0.set_title('$\mathbf{*CH_2*CH*CH_2}$', size=20)

handles, labels = ax0.get_legend_handles_labels()
ax0.legend(handles=[handles[0],patch], loc='upper right', ncol=1)

plt.savefig('CBH_uncertainty.pdf',bbox_inches='tight',transparent=False)