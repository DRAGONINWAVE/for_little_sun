#导入需要的库包
import xarray as xr
import os
import numpy as np
def annex(path,files):
    data_all = []
    a = []
    b = []
    # print(files)
    i = 0
    for file in files:
        f = xr.open_dataset(path + '/' + file)
        # print(f.variables.keys())
        # 读取变量，如果数据过大可以索引，但索引后合成的nc文件无法再索引
        lon = f['lon']
        lat = f['lat']
        time = f['time']
        t2m = f['t2m']

        # concat函数按维度合并
        for t in time:
            a.append(t)
        t_al = xr.concat(a, dim='time')

        for t2m1 in t2m:
            b.append(t2m1)
        t2m_al = xr.concat(b, dim='time')
        i = i + 1
        # print(i)
    print(t_al.shape)
    # 写成dataarray
    T2m_all = xr.DataArray(data=t2m_al, dims=('time', 'lat', 'lon'),
                       coords=dict(time=t_al, lat=lat, lon=lon))
    # dataarray转化为dataset
    ds = xr.Dataset({'t2m':T2m_all})
    return ds

def main():
    path = 'F:\\Nepal_ET0'  # 输入文件存储路径
    folder = os.walk(path)  # 生成器，里面包含三个东西：根目录，根目录下的目录和文件；生成器只能用list读取
    # print(list(folder))
    # files = list(folder)[0][2]  # 选择文件名集合的list
    # ds = list(folder)[0][2][1]
    i = [3,5]
    j = [2,4]
    for s,n in  zip(i,j):

        annex(str(list(os.walk(path))[s][2]),str(list(os.walk(path))[s][0])).to_netcdf('F:\\'+str(list(os.walk(path)[n][1]))+'t2m_al_test.nc')
    # 输出成nc文件
    # ds.to_netcdf(r'F:\\t2m_al_test.nc')


if __name__=='__main__':
    main()


