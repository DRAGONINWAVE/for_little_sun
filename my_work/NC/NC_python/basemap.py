import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap
plt.figure(1)


map=Basemap(llcrnrlon=79,llcrnrlat=26,urcrnrlon=90,urcrnrlat=31)
CHN = r'F:\Nepal_ET0'
map.readshapefile(CHN+'\\NEPAL_BOUNDARIES\\npl_admbnda_adm0_nd_20201117',
'country',drawbounds=True)
map.readshapefile(CHN+'\\NEPAL_BOUNDARIES\\npl_admbnda_adm1_nd_20201117',
'states',drawbounds=True)
plt.show()