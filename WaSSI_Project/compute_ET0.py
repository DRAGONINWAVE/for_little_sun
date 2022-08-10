import numpy as np
import pandas as pd
import xarray as xr
import datetime

data = xr.open_dataset(r'D:\TD\my_work\NC\NC_python\M2000_2020mean_mean.nc')
TEMP = data['t2m'] - 273.3
# data = data.isel(time=(data.time.dt.month.isin([1, 2, 3])))
# print(xr.cftime_range(start="2000", periods=6, freq="1MS", calendar="julian"))
# print(d)
# dt = datetime.datetime.strptime(d,fmt)
# print(dt)
e = 6.108*np.exp(17.2693882*TEMP/(TEMP+237.3))
rou_W = 216.7*e/(TEMP + 273.3)
date = data['time']
ts = pd.Timestamp(year = 2000,  month = 11, day = 21,
                  hour = 10, second = 49, tz = 'US/Central')
print(ts)
print(date.to_julian_date())