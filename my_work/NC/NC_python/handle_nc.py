from netCDF4 import Dataset
import numpy as np
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pandas import DataFrame
import datetime
#用Basemap画地图
def graph(lon,lat,target,levelT,colorT,title):
    b_map=Basemap(resolution='l', area_thresh=10000, projection='cyl',
                  llcrnrlon=min(lon), urcrnrlon=max(lon), llcrnrlat=min(lat),urcrnrlat=max(lat))
    #llcrnrlon=0, urcrnrlon=360, llcrnrlat=-90,urcrnrlat=90
    print(type(target))
    fig=plt.figure(figsize=(9, 6))  #plt.figure(figsize=(12, 8))
    ax=fig.add_axes([0.1,0.1,0.8,0.8])
    lon,lat=np.meshgrid(lon,lat)
    x,y=b_map(lon,lat)
    print(x.shape,y.shape,target.shape)
    cs=b_map.contourf(x,y,target,levels=levelT,colors=colorT) #target[0,:,:]
    b_map.colorbar(cs)
    b_map.drawcoastlines(linewidth=1)
    b_map.drawcountries(linewidth=1.5)

    plt.title(title,size=20)

    #plt.savefig('Rainf_0.png',dpi=300)
    plt.show()
    plt.close()

nc=Dataset('F:\\Nepal_ET0\\Tmin\\200101.nc')
print(nc.variables.keys())

for var in nc.variables.keys():
    data=nc.variables[var][:].data
    print(var,data.shape)

# time variable查看，时间戳变换
# 看出是逐时数据

time = nc.variables['time'][:].data
print(time)
# for i in range(3):
#     tstamp = (time[i] - 613608) * 3600  # 1900年1月1日零时距离1970年1月1日零时有613608个小时
#     date = datetime.datetime.utcfromtimestamp(tstamp)
#     print(date.strftime("%Y-%m-%d %H:%M:%S"))
print(nc.variables.keys())

data=nc.variables['t2m'][:]
print(data.shape)

long= nc.variables['lon'][:]
lati= nc.variables['lat'][:]
print(long[0],long[-1],lati[0],lati[-1])
print(long.shape,lati.shape,data.shape)

plt.contourf(long,lati,data[30,:,:]-273) #转为摄氏度
plt.colorbar()


plt.show()