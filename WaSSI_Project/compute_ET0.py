import numpy as np
import pandas as pd
import xarray as xr

data = xr.open_dataset(r'D:\TD\my_work\NC\NC_python\M2000_2020mean_mean.nc')
TEMP = data['t2m'] - 273.3
e = 6.108*np.exp(17.2693882*TEMP/(TEMP+237.3))
# e.to_netcdf('x.nc')
# print(xr.open_dataset(r'x.nc')['t2m'].values)
rou_W = 216.7*e/(TEMP + 273.3)
print(rou_W)
