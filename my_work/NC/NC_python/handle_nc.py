from netCDF4 import Dataset
import numpy as np
import sys
import matplotlib.pyplot as plt
# from mpl_toolkits.basemap import Basemap
from pandas import DataFrame

nc=Dataset('F:\\Nepal_ET0\wind\\u\\200001.nc')
print(nc.variables.keys())

for var in nc.variables.keys():
    data=nc.variables[var][:].data
    print(var,data.shape)