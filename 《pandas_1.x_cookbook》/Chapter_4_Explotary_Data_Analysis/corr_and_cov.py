import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')

print(
    vehicle.city08.cov(vehicle.highway08)
)
print(
    vehicle.city08.corr(vehicle.highway08)
)


fig,ax = plt.subplots(figsize=(8,8))
corr = vehicle[["city08", "highway08", "cylinders"]].corr()

mask = np.zeros_like(corr,dtype=np.bool)
print(mask)
mask[np.triu_indices_from(mask)] = True
sns.heatmap(
    corr,
    mask = mask,
    fmt = '.2f',
    annot = True,
    ax = ax,
    cmap = 'RdBu',
    vmin = -1,
    vmax = 1,
    square = True,
)

fig.savefig(
    'c5-heatmap.png',dpi=300,bbox_inches='tight'
)

res =  sns.relplot(
    x     = 'city08',
    y     = 'highway08',
    data  = vehicle.assign(highway08=vehicle.highway08.fillna(0)),
    hue="year",
    size  = 'barrels08',
    alpha = 0.8,
    height = 8
)
res.fig.savefig(
   "c5-relplot2.png", dpi=300, bbox_inches="tight"
)
res1 =  sns.relplot(
    x     = 'city08',
    y     = 'highway08',
    data  = vehicle.assign(highway08=vehicle.highway08.fillna(0)),
    hue="year",
    size  = 'barrels08',
    alpha = 0.8,
    height = 8,
    col = 'make',
    col_order = ['Tesla','Ford']
)
res1.fig.savefig(
   "c5-relplot3.png", dpi=300, bbox_inches="tight"
)


print('end')