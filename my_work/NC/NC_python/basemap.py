import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap
# plt.figure(1)


map=Basemap(llcrnrlon=79,llcrnrlat=26,urcrnrlon=90,urcrnrlat=31)
CHN = r'F:\Nepal_ET0'
map.readshapefile(CHN+'\\NEPAL_BOUNDARIES\\npl_admbnda_adm0_nd_20201117',
'country',drawbounds=True)
map.readshapefile(CHN+'\\NEPAL_BOUNDARIES\\npl_admbnda_adm1_nd_20201117',
'states',drawbounds=True)
plt.show()
# import Fiona
#
# shape = Fiona.open(r"F:\Nepal_ET0\NEPAL_BOUNDARIES\npl_admbnda_adm0_nd_20201117.shp")
# print (shape.schema)
# # {'geometry': 'LineString', 'properties': OrderedDict([(u'FID', 'float:11')])}
# #first feature of the shapefile
# first = shape.next()
# print (first) # (GeoJSON format)
# # {'geometry': {'type': 'LineString', 'coordinates': [(0.0, 0.0), (25.0, 10.0), (50.0, 50.0)]}, 'type': 'Feature', 'id': '0', 'properties': OrderedDict([(u'FID', 0.0)])}