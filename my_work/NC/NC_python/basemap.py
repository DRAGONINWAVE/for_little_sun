import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap
plt.figure(1)

# map=Basemap()
map=Basemap(llcrnrlon=79,llcrnrlat=26,urcrnrlon=90,urcrnrlat=31)
# map.drawcoastlines()
# map.drawcountries()
# map.drawrivers(color='black',linewidth=0.3)
CHN = r'F:\Nepal_ET0'
map.readshapefile(CHN+'\\NEPAL_BOUNDARIES\\npl_admbnda_adm0_nd_20201117',
'country',drawbounds=True)
map.readshapefile(CHN+'\\NEPAL_BOUNDARIES\\npl_admbnda_adm1_nd_20201117',
'states',drawbounds=True)
# map.readshapefile(CHN+'\gadm36_TWN_shp\gadm36_TWN_1',
# 'taiwan',drawbounds=True)
# parallels = np.linspace(3,55,5)
# map.drawparallels(parallels,labels=[True,False,False,False])
# meridians = np.linspace(70,140,5)
# map.drawmeridians(meridians,labels=[False,False,False,True])
# plt.title(r'$World\ Map$',fontsize=24)
# map=Basemap(llcrnrlon=70,llcrnrlat=3,urcrnrlon=137,urcrnrlat=54,
# projection = 'lcc', lat_1 = 33, lat_2 = 45, lon_0 = 100)
plt.show()