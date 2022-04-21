import seaborn as sns
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()
path = 'D:\TD\my_work\data1\\'
names = os.listdir(path)
df = pd.read_excel(path + 'all.xlsx')
print(df)
i = 2
sns.set_theme(style='dark')
f,axes = plt.subplots(2,2,
                      figsize=(40,30)
                    )
for ax in axes.flatten(order='F'):
    s = df.columns[i]
    print(s)
    plt.sca(ax)
    p = sns.lineplot(
        data=df,
        x = 'Year',y = s,
        # kind="line",
        # ax = ax
    )
    i = i +1

f.subplots_adjust(0.02,0.03,1,1,0.09,0.08)
kdeplot_fig = f.get_figure()
kdeplot_fig.savefig(str(time.strftime("%Y%m%d%H%M%S")),dpi = 200)
end_time = time.time()
print('cost_time',end_time-start_time,'s')