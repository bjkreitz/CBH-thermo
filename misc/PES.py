

import matplotlib.pyplot as plt
from energydiagram import ED

# diagram = ED()

# diagram.add_level(0,bottom_text='$\mathrm{CH_3CH_2CH_3(g)}$',)
# diagram.add_level(-21.5,bottom_text='$\mathrm{CH_3CH_2CH_3^*}$')

# diagram.add_level(18.2,top_text='$\mathrm{^*CH_2CH_2CH_3}$')
# diagram.add_level(242.46,position='l',top_text='$\mathrm{CH_2CH_2CH_3(g)}$')
# diagram.add_level(54.2,top_text='$\mathrm{CH_3CHCH_2^*}$')
# diagram.add_level(114.22,position='l',top_text='$\mathrm{CH_3CHCH_2(g)}$')
# diagram.add_level(125.02,bottom_text='$\mathrm{CH_3CHCH_2(g)}$')
# #diagram.space= 20

# #diagram.add_link(0,1)
# #diagram.add_link(1,2)
# #diagram.add_link(2,3)
# #diagram.add_link(3,4)
# # diagram.add_link(3,4)
# # diagram.add_link(3,5)
# # diagram.add_link(0,6)

# diagram.plot(show_IDs=False,ylabel='$\mathrm{Energy\, /\, kJ mol^{-1}}$')

diagram = ED()

diagram.add_level(0,bottom_text='$\mathrm{CH_3CH_2CH_3}$',)
diagram.add_level(-21.5,bottom_text='$\mathrm{CH_3CH_2CH_3^*}$')
diagram.add_level(-118.56,position='l',top_text='$\mathrm{3CH_4,\, 2H_2}$')
diagram.add_level(7,position='l',top_text='$\mathrm{CH_3CH_2CH_3(g)}$')
diagram.add_level(18.2,bottom_text='$\mathrm{^*CH_2CH_2CH_3}$')
diagram.add_level(-118.56,position='l',top_text='$\mathrm{3CH_4,\, 2.5H_2}$')
diagram.add_level(242.46,position='l',top_text='$\mathrm{CH_2CH_2CH_3(g)}$')
diagram.add_level(-43.4,bottom_text='$\mathrm{CH_3^*CH^*CH_2}$')
diagram.add_level(-118.56,position='l',top_text='$\mathrm{3CH_4,\, 3H_2}$')
diagram.add_level(114.22,position='l',top_text='$\mathrm{CH_3CHCH_2(g)}$')
diagram.add_level(125.02,bottom_text='$\mathrm{CH_3CHCH_2}$')
diagram.dimension*= 20

#diagram.add_link(0,1)
#diagram.add_link(1,4)
#diagram.add_link(4,7)
#diagram.add_link(7,10)


#diagram.add_link(0,2)
#diagram.add_link(2,5)
#diagram.add_link(5,8)
#diagram.add_link(8,10)

diagram.plot(show_IDs=False,ylabel='$\mathrm{Energy\, /\, kJ mol^{-1}}$')