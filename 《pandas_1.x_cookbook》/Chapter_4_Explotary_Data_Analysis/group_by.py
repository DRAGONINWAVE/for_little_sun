import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')


mask  = vehicle.make.isin(
    ["Ford", "Honda", "Tesla", "BMW"]
)
print(
    vehicle[mask].groupby('make').city08.agg(
        ["mean", "std"]
    )
)

g = sns.catplot(
    x = 'make',
    y = 'city08',
    data = vehicle[mask],
    kind = 'box'
)
g.ax.figure.savefig('catplot.png',dpi=300)