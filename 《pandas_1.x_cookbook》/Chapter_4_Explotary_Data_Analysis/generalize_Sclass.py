# from ctypes import kind

import pandas as pd
import scipy.stats as ss
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def generalize(ser,match_name,default):
    seen = None
    for match,name in match_name:
        mask = ser.str.contains(match)
        if seen is None:
            seen = mask
        else:
            seen |= mask
        ser = ser.where(~mask,name)
    ser = ser.where(seen,default)
    return ser


vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')
makes = ["Ford", "Tesla", "BMW", "Toyota"]
data = vehicle[vehicle.make.isin(makes)].assign(
    SClass = lambda df_:generalize(
        df_.VClass,[
            ('Seaters','Car'),
            ('Car','Car'),
            ('Utility','SUV'),
            ("Truck", "Truck"),
            ("Van", "Van"),
            ("van", "Van"),
            ("Wagon", "Wagon")
        ],
        'other',
    )
)
print(
    data.groupby(['make','SClass']).size().unstack()
)
print(
    pd.crosstab(data.make,data.SClass)
)
print(
    pd.crosstab(
        [data.year,data.make],
        [data.SClass,data.VClass]
    )
)
fig ,ax = plt.subplots(figsize=(10,8))
data.pipe(
    lambda df_:pd.crosstab(df_.make,df_.SClass)
).plot.bar(ax=ax)

fig.savefig("c5-bar.png", dpi=300, bbox_inches="tight")


res = sns.catplot(
    kind = 'count',
    hue = 'SClass',
    x = 'make',
    data = data,
)

res.fig.savefig("c5-catplot.png",dpi=300, bbox_inches="tight")