from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
map = Basemap(
    llcrnrlon = 79.1, llcrnrlat = 26., urcrnrlon = 89., urcrnrlat = 31, resolution = 'h', epsg = 3415
)
map.drawmapboundary(fill_color = 'aqua')
map.fillcontinents(color = 'coral', lake_color = 'aqua')
map.drawcountries(linewidth=2)
map.drawcoastlines()
plt.show()

# import matplotlib.pyplot as plt
#
# from mpl_toolkits.basemap import Basemap
#
# plt.figure(figsize=(16,8))
#
# m = Basemap(llcrnrlon=77, llcrnrlat=14, urcrnrlon=140, urcrnrlat=51, projection='lcc', lat_1=33, lat_2=45, lon_0=100)
# m.drawcoastlines()
# # m.readshapefile('CHN_adm_shp/CHN_adm1', 'states', drawbounds=True)
# m.drawcountries(linewidth=2)
#
#
# plt.show()