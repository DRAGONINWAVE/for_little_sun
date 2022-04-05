import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.pyplot import subplot

AF = pd.read_excel(r'D:\piles\冬季温度及其各类影响指数.xlsx')
JAN_NDVI_c = AF['JAN_NDVI_c']
JAN_tem = AF['     JAN.tem']
# print(JAN_tem)
sns.set_theme(style="dark")
f,ax = plt.subplots(figsize=(6,6))

sns.set_style("white")
# sns.scatterplot(x=JAN_NDVI_c, y=JAN_tem, s=5, color=".15")
# sns.histplot(x=JAN_NDVI_c, y=JAN_tem, bins=50, pthresh=.1, cmap="Reds")
sns.kdeplot(x=JAN_NDVI_c, y=JAN_tem, levels=5, color="w", linewidths=1)
plt.save()
plt.show()
# p1 = sns.kdeplot(JAN_NDVI_c.sepal_width, JAN_NDVI_c.sepal_length, cmap="Reds", shade=True, bw=.15)
# plt.show()
