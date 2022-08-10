import numpy as np
import pandas as pd
import xarray as xr
import datetime
from tqdm import tqdm

def main():
    ##读取nc文件
    data = xr.open_dataset(r'D:\TD\my_work\NC\NC_python\M2000_2020mean_mean.nc')
    # data = data.resample(time='1MS')
    ## 计算平均摄氏度：TEMP；饱和蒸汽压：e；饱和蒸汽压密度：rou_W
    TEMP = data['t2m'] - 273.3
    e = 6.108*np.exp(17.2693882*TEMP/(TEMP+237.3))
    rou_W = 216.7*e/(TEMP + 273.3)

    ##单独提取time元素
    date = data['time']

    ## 合并里面的日序 dayofmonth
    data['time.day'] = (data['time.day']/2)
    # print(data)

    ## 计算日序（一种是从公元前开始：julian_date_all;一种是从每年的一月一号开始：julian_date_year）

    # 从公元前开始：julian_date_all
    df = pd.DataFrame({'dates': date})
    df['dates'] = pd.to_datetime(df['dates'])
    df['jul1'] = pd.DatetimeIndex(df['dates']).to_julian_date()
    df['jul2'] = pd.DatetimeIndex(df['dates']).floor('d').to_julian_date()
    data['jul2'] = df['jul2']
    julian_date_all = (np.ceil(np.array(data['jul2']) - data['time.day'])).astype(int)
    data['jul2'] = julian_date_all
    # print(data['jul2'])

    # 从一月一号开始：julian_date_year
    julian_date_year = (np.ceil(data['time.dayofyear']-data['time.day'])).astype(int)
    data['julian_date_year'] = julian_date_year
    # print(julian_date_year)

    # print(data)
    ## 计算月中julian_date的太阳偏角:SIGMA
    SIGMA_all  = 0.4093 * np.sin(2*np.pi*np.array(data['jul2'])/365 - 1.405)
    SIGMA_year = 0.4093 * np.sin(2*np.pi*np.array(julian_date_year)/365 - 1.405)
    # print(SIGMA_all,SIGMA_year)

    ## 计算日落时角：OUMIG
    # OUMIGA = np.reshape(newshape=[50,252])
    OUMIGA = np.outer(-1*np.array(np.tan((data['lat']) * 2 * np.pi /360)),np.array(np.tan(julian_date_year)))
    # OUMIGA = np.arccos(-1*np.array(np.tan((data['lat']) * 2 * np.pi /360)) @ np.array(np.tan(data['julian_date_year'])).T)
    print(np.arccos(OUMIGA))
    # K = 2 * OUMIGA / np.pi
    # print(K)

if __name__ == '__main__':
    main()