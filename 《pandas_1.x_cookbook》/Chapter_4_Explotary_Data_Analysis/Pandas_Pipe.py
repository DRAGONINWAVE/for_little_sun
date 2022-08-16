import pandas as pd
import matplotlib.pyplot as plt

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

