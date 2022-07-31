import numpy as np
import xarray as xr
import pandas as pd
from tqdm import tqdm
#setting the all_used path
global path
path = r'F:\ERA5\ERA5\\'
global path2
path2 = 'temperature\mean\\'
#create the filenames will be used

def FILENAMES(start, end):
    filenames = []
    for year in tqdm(range(start,end + 1),desc='creating the filenames'):
        # years.set_description('creating the filenames')
        for month in range(1,13):
            month = str(month).zfill(2)
            filenames.append(str(year)+month+'.nc')
    return filenames

#合并所有的nc文件,并求出各年每月平均
def MEAN_TEMP(read_path,filenames,value,name):
    f1 = xr.Dataset()
    for filename in tqdm(filenames,desc='computing mean temperature'):
        f  = xr.open_dataset(path + read_path + filename)
        f1 = xr.merge([f,f1])
    f2 = f1[value]
    f2 = f2.resample(time='1m').mean()
    f2.to_netcdf(name)
    return f2

def main():
    filenames = FILENAMES(start=2000,end=2020)
    TEMP  = MEAN_TEMP(path2,filenames,'t2m',name='M2000_2020mean_mean.nc')
    print(TEMP)

if __name__ == '__main__':
    main()
