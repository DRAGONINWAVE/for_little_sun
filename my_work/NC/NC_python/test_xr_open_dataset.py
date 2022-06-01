import xarray as xr
ds = xr.open_dataset('F:\\Nepal_ET0\Tmax\\')
monthly_data = ds.resample(freq = 'd2m', dim = 'time', how = 'mean')
