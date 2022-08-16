import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')
# print(vehicle.make.unique())
# print(vehicle.model.unique())
# print(vehicle[['make']])
# print(vehicle[['make']].info(memory_usage='deep'))
# print(vehicle[['make']].assign(make=vehicle.make.astype('category')).info(memory_usage='deep'))
# print(vehicle.select_dtypes('object').columns)
# print(vehicle.drive.unique())
# print(vehicle.drive.sample(5,random_state=42))
# print(vehicle.drive.isna().mean()*100)
# print(vehicle.drive.value_counts())

top_n = vehicle.make.value_counts().index[:6]
print(vehicle.assign(make=vehicle.make.where(vehicle.make.isin(top_n),'Other')).make.value_counts())

fig,ax = plt.subplots(figsize=(10,8))
sns.countplot(
    y = 'make',
    data = (vehicle.assign(make=vehicle.make.where(vehicle.make.isin(top_n),'Other')))
)
fig.savefig('c5.png',dpi = 300)