import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

plt.rcParams['figure.figsize'] = (18, 6)
plt.rcParams['axes.linewidth'] = 2
plt.rc('xtick', labelsize=16)
plt.rc('ytick', labelsize=16)
plt.rc('axes', labelsize=16)
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

colormap = plt.cm.Dark2
colors = [colormap(i) for i in np.linspace(0, 1, 4)]


gs = gridspec.GridSpec(nrows=1, ncols=2)
gs.update(wspace=0.25, hspace=0.4)

ax0 = plt.subplot(gs[0, 0])
ax1 = plt.subplot(gs[0, 1])

ax0.set_ylim([-100,200])
ax0.set_xlim([-1,20])
ax0.get_xaxis().set_visible(False)
ax0.spines['right'].set_visible(False)
ax0.spines['top'].set_visible(False)
ax0.spines['bottom'].set_visible(False)
ax0.set_ylabel('$\mathrm{enthalpy\ (kJ\,mol^{-1})}$')

va_offset=4
Hf_H=-23.4
Hf_ref=-82.7
#############old approach#####################
#CH3CH2CH3
Hf_CH3CH2CH3=-82.7-Hf_ref
ax0.plot((0,3),(Hf_CH3CH2CH3,Hf_CH3CH2CH3),linestyle='solid',color='b')
ax0.text(1.3,Hf_CH3CH2CH3-va_offset,'$\mathrm{CH_3CH_2CH_{3(g)}}$',va='top',ha='center',size=12)

#CH3CH2CH3_ads
Hf_CH3CH2CH3_ads=-121.27-Hf_ref
ax0.plot((4,7),(Hf_CH3CH2CH3_ads,Hf_CH3CH2CH3_ads),linestyle='solid',color='k')
ax0.text(5.5,Hf_CH3CH2CH3_ads-va_offset,'$\mathrm{CH_3CH_2CH_3^*}$',va='top',ha='center',size=12)


#reference CH3CH2CH3*
Hf_CH3CH2CH3_precursor=23.16+Hf_CH3CH2CH3_ads
ax0.plot((4,7),(Hf_CH3CH2CH3_precursor,Hf_CH3CH2CH3_precursor),linestyle='solid',color='r')
ax0.text(5.5,Hf_CH3CH2CH3_precursor+va_offset,'$\mathrm{CH_3CH_2CH_{3(g)}}$',va='bottom',ha='center',size=11,color='r')

ax0.arrow(6.5,Hf_CH3CH2CH3_ads+va_offset,0,Hf_CH3CH2CH3_precursor-Hf_CH3CH2CH3_ads-2*va_offset,
          length_includes_head=True, head_length=3, head_width=0.25, color='r')

ax0.arrow(6.5,Hf_CH3CH2CH3_precursor-va_offset,0,Hf_CH3CH2CH3_ads-Hf_CH3CH2CH3_precursor+2*va_offset,
          length_includes_head=True, head_length=3, head_width=0.25, color='r')

ax0.text(6.3,(Hf_CH3CH2CH3_precursor-Hf_CH3CH2CH3_ads)/2+Hf_CH3CH2CH3_ads,'$\mathrm{\Delta H_{ads}}$',va='center',ha='right',size=11,color='r')


#*CH2CH2CH3
Hf_CH2CH2CH3_ads=-87.66+Hf_H-Hf_ref
ax0.plot((8,11),(Hf_CH2CH2CH3_ads,Hf_CH2CH2CH3_ads),linestyle='solid',color='k')
ax0.text(9.3,Hf_CH2CH2CH3_ads-va_offset-5,'$\mathrm{^*CH_2CH_2CH_3}$\n$\mathrm{+\,^*H}$',va='top',ha='center',size=12)

#reference *CH2CH2CH3(g)
Hf_CH2CH2CH3_precursor=225.12+Hf_CH2CH2CH3_ads
ax0.plot((8,11),(Hf_CH2CH2CH3_precursor,Hf_CH2CH2CH3_precursor),linestyle='solid',color='r')
ax0.text(9.5,Hf_CH2CH2CH3_precursor+va_offset,'$\mathrm{\u2022 CH_2CH_2CH_{3(g)}}$',va='bottom',ha='center',size=11,color='r')

ax0.arrow(9.8,Hf_CH2CH2CH3_ads+va_offset,0,Hf_CH2CH2CH3_precursor-Hf_CH2CH2CH3_ads-2*va_offset,
          length_includes_head=True, head_length=10, head_width=0.5, color='r')

ax0.arrow(9.8,Hf_CH2CH2CH3_precursor-va_offset,0,Hf_CH2CH2CH3_ads-Hf_CH2CH2CH3_precursor+2*va_offset,
          length_includes_head=True, head_length=10, head_width=0.5, color='r')

ax0.text(9.6,(Hf_CH2CH2CH3_precursor-Hf_CH2CH2CH3_ads)/2+Hf_CH2CH2CH3_ads,'$\mathrm{\Delta H_{ads}}$',va='center',ha='right',size=11,color='r')

#*CH2CH*CH3
Hf_CH2CHCH3_ads=-91.71+2*Hf_H-Hf_ref
ax0.plot((12,15),(Hf_CH2CHCH3_ads,Hf_CH2CHCH3_ads),linestyle='solid',color='k')
ax0.text(13.5,Hf_CH2CHCH3_ads-va_offset,'$\mathrm{^*CH_2^*CHCH_3}$\n$\mathrm{+\,2\,^*H}$',va='top',ha='center',size=12)

#refernce *CH2CH*CH3(g)
Hf_CH2CHCH3_precursor=100.92+Hf_CH2CHCH3_ads
ax0.plot((12,15),(Hf_CH2CHCH3_precursor,Hf_CH2CHCH3_precursor),linestyle='solid',color='r')
ax0.text(13.5,Hf_CH2CHCH3_precursor+va_offset,'$\mathrm{CH_2CHCH_{3(g)}}$',va='bottom',ha='center',size=11,color='r')

ax0.arrow(14,Hf_CH2CHCH3_ads+va_offset,0,Hf_CH2CHCH3_precursor-Hf_CH2CHCH3_ads-2*va_offset,
          length_includes_head=True, head_length=10, head_width=0.5, color='r')

ax0.arrow(14,Hf_CH2CHCH3_precursor-va_offset,0,Hf_CH2CHCH3_ads-Hf_CH2CHCH3_precursor+2*va_offset,
          length_includes_head=True, head_length=10, head_width=0.5, color='r')

ax0.text(13.8,(Hf_CH2CHCH3_precursor-Hf_CH2CHCH3_ads)/2+Hf_CH2CHCH3_ads,'$\mathrm{\Delta H_{ads}}$',va='center',ha='right',size=11,color='r')

#CH2CHCH3
Hf_CH2CHCH3=34.85-Hf_ref
ax0.plot((16,19),(Hf_CH2CHCH3,Hf_CH2CHCH3),linestyle='solid',color='b')
ax0.text(16,Hf_CH2CHCH3-va_offset,'$\mathrm{CH_2CHCH_{3(g)}}$\n$\mathrm{+\,H_{2(g)}}$',va='top',ha='left',size=12)

#connecting lines
ax0.plot((3,4),(Hf_CH3CH2CH3,Hf_CH3CH2CH3_ads),linestyle='dashed',color='k', linewidth=1)
ax0.plot((7,8),(Hf_CH3CH2CH3_ads,Hf_CH2CH2CH3_ads),linestyle='dashed',color='k', linewidth=1)
ax0.plot((11,12),(Hf_CH2CH2CH3_ads,Hf_CH2CHCH3_ads),linestyle='dashed',color='k', linewidth=1)
ax0.plot((15,16),(Hf_CH2CHCH3_ads,Hf_CH2CHCH3),linestyle='dashed',color='k', linewidth=1)


#############new approach#####################

ax1.set_ylim([-100,200])
ax1.set_xlim([-1,20])
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['bottom'].set_visible(False)
ax1.get_xaxis().set_visible(False)
ax1.set_ylabel('$\mathrm{enthalpy\ (kJ\,mol^{-1})}$')

Hf_H=-32.7

#CH3CH2CH3
Hf_CH3CH2CH3=-82.7-Hf_ref
ax1.plot((0,3),(Hf_CH3CH2CH3,Hf_CH3CH2CH3),linestyle='solid',color='b')
ax1.text(1.3,Hf_CH3CH2CH3-va_offset,'$\mathrm{CH_3CH_2CH_{3(g)}}$',va='top',ha='center',size=12)

#CH3CH2CH3*
Hf_CH3CH2CH3_ads=-120.963385494994-Hf_ref
ax1.plot((4,7),(Hf_CH3CH2CH3_ads,Hf_CH3CH2CH3_ads),linestyle='solid',color='k')
ax1.text(5.3,Hf_CH3CH2CH3_ads-va_offset,'$\mathrm{CH_3CH_2CH_3^*}$',va='top',ha='center',size=12)

#reference CH3CH2CH3*
Hf_CH3CH2CH3_ref=10.0633854949948+Hf_CH3CH2CH3_ads
ax1.plot((4.5,6.5),(Hf_CH3CH2CH3_ref,Hf_CH3CH2CH3_ref),linestyle='solid',color='r')
ax1.text(5.5,Hf_CH3CH2CH3_ref+va_offset,'$\mathrm{2\,CH_3CH_3^*}$\n$\mathrm{-\,CH_4^*}$',va='bottom',ha='center',size=11,color='r')

ax1.arrow(6.2,Hf_CH3CH2CH3_ads+3,0,Hf_CH3CH2CH3_ref-Hf_CH3CH2CH3_ads-6,
          length_includes_head=True, head_length=1, head_width=0.2, color='r')

ax1.arrow(6.2,Hf_CH3CH2CH3_ref-3,0,Hf_CH3CH2CH3_ads-Hf_CH3CH2CH3_ref+6,
          length_includes_head=True, head_length=1, head_width=0.2, color='r')

#ax1.text(5.9,(Hf_CH3CH2CH3_ref-Hf_CH3CH2CH3_ads)/2+Hf_CH3CH2CH3_ads-1,'$\mathrm{\Delta H_{rxn}}$',va='center',ha='right',size=11,color='r')


#*CH2CH2CH3
Hf_CH2CH2CH3_ads=-92.53+Hf_H-Hf_ref
ax1.plot((8,11),(Hf_CH2CH2CH3_ads,Hf_CH2CH2CH3_ads),linestyle='solid',color='k')
ax1.text(9.2,Hf_CH2CH2CH3_ads-va_offset,'$\mathrm{^*CH_2CH_2CH_3}$\n$\mathrm{+\,^*H}$',va='top',ha='center',size=12)

#reference *CH2CH2CH3
Hf_CH2CH2CH3_ref=15.5340850021116+Hf_CH2CH2CH3_ads
ax1.plot((8.5,10.5),(Hf_CH2CH2CH3_ref,Hf_CH2CH2CH3_ref),linestyle='solid',color='r')
ax1.text(9.5,Hf_CH2CH2CH3_ref+va_offset,'$\mathrm{2\,CH_3CH_3^*}$\n$\mathrm{+\,^*CH_3}$\n$\mathrm{-\,2\,CH_4^*}$',va='bottom',ha='center',size=11,color='r')

ax1.arrow(10.2,Hf_CH2CH2CH3_ads+3,0,Hf_CH2CH2CH3_ref-Hf_CH2CH2CH3_ads-6,
          length_includes_head=True, head_length=3, head_width=0.3, color='r')

ax1.arrow(10.2,Hf_CH2CH2CH3_ref-3,0,Hf_CH2CH2CH3_ads-Hf_CH2CH2CH3_ref+6,
          length_includes_head=True, head_length=3, head_width=0.3, color='r')

ax1.text(10,(Hf_CH2CH2CH3_ref-Hf_CH2CH2CH3_ads)/2+Hf_CH2CH2CH3_ads-1,'$\mathrm{\Delta H_{rxn}}$',va='center',ha='right',size=11,color='r')

#*CH2CH*CH3
Hf_CH2CHCH3_ads=-101.8+2*Hf_H-Hf_ref
ax1.plot((12,15),(Hf_CH2CHCH3_ads,Hf_CH2CHCH3_ads),linestyle='solid',color='k')
ax1.text(13.5,Hf_CH2CHCH3_ads-va_offset,'$\mathrm{^*CH_2^*CHCH_3}$\n$\mathrm{+\,2\,^*H}$',va='top',ha='center',size=12)

#reference *CH2CH*CH3
Hf_CH2CHCH3_ref=58.662880006335+Hf_CH2CHCH3_ads
ax1.plot((12.5,14.5),(Hf_CH2CHCH3_ref,Hf_CH2CHCH3_ref),linestyle='solid',color='r')
ax1.text(13.5,Hf_CH2CHCH3_ref+va_offset,'$\mathrm{2\,CH_3CH_3^*}$\n$\mathrm{+\,2\,^*CH_3}$\n$\mathrm{-\,3\,CH_4^*}$',va='bottom',ha='center',size=11,color='r')

ax1.arrow(14,Hf_CH2CHCH3_ads+va_offset,0,Hf_CH2CHCH3_ref-Hf_CH2CHCH3_ads-2*va_offset,
          length_includes_head=True, head_length=10, head_width=0.5, color='r')

ax1.arrow(14,Hf_CH2CHCH3_ref-va_offset,0,Hf_CH2CHCH3_ads-Hf_CH2CHCH3_ref+2*va_offset,
          length_includes_head=True, head_length=10, head_width=0.5, color='r')

ax1.text(13.8,(Hf_CH2CHCH3_ref-Hf_CH2CHCH3_ads)/2+Hf_CH2CHCH3_ads,'$\mathrm{\Delta H_{rxn}}$',va='center',ha='right',size=11,color='r')

#CH2CHCH3
Hf_CH2CHCH3=34.85-Hf_ref
ax1.plot((16,19),(Hf_CH2CHCH3,Hf_CH2CHCH3),linestyle='solid',color='b')
ax1.text(16,Hf_CH2CHCH3-va_offset,'$\mathrm{CH_2CHCH_{3(g)}}$\n$\mathrm{+\,H_{2(g)}}$',va='top',ha='left',size=12)

#connecting lines
ax1.plot((3,4),(Hf_CH3CH2CH3,Hf_CH3CH2CH3_ads),linestyle='dashed',color='k', linewidth=1)
ax1.plot((7,8),(Hf_CH3CH2CH3_ads,Hf_CH2CH2CH3_ads),linestyle='dashed',color='k', linewidth=1)
ax1.plot((11,12),(Hf_CH2CH2CH3_ads,Hf_CH2CHCH3_ads),linestyle='dashed',color='k', linewidth=1)
ax1.plot((15,16),(Hf_CH2CHCH3_ads,Hf_CH2CHCH3),linestyle='dashed',color='k', linewidth=1)

import string 
ax0.text(-0.15, 1.05, string.ascii_lowercase[0], transform=ax0.transAxes, size=20, weight='bold')
ax1.text(-0.15, 1.05, string.ascii_lowercase[1], transform=ax1.transAxes, size=20, weight='bold')

plt.savefig('pes_propane_mech.pdf',transparent=False, bbox_inches='tight')