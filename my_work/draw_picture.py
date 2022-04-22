import seaborn as sns
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
from scipy import stats
from matplotlib.ticker import MaxNLocator

start_time = time.time()
path = 'D:\TD\my_work\data1\\'
names = os.listdir(path)
df = pd.read_excel(path + 'all.xlsx')
# print(df)
i = 1
k = 0
sns.set_theme(style='white')
f,axes = plt.subplots(3,2,
                      figsize=(80,60),
                      sharex= True,
                    )
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

for ax in axes.flatten():
    s = df.columns[i]
    ls = ['气温变化趋势','气温距平变化趋势','第一季度','第二季度','第三季度','第四季度']
    # print(df)
    plt.sca(ax)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    print(s)
    y = df.iloc[:,i].values
    sns.lineplot(
        data=df,
        x = 'Year',y = s,
        # kind="line",
        # ax = ax
                 )
    res = stats.linregress(list(df.Year),y)
    print(res)
    # if k == 2 or k == 5 or k == 0 or k == 1:
    #     p = sns.regplot(x='Year', y=s, data=df,ci=None,scatter=False,
    #                 label=f'y={res.slope:.2f}*x{res.intercept:.2f} \n r\u00b2 ={res.rvalue**2:.2f}',
    #                     # ,\n r = {res.rvalue:.2f}',
    #                 # locals = 'right',
    #                 ax=ax,
    #                 color = 'black'
    #                 )
    # else:
    p = sns.regplot(x='Year', y=s, data=df,ci=None,scatter=False,
                label=f'y={res.slope:.2f}*x{res.intercept:.2f} \n R^2 ={res.rvalue**2:.2f}',
                    # ,\n r = {res.rvalue:.2f}',
                # locals = 'right',
                ax=ax,
                color = 'black'
                )
    p.legend(loc = 'upper right',fontsize = 80)
    i = i + 1
    ax.tick_params(labelsize=80,tickdir='in', length=30, width=5, colors='black',bottom='True',left='True',
               grid_color='r', grid_alpha=1)
    # ax.tick_params(axis='x', labelsize=80,direction='in', length=6, width=2, colors='black',
    #            grid_color='r', grid_alpha=1)
    # plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.xlabel('年代',fontsize = 80)
    plt.ylabel(ls[k]+'℃',fontsize = 80)
    # ax.arrow(0,12,0,1,length_includes_head= True)

    # ax.arrow(y, 0, 0., fc='k', ec='k',
    #          length_includes_head= True, clip_on = False)
    k = k + 1
# ax.tick_params( labelsize=80,tickdir='in', length=6, width=2, colors='black',
#        grid_color='r', grid_alpha=1)
f.subplots_adjust(0.05,0.04,1,1,0.09,0.00)
kdeplot_fig = f.get_figure()
kdeplot_fig.savefig(str(time.strftime("%Y%m%d%H%M%S")),dpi = 200)
end_time = time.time()
print('cost_time',end_time-start_time,'s')