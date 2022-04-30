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
i = 1
k = 0
sns.set_theme(style='white')
f1,axes1 = plt.subplots(3,2,
                      figsize=(80,70),
                      # sharex= True,
                    )
plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

for ax in axes1.flatten():
    s = df.columns[i]
    ls = ['气温变化趋势','气温距平变化趋势','第一季度','第二季度','第三季度','第四季度']
    data=['a','b','c','d','e','f']
    # print(df)
    plt.sca(ax)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    # print(s)
    y = df.iloc[:,i].values
    sns.lineplot(
        data=df,
        x = 'Year',y = s,
        color = 'black',
        # width = 5
        # kind="line",
        # ax = ax
        marker='o',
        markersize=30,
        lw = 3
                 )
    res = stats.linregress(list(df.Year),y)
    print(res)
    p = sns.regplot(x='Year', y=s, data=df,ci=None,scatter=False,
                label=f' y = {res.slope:.2f}x{res.intercept:.2f} \n R\u00b2= {res.rvalue**2:.2f}  \n P = {res.pvalue:.2f}',
                    # ,\n r = {res.rvalue:.2f}',

                # locals = 'right',
                ax=ax,
                color = 'black',
                # ls='-'
                # lw = 10,
                )
    font1 = {'family': 'Times New Roman','size':80}
    p.legend(loc = 'upper right',fontsize = 80,prop=font1)

    i = i + 1
    ax.tick_params(labelsize=80,tickdir='in', length=30, width=5, colors='black',bottom='True',left='True',
               grid_color='r', grid_alpha=1)
    # font = {'fontsize': 80}


    # axes1.titlesize(80)
    plt.xlabel(u'年代',fontsize = 80)
    plt.ylabel(u'温度'+u'（℃）',fontsize = 80)
    ax.set_title(data[k]+'.'+ls[k],
                      fontsize=160,
                      y=-0.22,
                      pad=0
                      )
    # ax.arrow(0,12,0,1,length_includes_head= True)

    # ax.arrow(y, 0, 0., fc='k', ec='k',
    #          length_includes_head= True, clip_on = False)
    k = k + 1
# ax.tick_params( labelsize=80,tickdir='in', length=6, width=2, colors='black',
#        grid_color='r', grid_alpha=1)
# f.plots_adjust(*,*,*,*,*,0.09)
f1.subplots_adjust(0.03,0.07,1,0.99,0.09,0.27)
kdeplot_fig = f1.get_figure()
kdeplot_fig.savefig('T'+str(time.strftime("%Y%m%d%H%M%S")),dpi = 200)

sns.set_theme(style='white')
f2,axes2 = plt.subplots(3,2,
                      figsize=(80,70),
                      # sharex= True,
                    )
plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
k1  = 0
for ax in axes2.flatten():
    s = df.columns[i]
    ls1 = ['相对湿度变化趋势','相对湿度距平变化趋势','第一季度','第二季度','第三季度','第四季度']
    data=['a','b','c','d','e','f']
    # print(ls1[k1])
    plt.sca(ax)
    plt.gca().xaxis.set_major_locator(MaxNLocator(integer=True))
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    # print(s)
    y = df.iloc[:,i].values
    sns.lineplot(
        data=df,
        x = 'Year',y = s,
        color = 'black',
        # width = 5
        # kind="line",
        # ax = ax
        marker = 'o',
        markersize = 30,
        lw = 3
                 )
    res = stats.linregress(list(df.Year),y)
    print(res.pvalue)
    p = sns.regplot(x='Year', y=s, data=df,ci=None,scatter=False,
                label=f' y = {res.slope:.2f}x+{res.intercept:.2f} \n R\u00b2= {res.rvalue**2:.2f} \n P = {res.pvalue:.2f}',
                    # ,\n r = {res.rvalue:.2f}',

                # locals = 'right',
                ax=ax,
                color = 'black',
                # ls='-'
                # lw = 10,
                )
    font1 = {'family': 'Times New Roman','size':80}
    p.legend(loc = 'upper right',fontsize = 80,prop=font1)

    i = i + 1
    ax.tick_params(labelsize=80,tickdir='in', length=30, width=5, colors='black',bottom='True',left='True',
               grid_color='r', grid_alpha=1)

    plt.xlabel(u'年代',fontsize = 80)
    plt.ylabel(u'相对湿度'+u'（%）',fontsize = 80)
    ax.set_title(data[k1]+'.'+ls1[k1],fontsize=160,
                        y = -.215,
                        # pad = 10
                      )
    # ax.arrow(0,12,0,1,length_includes_head= True)

    # ax.arrow(y, 0, 0., fc='k', ec='k',
    #          length_includes_head= True, clip_on = False)
    k1 = k1 + 1
# ax.tick_params( labelsize=80,tickdir='in', length=6, width=2, colors='black',
#        grid_color='r', grid_alpha=1)
# f.plots_adjust(*,*,*,*,*,0.09)
f2.subplots_adjust(0.03,0.07,1,0.99,0.09,0.27)
kdeplot_fig = f2.get_figure()
kdeplot_fig.savefig('RH' + str(time.strftime("%Y%m%d%H%M%S")),dpi = 200)

end_time = time.time()
print('cost_time',end_time-start_time,'s')