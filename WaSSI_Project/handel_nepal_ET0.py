import xarray as xr
import pandas as pd
import numpy as np
import asyncio
from tqdm import tqdm
import netCDF4 as nc

path = r'F:\ERA5\ERA5\temperature\mean'
#读取nc文件
filename = r'\200101.nc'
data = nc.Dataset(path+filename,'r')
# #查看所有变量
# print(data.variables.keys())
# #查看所有变量的详细情况
# print(data.variables.items())
# var = 't2m'
# var_info = data.variables[var]
# var_data = data[var]
# print(var_info)
# print(var_data.shape)
# print(type(var_data))
# var_data = np.array(var_data)
# print(type(var_data))
# group_name = data.groups.keys()
# print(group_name)
# print(data[t2m].values)

# #create NC file
# f_w = nc.Dataset('b.nc','a',format = 'NETCDF4')   #创建一个格式为.nc的，名字为 ‘hecheng.nc’的文件
# #time纬度为12。注意，第2个参数 表示维度，但是必须是 integer整型，也就是只能创建一个基础单一维度信息。
# #如果后面要创建一个变量维度>1，则必须由前面的单一维度组合而来。后面会介绍。
#
# #确定基础变量的维度信息。相对与坐标系的各个轴(x,y,z)
# f_w.createDimension('time',12)
# f_w.createDimension('level',37)
# f_w.createDimension('lat',161)
# f_w.createDimension('lon',177)
#
# ##创建变量。参数依次为：‘变量名称’，‘数据类型’，‘基础维度信息’
# f_w.createVariable('time',int,('time'))
# f_w.createVariable('level',int,('level'))
# f_w.createVariable('lat',np.float32,('lat'))
# f_w.createVariable('lon',np.float32,('lon'))
#
# #写入变量time的数据。维度必须与定义的一致。
# time = np.array([0,6,12,18,0,6,12,18,0,6,12,18])
# f_w.variables['time'][:] = time
#
# #新创建一个多维度变量，并写入数据，
# f_w.createVariable( 'u', np.float32, ('time','level','lat','lon'))
# var_data = np.ones(shape=(12,37,161,177), dtype = np.float32)
#
# f_w = nc.Dataset('haha4.nc','w',format = 'NETCDF4')
#
# f_w.createDimension('time',12)
# f_w.createDimension('level',37)
# f_w.createDimension('lat',161)
# f_w.createDimension('lon',177)
#
# f_w.createVariable('time',np.int,('time'))
# f_w.createVariable('level',np.int,('level'))
# f_w.createVariable('lat',np.float32,('lat'))
# f_w.createVariable('lon',np.float32,('lon'))
#
# time = np.array([0,6,12,18,0,6,12,18,0,6,12,18])
#
# f_w.variables['time'][:] = time
# f_w.variables['level'][:] = level
#
# f_w.createVariable( 'q', np.float32, ('time','level','lat','lon'))
# var_data = np.ones(shape=(12,37,161,177), dtype = np.float32)
# f_w.variables['q'][:] = var_data
#
# #创建一个群组，名字为'wind'
# group1 = f_w.createGroup('wind')
#
# group1.createVariable( 'u', np.float32, ('time','level','lat','lon'))
# var_data = np.ones(shape=(12,37,161,177), dtype = np.float32)
# group1.variables['u'][:] = var_data
#
# group1.createVariable( 'v', np.float32, ('time','level','lat','lon'))
# var_data = np.zeros(shape=(12,37,161,177), dtype = np.float32)
# group1.variables['v'][:] = var_data
#
# group1.close  # 关闭群组， 注意，这里没有括号
#
# f_w.close()

