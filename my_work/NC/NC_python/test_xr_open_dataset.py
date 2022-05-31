import xarray as xr
ds = xr.open_dataset('F:\\Nepal_ET0\Tmax\\202012.nc')
monthly_data = ds.resample(freq = 'd2m', dim = 'time', how = 'mean')
