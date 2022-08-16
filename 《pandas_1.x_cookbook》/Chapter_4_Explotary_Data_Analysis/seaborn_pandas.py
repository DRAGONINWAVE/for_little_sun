import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fueleco = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')

fig,axs = plt.subplots(nrows=3,figsize=(10,8))
sns.boxplot(fueleco.city08, ax=axs[0])
sns.violinplot(fueleco.city08, ax=axs[1])
sns.boxenplot(fueleco.city08, ax=axs[2])
fig.savefig("c5-nrows.png", dpi=300)