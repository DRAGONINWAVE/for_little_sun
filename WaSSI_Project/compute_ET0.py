import numpy as np
import pandas as pd
import xarray as xr
import datetime

def main():
    data = xr.open_dataset(r'D:\TD\my_work\NC\NC_python\M2000_2020mean_mean.nc')
    # data = data.resample(time='1MS')
    TEMP = data['t2m'] - 273.3
    e = 6.108*np.exp(17.2693882*TEMP/(TEMP+237.3))
    rou_W = 216.7*e/(TEMP + 273.3)
    data['time.day'] = (data['time.day']/2)
    print((np.ceil(data['time.dayofyear']-data['time.day'])).astype(int))

if __name__ == '__main__':
    main()