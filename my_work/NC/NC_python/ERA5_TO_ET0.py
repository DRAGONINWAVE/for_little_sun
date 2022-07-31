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

#合并所有的nc文件
def MEAN_TEMP(path2,filenames):
    f1 = xr.Dataset()
    for filename in tqdm(filenames,desc='computing mean temperature'):
        f  = xr.open_dataset(path + path2 + filename)
        f1 = xr.merge([f,f1])
    return f1

def main():
    # global filenames
    filenames = FILENAMES(2000,2020)
    TEMP  = MEAN_TEMP(path2,filenames)
    TEMPA = TEMP['t2m']
    TEMPA = TEMPA.resample(time='1m').mean()
    TEMPA.to_netcdf('2000-2020mean.nc')
    print(xr.open_dataset('2000-2020mean.nc'))

    # print(concat_files)

if __name__ == '__main__':
    main()
