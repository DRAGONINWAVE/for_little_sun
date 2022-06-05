from netCDF4 import Dataset
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap


nc=Dataset('F:\\Nepal_ET0\\Tmin\\200101.nc')
nc1 = Dataset('F:\\Nepal_ET0\\Tmin\\200102.nc')
# print(nc.variables.keys())
# print(nc.realization)
for var in nc.variables.keys():
    data=nc.variables[var][:].data
    print(var,data.shape)
time = nc.variables['time'][:].data

data=nc.variables['t2m'][:]
print(data.shape)

long= nc.variables['lon'][:]
lati= nc.variables['lat'][:]
print(long[0],long[-1],lati[0],lati[-1])
print(long.shape,lati.shape,data.shape)

plt.contourf(long,lati,data[30,:,:]-273) #转为摄氏度
plt.colorbar()

print(lati,
      long)
print()

plt.figure(1)
map=Basemap(llcrnrlon=79.1,llcrnrlat=26,urcrnrlon=89.,urcrnrlat=30.9)
CHN = r'F:\Nepal_ET0'
map.readshapefile(CHN+'\\NEPAL_BOUNDARIES\\npl_admbnda_adm0_nd_20201117',
'country',drawbounds=True)
map.readshapefile(CHN+'\\NEPAL_BOUNDARIES\\npl_admbnda_adm1_nd_20201117',
'states',drawbounds=True)
plt.show()