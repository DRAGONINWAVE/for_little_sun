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
#计算每月的平均温度
def MEAN_TEMP(path2,filenames):
    f1 = xr.Dataset()
    for filename in tqdm(filenames,desc='computing mean temperature'):
        f = xr.open_dataset(path + path2 + filename)
        f1 = xr.concat([f],dim=['time'])
    return f1
# def test_MEAN_TEMP(path2,filenames):
def CONCAT_ARRAYS(filenames):
    xadv_new = []
    for i in tqdm(range(len(filenames)),desc='concating arrays'):
        f0 = xr.open_dataset(path + path2 + filenames[i])
        xadv_new.append(f0)
    f1 = xr.concat(xadv_new,dim=['time'])
    return f1
def main():
    filenames = FILENAMES(2000,2020)
    TEMP = MEAN_TEMP('temperature\mean\\',filenames)
    concat_files = CONCAT_ARRAYS(filenames)
    print(concat_files)
if __name__ == '__main__':
    main()




