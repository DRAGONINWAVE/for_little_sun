import xarray as xr
import numpy as np
import pandas as pd
import netCDF4 as nc
from tqdm import tqdm
import time
start_time = time.perf_counter()
path = r'F:\Nepal_ET0\Tdmin\min'  #输入文件存储路径
#按照nc文件的格式来进行对nc文件批量命名
files = []
for i in  tqdm(range(2000,2021)):
    for j in range(1,13):
        ncname = str(i) + str(j).zfill(2) + '.nc'
        files.append(ncname)
# print(files)
data_all = []
a=[]
b=[]
# print(files)
i = 0
for file in tqdm(files):
    f = xr.open_dataset(path+'/'+file)
    # print(f.variables.keys())
    #读取变量，如果数据过大可以索引，但索引后合成的nc文件无法再索引
    lon=f['lon']
    lat=f['lat']
    time=f['time']
    t2m=f['d2m']

#concat函数按维度合并
    for t in time:
        a.append(t)
    t_al=xr.concat(a,dim='time')

    for t2m1 in t2m:
        b.append(t2m1)
    t2m_al=xr.concat(b,dim='time')
    i = i + 1
    # print(i)
# print(t_al.shape)
#写成dataarray
OLR=xr.DataArray(data=t2m_al,dims=('time','lat','lon'),
                coords=dict(time=t_al,lat=lat,lon=lon))
#dataarray转化为dataset
ds=xr.Dataset({'t2m':OLR})
elapsed_time = time.perf_counter() - start_time
print('执行时间%fs',elapsed_time)
#输出成nc文件
