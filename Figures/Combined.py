import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.rcParams['figure.figsize'] = (14, 6)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.rc('axes', labelsize=18)
plt.rc('legend', fontsize=16)
plt.rcParams['lines.markersize'] = 10
plt.rcParams['lines.linewidth'] = 3
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
plt.rcParams['legend.handletextpad'] = 0.2
plt.rcParams['legend.columnspacing'] = 0.1
plt.rcParams['legend.labelspacing'] = 0.1
plt.rcParams['legend.title_fontsize'] = 14
plt.rcParams['axes.formatter.limits'] = (-3, 6)

results=pd.read_csv('../CBH_results.txt', sep="\t", header=0, index_col=0)

binding_o=['^*OCH_3','H_2C^*O_2CH_3','^*OCH_2CH_3','HCO^*O','^*OCH_2OH','HC^*O_3']

binding_c3=['^*CCHCH_2','^*CHCHCH_2','^*CHCHCH_3','^*CH_2CH_2CH_3',
           'CH_2^*CCH_3','CH_3^*CHCH_3','^*CCCH_2',
           '^*CCH_2CH_3','CH_3CH_2^*CO','CH_3^*CHOH',
           '^*CHCCH_2','^*CHCH_2CH_3','CH_3^*CCH_3']

binding_c=['^*CCH_2','^*CCH_3','^*COH','^*CH_2CH_3','H_2^*COH','^*CHCH_3',
           'H^*CO','H^*COH','^*COOH','CH_3^*CO','^*CHCO','^*CCH_2OH','^*CCHO','^*CCO','CH_3^*CHOH',
           'CH_3^*COH','^*CHCH_2']

binding_c_all=['^*CCH_2','^*CCH_3','^*COH','^*CH_2CH_3','H_2^*COH','^*CHCH_3',
           'H^*CO','H^*COH','^*COOH','CH_3^*CO','^*CHCO','^*CCH_2OH','^*CCHO','^*CCO','CH_3^*CHOH',
           'CH_3^*COH','^*CHCH_2','^*CCHCH_2','^*CHCHCH_2','^*CHCHCH_3','^*CH_2CH_2CH_3',
                      'CH_2^*CCH_3','CH_3^*CHCH_3','^*CCCH_2',
                      '^*CCH_2CH_3','CH_3CH_2^*CO','CH_3^*CHOH',
                      '^*CHCCH_2','^*CHCH_2CH_3','CH_3^*CCH_3']

binding_vdW=['CO_2^*','CH_2CO^*','CH_3CHCH_2^*','CH_3CH_2CH_3^*','HCOOH^*',
             'HCO_2CH_3^*','CH_3CH_2OH^*','CH_3CHO^*','CH_2CCH_2^*',
             'CH_3OCH_3^*','H_2CO_2H_2^*','OCO_2H_2^*','CH_3OCH_2OH^*']
bidentate=['^*C^*C','^*CH^*CH','^*CH_2^*CH_2','^*CH_2^*CH','^*CH^*C','H^*C^*O',
           'H_2^*C^*O','^*CH_2^*CH^*CH_2','H_2C^*O^*O','OC^*O^*O','^*C^*CCH_2',
           'CH_3^*CH^*CH_2']


CBH1_matrix=pd.read_csv('../data/QE_CBH1_matrix', sep="\t", header=0, index_col=0)
CBH1_matrix=CBH1_matrix.fillna(0)

def get_error(a):
    error=[]
    hrxn=[]
    for i in range(len(CBH1_matrix.index)):
        if CBH1_matrix[a][i] !=0:
            spcs=CBH1_matrix.index[i]
            for j in range(len(results.index)):
                if CBH1_matrix.index[i] != '^*OOH':
                    if CBH1_matrix.index[i] == results.index[j]:
                        dev=results.iloc[j,1]-results.iloc[j,0]
                        error.append(dev)
                        hrxn.append(results.iloc[j,2])
                 
    MAE=np.mean(np.abs(error))   
    avg_hrxn=np.mean(np.abs(hrxn))        
                 
    return error, MAE, hrxn, avg_hrxn

ch2_error=get_error("^*CH_2")
ch_error=get_error("^*CH")
ch3_error=get_error("^*CH_3")
oh_error=get_error("^*OH")
c2h6_error=get_error("C_2H_6^*")
c2h4_error=get_error("C_2H_4^*")
ch4_error=get_error("CH_4^*")
h2o_error=get_error("H_2O^*")
h2co_error=get_error("H_2CO^*")
ch3oh_error=get_error("CH_3OH^*")

results_o=[]
for no,spcs in enumerate(binding_o):
    results_o.append(results.loc[spcs].T)

results_o=pd.DataFrame(results_o)

def get_error_binding_atom(a):
    error=[]
    hrxn=[]
    for i in range(len(results.index)):
        for j in range(len(a)):
            if results.index[i] != '^*OOH':
                if results.index[i] == a[j]:
                    dev=results.iloc[i,1]-results.iloc[i,0]
                    error.append(dev)
                    hrxn.append(results.iloc[j,2])
                    
    MAE=np.mean(np.abs(error))           
    avg_hrxn=np.mean(np.abs(hrxn))  
    
    return error, MAE, hrxn, avg_hrxn

error_o=get_error_binding_atom(binding_o)
error_c=get_error_binding_atom(binding_c)
error_c3=get_error_binding_atom(binding_c3)
error_c_all=get_error_binding_atom(binding_c_all)
error_bidentate=get_error_binding_atom(bidentate)
error_vdW=get_error_binding_atom(binding_vdW)

def get_error_all():
    error=[]
    hrxn=[]
    for i in range(len(results.index)):
            if results.index[i] != '^*OOH':
                    dev=results.iloc[i,1]-results.iloc[i,0]
                    error.append(dev)
                    hrxn.append(results.iloc[i,2])
                    
    MAE=np.mean(np.abs(error))   
    avg_hrxn=np.mean(np.abs(hrxn))        
                 
    return error, MAE, hrxn, avg_hrxn

error_all=get_error_all()

results_vdW=[]
for no,spcs in enumerate(binding_vdW):
    results_vdW.append(results.loc[spcs].T)

results_vdW=pd.DataFrame(results_vdW)

results_bidentate=[]
for no,spcs in enumerate(bidentate):
    results_bidentate.append(results.loc[spcs].T)

results_bidentate=pd.DataFrame(results_bidentate)

results_c=[]
for no,spcs in enumerate(binding_c):
    results_c.append(results.loc[spcs].T)

results_c=pd.DataFrame(results_c)

results_c3=[]
for no,spcs in enumerate(binding_c3):
    results_c3.append(results.loc[spcs].T)

results_c3=pd.DataFrame(results_c3)

colormap = plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 4)]

gs = gridspec.GridSpec(nrows=1, ncols=2)
gs.update(wspace=0.4, hspace=0.4)

ax0 = plt.subplot(gs[0, 0])
ax1 = plt.subplot(gs[0, 1])

ax0.bar(-0.125,error_o[1], width=0.25,color=colors[0], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax0.bar(1-0.125,error_c_all[1], width=0.25,color=colors[0], edgecolor='k')
ax0.bar(2-0.125,error_bidentate[1], width=0.25,color=colors[0], edgecolor='k')
ax0.bar(3-0.125,error_vdW[1], width=0.25,color=colors[0], edgecolor='k')

ax0.bar(0.25-0.125,error_o[3], width=0.25,color=colors[1], edgecolor='k', label='$\mathrm{\overline{|\Delta H_{rxn}|}}$')
ax0.bar(1.25-0.125,error_c_all[3], width=0.25,color=colors[1], edgecolor='k')
ax0.bar(2.25-0.125,error_bidentate[3], width=0.25,color=colors[1], edgecolor='k')
ax0.bar(3.25-0.125,error_vdW[3], width=0.25,color=colors[1], edgecolor='k')

ax0.set_xlim([-0.5,3.5])
ax0.set_ylim([0,80])
ax0.set_ylabel('$\mathrm{enthalpy\ (kJ\,mol^{-1})}$') 
ax0.set_xticks([0,1,2,3])
ax0.set_xticklabels(['$\mathrm{^*O\u2010 X}$','$\mathrm{^*C\u2010 X}$','$\mathrm{bidentate}$', '$\mathrm{vdW}$'])
ax0.legend()

ax1.bar(0-0.125,ch_error[1], width=0.25,color=colors[0], edgecolor='k', label='$\mathrm{\overline{|\Delta\Delta_fH|}}$')
ax1.bar(1-0.125,ch2_error[1], width=0.25,color=colors[0], edgecolor='k')
ax1.bar(2-0.125,ch3_error[1], width=0.25,color=colors[0], edgecolor='k')
ax1.bar(3-0.125,ch4_error[1], width=0.25,color=colors[0], edgecolor='k')
ax1.bar(4-0.125,c2h4_error[1], width=0.25,color=colors[0], edgecolor='k')
ax1.bar(5-0.125,c2h6_error[1], width=0.25,color=colors[0], edgecolor='k')
ax1.bar(6-0.125,h2co_error[1], width=0.25,color=colors[0], edgecolor='k')
ax1.bar(7-0.125,ch3oh_error[1], width=0.25,color=colors[0], edgecolor='k')
ax1.bar(8-0.125,h2o_error[1], width=0.25,color=colors[0], edgecolor='k')
ax1.bar(9-0.125,oh_error[1], width=0.25,color=colors[0], edgecolor='k')

ax1.bar(0.25-0.125,ch_error[3], width=0.25,color=colors[1], edgecolor='k', label='$\mathrm{\overline{|\Delta H_{rxn}|}}$')
ax1.bar(1.25-0.125,ch2_error[3], width=0.25,color=colors[1], edgecolor='k')
ax1.bar(2.25-0.125,ch3_error[3], width=0.25,color=colors[1], edgecolor='k')
ax1.bar(3.25-0.125,ch4_error[3], width=0.25,color=colors[1], edgecolor='k')
ax1.bar(4.25-0.125,c2h4_error[3], width=0.25,color=colors[1], edgecolor='k')
ax1.bar(5.25-0.125,c2h6_error[3], width=0.25,color=colors[1], edgecolor='k')
ax1.bar(6.25-0.125,h2co_error[3], width=0.25,color=colors[1], edgecolor='k')
ax1.bar(7.25-0.125,ch3oh_error[3], width=0.25,color=colors[1], edgecolor='k')
ax1.bar(8.25-0.125,h2o_error[3], width=0.25,color=colors[1], edgecolor='k')
ax1.bar(9.25-0.125,oh_error[3], width=0.25,color=colors[1], edgecolor='k')

ax1.set_xlim([-0.5,9.5])
ax1.set_ylim([0,175])
ax1.set_ylabel('$\mathrm{enthalpy\ (kJ\,mol^{-1})}$') 
ax1.set_xticks([0,1,2,3,4,5,6,7,8,9])
ax1.set_xticklabels(['$\mathrm{^*CH}$','$\mathrm{^*CH_2}$','$\mathrm{^*CH_3}$', '$\mathrm{CH_4^*}$', '$\mathrm{C_2H_4^*}$', '$\mathrm{C_2H_6^*}$',
                     '$\mathrm{H_2CO^*}$', '$\mathrm{CH_3OH^*}$', '$\mathrm{H_2O^*}$', '$\mathrm{^*OH}$'], rotation=70)

ax1.legend()

import string 
ax0.text(-0.25, 1.05, string.ascii_lowercase[0], transform=ax0.transAxes, size=20, weight='bold')
ax1.text(-0.25, 1.05, string.ascii_lowercase[1], transform=ax1.transAxes, size=20, weight='bold')
plt.savefig('Summary_CBH.pdf', bbox_inches='tight',transparent=False)