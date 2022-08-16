import pandas as pd
import numpy as np
import seaborn as sns
# import matplotlib.pyplot as plt

vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')

print(
    vehicle.rangeA.str.extract(r'([^0-9.])')
    .dropna()
    .apply(lambda row: ''.join(row),axis=1)
    .value_counts()
)
print(
    vehicle.rangeA.fillna('0')
    .str.replace('-','/')
    .str.split('/',expand=True)
    .astype('float')
    .mean(axis=1)
)
print(
    vehicle.rangeA.fillna('0')
    .str.replace('-','/')
    .str.split('/',expand=True)
    .astype('float')
    .mean(axis=1)
    .pipe(lambda str_:pd.cut(str_,10))
    .value_counts()
)