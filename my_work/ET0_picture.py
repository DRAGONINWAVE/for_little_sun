import seaborn as sns
import os
import pandas as pd
# import numpy as np
import time
from scipy import stats
from matplotlib.ticker import MaxNLocator
# import unicode
import matplotlib.pyplot as plt

start_time = time.time()
path = 'D:\TD\my_work\data1\\'
names = os.listdir(path)
df = pd.read_excel(path + 'all.xlsx')


# print(df)
# i = 1
k = 0
for i in range(13,25):
    sns.set_theme(style='white')
    f1 = plt.figure(figsize=(40,24),
                          # sharex= True,
                    )
    plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号


    s = df.columns[i]
    print(s,i)
    if i == 14:
        # print(s)
        plt.bar(df.Year, df.annual_ET0, fc='black')
        # ax.xaxis.set_ticks_position('bottom')
        # ax.spines['bottom'].set_position(('data', 0))
        # ax.spines['top'].set_color('none')
    else:
        sns.lineplot(data = df,
                     x = 'Year', y = s,
                     color = 'black',
                     marker='o',
                     markersize=30,
                     lw=3
                     )
    y = df.iloc[:,i].values
    res = stats.linregress(list(df.Year), y)
    # print(res)
    if i == 15 or i == 22:
        p = sns.regplot(x='Year', y=s, data=df, ci=None, scatter=False,
                        label=f' y = {res.slope:.4f}x+{res.intercept:.2f} \n R\u00b2= {res.rvalue ** 2:.2f}',
                        # ,\n r = {res.rvalue:.2f}',

                        # locals = 'right',
                        # ax=ax,
                        color='black',
                        # ls='-'
                        # lw = 10,
                        )
    else:
        p = sns.regplot(x='Year', y=s, data=df, ci=None, scatter=False,
                        label=f' y = {res.slope:.4f}x{res.intercept:.2f} \n R\u00b2= {res.rvalue ** 2:.2f}',
                        # ,\n r = {res.rvalue:.2f}',

                        # locals = 'right',
                        # ax=ax,
                        color='black',
                        # ls='-'
                        # lw = 10,
                        )
    font1 = {'family': 'Times New Roman', 'size': 80}
    p.legend(loc='upper right', fontsize=80, prop=font1)

    # i = i + 1
    plt.tick_params(labelsize=80,tickdir='in', length=30, width=5, colors='black',bottom='True',left='True',
               grid_color='r', grid_alpha=1)
    # font = {'fontsize': 80}

    plt.xlabel(u'年代', fontsize=80)
    # axes1.titlesize(80)
    if i == 13 or i == 18 or i == 19:
        plt.ylabel(u'ET0'+u' mm a$^{-1}$',fontsize = 80)
    else:
        plt.ylabel(u'ET0'+u' mm m$^{-1}$',fontsize = 80)
    # # ax.set_title(data[k]+'.'+ls[k],
    #                   fontsize=160,
    #                   y=-0.22,
    #                   pad=0
    #                   )
    # ax.arrow(0,12,0,1,length_includes_head= True)

    # ax.arrow(y, 0, 0., fc='k', ec='k',
    #          length_includes_head= True, clip_on = False)
    k = k + 1
    # ax.tick_params( labelsize=80,tickdir='in', length=6, width=2, colors='black',
    #        grid_color='r', grid_alpha=1)
    # f.plots_adjust(*,*,*,*,*,0.09)
    f1.subplots_adjust(0.1,0.1,1,0.99,0.09,0.27)
    kdeplot_fig = f1.get_figure()
    kdeplot_fig.savefig('D:\TD\my_work\data1\\' + s + str(time.strftime("%Y%m%d%H%M%S")),dpi = 200)

end_time = time.time()
print('cost_time',end_time-start_time,'s')