from netCDF4 import Dataset
import numpy as np
import sys
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from pandas import DataFrame
import datetime
# #用Basemap画地图
# def graph(lon,lat,target,levelT,colorT,title):
#     b_map=Basemap(resolution='l', area_thresh=10000, projection='cyl',
#                   llcrnrlon=min(lon), urcrnrlon=max(lon), llcrnrlat=min(lat),urcrnrlat=max(lat))
#     #llcrnrlon=0, urcrnrlon=360, llcrnrlat=-90,urcrnrlat=90
#     print(type(target))
#     fig=plt.figure(figsize=(9, 6))  #plt.figure(figsize=(12, 8))
#     ax=fig.add_axes([0.1,0.1,0.8,0.8])
#     lon,lat=np.meshgrid(lon,lat)
#     x,y=b_map(lon,lat)
#     print(x.shape,y.shape,target.shape)
#     cs=b_map.contourf(x,y,target,levels=levelT,colors=colorT) #target[0,:,:]
#     b_map.colorbar(cs)
#     b_map.drawcoastlines(linewidth=1)
#     b_map.drawcountries(linewidth=1.5)
#
#     plt.title(title,size=20)
#
#     #plt.savefig('Rainf_0.png',dpi=300)
#     plt.show()
#     plt.close()

nc=Dataset('F:\\Nepal_ET0\\Tmin\\200101.nc')
nc1 = Dataset('F:\\Nepal_ET0\\Tmin\\200102.nc')
# print(nc.variables.keys())
# print(nc.realization)
for var in nc.variables.keys():
    data=nc.variables[var][:].data
    print(var,data.shape)

# time variable查看，时间戳变换
# 看出是逐时数据

time = nc.variables['time'][:].data
# print(time)
# for i in range(3):
#     tstamp = (time[i] - 613608) * 3600  # 1900年1月1日零时距离1970年1月1日零时有613608个小时
#     date = datetime.datetime.utcfromtimestamp(tstamp)
#     print(date.strftime("%Y-%m-%d %H:%M:%S"))
# print(nc.variables.keys())


data=nc.variables['t2m'][:]
# print(data)
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
# #生成一个Basemap类，用来变换坐标，画出合适尺寸的图
# m = Basemap(llcrnrlon=72.0,#地图左边经度
#     llcrnrlat=10.0,#地图下方纬度
#     urcrnrlon=137.0,#地图右边经度
#     urcrnrlat=55.0,#地图上方纬度
#     resolution = None,#分辨率，这里设置为无
#     projection = 'cyl')#投影方式：默认，圆柱投影
# #读取图形文件，画中国行政边界
# m.readshapefile('bou2_4l','China Map',color='k',linewidth=1.2)
import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.basemap import Basemap
plt.figure(1)


map=Basemap(llcrnrlon=79.1,llcrnrlat=26,urcrnrlon=89.,urcrnrlat=30.9)
CHN = r'F:\Nepal_ET0'
map.readshapefile(CHN+'\\NEPAL_BOUNDARIES\\npl_admbnda_adm0_nd_20201117',
'country',drawbounds=True)
map.readshapefile(CHN+'\\NEPAL_BOUNDARIES\\npl_admbnda_adm1_nd_20201117',
'states',drawbounds=True)
plt.show()
# plt.show()

# 28.909304, 80.030027
# 30.446004, 81.612058
# 26.339878, 88.017087
# 26.764536, 88.195477

# import cartopy.crs as ccrs
# import matplotlib.pyplot as plt
# from matplotlib.path import Path
# from matplotlib.patches import PathPatch
# import numpy as np
# import shapefile
# import xarray as xr
# from mpl_toolkits.basemap import Basemap
#
# #设置画图字体的大小
# plt.rcParams.update({'font.size':20})
# #解决中文乱码问题
# plt.rcParams['font.sans-serif'] = ['SimHei']
# #解决负号乱码问题
# plt.rcParams['axes.unicode_minus'] = False
# #设置画布和绘图区
# fig = plt.figure(figsize=[12,18])
# ax = fig.add_subplot(111)
#
# #读取shp格式的地图
# sf = shapefile.Reader("country1")
# #得到mask白化路径
# for shape_rec in sf.shapeRecords():
#     if shape_rec.record[2] == 'China':
#         codes = []
#         pts = shape_rec.shape.points#边界点
#         prt = list(shape_rec.shape.parts) + [len(pts)]#区块起始索引
#         for i in range(len(prt) - 1):
#             codes += [Path.MOVETO]#点移动
#             codes += [Path.LINETO] * (prt[i+1] - prt[i] -2)#画线
#             codes += [Path.CLOSEPOLY]#这块画完，循环结束，下一块
#         clip = Path(pts, codes)#利用数据和路径生成一个画图动作
#         clip = PathPatch(clip, transform=ax.transData)#再加入ax的变换
# #########################至此，所需国界图形读取完毕####################
# #这里是读取NC数据部分，上一个帖子已经介绍了，不再赘述
# ds = xr.open_dataset('EC-Interim_monthly_2018.nc')
# lat = ds.latitude
# lon = ds.longitude
# data = (ds['t2m'][0,::-1,:] - 273.15) # 把温度转换为℃   [0,::-1,:]表示第一个时次、纬度反向
# ############################至此读取温度数据结束######################
#
# #下面画
# cbar_kwargs = {
#     'orientation': 'horizontal',
#     'label': 'Temperature (℃)',
#     'shrink': 0.02,
#     'ticks': np.arange(-25, 25 + 1, 5),
#     'pad': -0.28,
#     'shrink': 0.95
# }
#
# levels = np.arange(-25, 25 + 1, 1)
# cs = data.plot.contourf(ax=ax,levels=levels,cbar_kwargs=cbar_kwargs, cmap='Spectral_r')
# #但是画出的全球温度分布
# ############################至此温度画完了######################
# #添加掩膜路径，白化外部的分部
# for contour in cs.collections:
#         contour.set_clip_path(clip)
#
# #生成一个Basemap类，用来变换坐标，画出合适尺寸的图
# m = Basemap(llcrnrlon=72.0,#地图左边经度
#     llcrnrlat=10.0,#地图下方纬度
#     urcrnrlon=137.0,#地图右边经度
#     urcrnrlat=55.0,#地图上方纬度
#     resolution = None,#分辨率，这里设置为无
#     projection = 'cyl')#投影方式：默认，圆柱投影
#
# #读取图形文件，画中国行政边界
# m.readshapefile('bou2_4l','China Map',color='k',linewidth=1.2)
# ######################至此图基本画完了，下面是一些修饰过程######################
# #画纬度
# parallels = np.arange(10,55,10)
# m.drawparallels(parallels,labels=[True,True,True,True],color='dimgrey',dashes=[1, 3])
# #画经度
# meridians = np.arange(70,135,10)
# m.drawmeridians(meridians,labels=[True,True,False,True],color='dimgrey',dashes=[1, 3])
# #移除原来的坐标轴标签
# plt.ylabel('')
# plt.xlabel('')
# #设置标题
# plt.rcParams.update({'font.size':30})
# ax.set_title(u' 中国区域2018年1月平均气温',color='blue',fontsize= 25)
# #画南海
# with open('CN-border-La.dat') as src:
#     context = src.read()
#     blocks = [cnt for cnt in context.split('>') if len(cnt) > 0]
#     borders = [np.fromstring(block, dtype=float, sep=' ') for block in blocks]
# sub_ax = fig.add_axes([0.758, 0.249, 0.14, 0.155],projection=ccrs.LambertConformal(central_latitude=90, central_longitude=115))
# for line in borders:
#     sub_ax.plot(line[0::2], line[1::2], '-', lw=1, color='k',transform=ccrs.Geodetic())
# sub_ax.set_extent([106, 127, 0, 25],crs=ccrs.PlateCarree())
# ######################修饰完毕，出图######################
# plt.savefig("China_mask_T2m.png", dpi=300, bbox_inches='tight')
# plt.show()

