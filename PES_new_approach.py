import matplotlib.pyplot as plt
from energydiagram import ED


diagram = ED()

diagram.add_level(0,bottom_text='$\mathrm{CH_3CH_2CH_3}$',)
diagram.add_level(-48.6,bottom_text='$\mathrm{CH_3CH_2CH_3^*}$')
diagram.add_level(-38.5,position='l',top_text='$\mathrm{2CH_3CH_3*-CH_4*}$')
#diagram.add_level(7,position='l')
diagram.add_level(-27.1,bottom_text='$\mathrm{^*CH_2CH_2CH_3}$')
diagram.add_level(-11.6,position='l',top_text='$\mathrm{2CH_3CH_3*+*CH_3-2CH_4*}$')
#diagram.add_level(242.46,position='l')
diagram.add_level(-43.4,bottom_text='$\mathrm{CH_3^*CH^*CH_2}$')
diagram.add_level(-14.9,position='l',top_text='$\mathrm{2CH_3CH_3^* + 2^CH3-3CH_4^*}$')
#diagram.add_level(114.22,position='l')
diagram.add_level(125.02,bottom_text='$\mathrm{CH_3CHCH_2}$')
#diagram.space= 20

#diagram.add_link(0,1)
#diagram.add_link(1,4)
#diagram.add_link(4,7)
#diagram.add_link(7,10)


#diagram.add_link(0,2)
#diagram.add_link(2,5)
#diagram.add_link(5,8)
#diagram.add_link(8,10)

diagram.plot(show_IDs=False,ylabel='$\mathrm{Energy\, /\, kJ mol^{-1}}$')