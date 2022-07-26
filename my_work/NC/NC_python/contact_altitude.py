import numpy as np
import xarray as xr
import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import cartopy.io.shapereader as shpreader
import salem
import geopandas as gpd
import rasterio
import pymannkendall as mk

f1=xr.open_dataset('/Volumes/Lexi_2/nepal_DEM/elevation_nc/elevation_p01.nc')
ele=f1['nepal_aftclip.tif']
f2=xr.open_dataset('/Volumes/Lexi_2/ERA5/precip/INDEX/R99pTOT_40.nc')
R99=f2['R99pTOT']
f3=xr.open_dataset('/Volumes/Lexi_2/ERA5/precip/INDEX/R95pTOT_40.nc')
R95=f3['R95pTOT']
ele=ele.rename({'lon': 'longitude','lat': 'latitude'})
level=np.arange(330,3001,30)
tmp=per95.groupby_bins(ele,bins=level).mean()
tmp_mean=tmp.mean(dim='time')