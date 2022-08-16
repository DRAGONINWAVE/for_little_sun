import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')


mask  = vehicle.make.isin(
    ["Ford", "Honda", "Tesla", "BMW"]
)
print(mask)
print(
    vehicle[mask].groupby('make').city08.count()
)

g = sns.catplot(
    x = 'make',
    y = 'city08',
    data = vehicle[mask],
    kind = 'box'
)

sns.swarmplot(
    x='make',
    y='city08',
    data=vehicle[mask],
    # kind='box',
    color = 'k',
    size = 1,
    ax = g.ax
)
g.ax.figure.savefig('mask_warmplot.png',dpi=300)
#
# g = sns.catplot(
#     x = 'make',
#     y = 'city08',
#     data = vehicle[mask],
#     kind = 'box',
#     col = 'year',
#     col_order = [2012, 2014, 2016, 2018],
#     col_wrap=2
# )
#
# g.axes[0].figure.savefig(
#  "c5-gcatboxcol.png", dpi=300
# )

g = sns.catplot(
    x = 'make',
    y = 'city08',
    data = vehicle[mask],
    kind = 'box',
    hue = 'year',
    hue_order = [2012, 2014, 2016, 2018],
    # col_wrap=2
)

g.ax.figure.savefig(
 "c5-g_hue_catboxcol.png", dpi=300
)