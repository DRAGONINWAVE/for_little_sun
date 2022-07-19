import xarray as xr
# from netCDF4 import Dataset
import os
from tqdm import tqdm

import netCDF4 as nc


def main():
    #读取数据

    data = nc.Dataset(r'F:\\filename_4.nc', 'w', format='NETCDF4')
    path = 'F:\\'
    name = '1981-2020_daily_nepalonly.nc'
    gname = 'elevation_p01.nc'
    # v_name = 'u10_daily.nc'
    # Tmax = 'Nepal_ET0\Tdmax\Tdmax'
    ftp = xr.open_dataset(path+name)
    fg = xr.open_dataset(path+gname)
    fg1 = fg['nepal_aftclip.tif'][:]
    # print(fg)
    # print(fg1)
    # print(ftp)
    k = 0
    for i in tqdm(range(len(ftp.latitude))):
        for j in (range(len(fg.lon))):
            if ftp.latitude[i] == fg.lat[i] and ftp.longitude[j] == fg.lon[j]:
                k = k + 1
            else:
                break
    print(k)
    # fv = xr.open_dataset(path+v_name)
    # print(ftp['time'])
    # print(fg)
    # for i in tqdm(ftp['time']):
    #     pass
    # # print(fv)
    # print(os.listdir(path+Tmax))
    # print(len(os.listdir(path+Tmax)))
    # for i in tqdm((os.listdir(path+Tmax))):
    #     pass
    #     # print(i)


if __name__ == '__main__':
    main()


