import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')


print(
    vehicle.city08.pipe(
        lambda ser:pd.cut(ser,10)
    )
    .value_counts()
)

fig ,ax = plt.subplots(figsize=(10,8))
vehicle.city08.hist(ax=ax)
fig.savefig(
    "c5-conthistpan.png", dpi=300
)

fig1 ,ax1 = plt.subplots(figsize=(10,8))
sns.distplot(
    vehicle.city08,
    rug=True,
    ax=ax1
)
fig1.savefig(
    'c5-distplot.png', dpi=300
)