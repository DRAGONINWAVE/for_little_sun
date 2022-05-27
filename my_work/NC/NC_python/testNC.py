# from netCDF4 import Dataset
# import numpy as np
# import sys
# import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap
# from pandas import DataFrame
#
#
# nc=Dataset('F:\\t2m_al.nc')
#
# for var in nc.variables.keys():
#     data=nc.variables[var][:].data
#     print(var,data.shape)
#
#
# long= nc.variables['lon'][:]
# lati= nc.variables['lat'][:]
# data=nc.variables['t2m'][:]
# for i in range(15,18):
#     plt.contourf(long,lati,data[i,:,:]-273) #转为摄氏度
#     plt.colorbar()
#     plt.show()

import os
path = 'F:\\Nepal_ET0'
print(list(os.walk(path))[3][2],list(os.walk(path))[2][1])