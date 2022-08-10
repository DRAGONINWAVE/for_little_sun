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
    julian_date = (np.ceil(data['time.dayofyear']-data['time.day'])).astype(int)
    # print(julian_date)
    SIGMA = 0.4093 * np.sin(2*np.pi*julian_date/365 - 1.405)
    print(SIGMA)

if __name__ == '__main__':
    main()