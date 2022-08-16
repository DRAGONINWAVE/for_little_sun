import pandas as pd
import numpy as np
# from weblib.debug import memory_usage

vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')
# print(vehicle.describe().T.head(5))
# print(vehicle.mean().T.head(5))
# # print(vehicle.quantile([0,0.25,0.5,0.75,1]).T.head(5))
# print(vehicle.dtypes.value_counts())
# print(vehicle.select_dtypes('int64').describe().T)
print(np.iinfo(np.int8))
print(np.iinfo(np.int16))
print(vehicle.columns)
print(vehicle[['city08','comb08']].info(memory_usage='deep'))
print(vehicle[['city08','comb08']].assign(city08 = vehicle.city08.astype(np.int16),
                                          comb08 = vehicle.comb08.astype(np.int16)).info(memory_usage='deep'))