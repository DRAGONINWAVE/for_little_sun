import xarray as xr
import pandas as pd
import numpy as np
import asyncio
from tqdm import tqdm
import netCDF4 as nc

path = r'F:\Nepal_ET0\Tmax'
#读取nc文件
filename = r'\200101.nc'
data = nc.Dataset(path+filename,'r')
# #查看所有变量
# print(data.variables.keys())
# #查看所有变量的详细情况
# print(data.variables.items())
var = 't2m'
var_info = data.variables[var]
var_data = data[var]
print(var_info)
print(var_data.shape)
print(type(var_data))
var_data = np.array(var_data)
print(type(var_data))

