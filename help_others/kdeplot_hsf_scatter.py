import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import time
import os


start_time = time.time()
# # season = ['春','夏','秋','冬']
# # 清理数据并保存到指定文件夹
# raw_path = r'D:\piles\wuxi_four_seasons'
# names = os.listdir(raw_path)
# print(names)
# for name in names:
#     raw_data = pd.read_excel('D:\\piles\\wuxi_four_seasons\\'+name)
#     cleared_data = raw_data.dropna()
#     cleared_data.to_excel('D:\\TD\\help_others\\hsf_kdeplot\\'+name,index=False)

#设置大的画图背景，为白色
sns.set_theme(style='dark')
f, axes = plt.subplots(3,4,
                       figsize=(36,27),
                       # sharex = True
                       )
i = 4
k = 1
l = 0
for ax, s in zip(axes.flatten(order='F'), np.linspace(0, 3, 12)):
    # print(ax)
    plt.sca(ax)
    cmaps = sns.cubehelix_palette(start=s,light=1,as_cmap=True)
    season = ['Spring','Summer','Fall','Winter']
    cleared_data1 = pd.read_excel('D:\\TD\\help_others\\hsf_kdeplot\\'+season[l]+'.xlsx')
    ls = cleared_data1.columns.values[-4:]
    y = cleared_data1.iloc[:, -4].values  # 因变量
    x = cleared_data1.iloc[:, i].values
    df = pd.DataFrame(dict(x1 = x,JAN_tem=y))
    if ls[k] == 'NDVI':
        df = df.drop(df[(df['x1']< 0)].index)
        # df.to_excel('NDVI'+season[l]+'.xlsx',index=False)
    # sns.kdeplot(
    #     x = 'x1' , y = 'JAN_tem',
    #     data = df,
    #     cmap = 'rocket',
    #     # color = '#DC143C',
    #     levels = 5,
    #     # fill = True,
    #     thresh=.2,
    #     ax=ax,
    # )
    plt.scatter(
        df.x1, df.JAN_tem,
        # data=df,
        # color = '#00CED1',
        # color = 'blue',
        # marker = '+',
        # levels=10,
        # fill=True,
        # thresh=.2,
        # alpha = 0.2,
        # ax=ax,
    )
    x1_1 = list(df.x1)

    res = stats.linregress(x1_1,df.JAN_tem)
    print(res)
    p = sns.regplot(x='x1', y='JAN_tem', data=df,ci=None,scatter=False,
                label=f'y={res.slope:.2f}*x+{res.intercept:.2f} \n R\u00b2 ={res.rvalue**2:.2f}',
                # locals = 'right',
                ax=ax,
                color = 'black'
                )
    plt.xlabel(season[l]+'_'+ls[k])
    plt.ylabel(season[l]+'_'+ls[0]+'(°C)')
    p.legend(loc = 'upper right')
    k = k + 1
    i = i + 1
    if k == 4:
      k = 1
      l = l + 1
      i = 4
    p.legend()
    sns.rugplot(df.x1,
                color="b",
                ax=ax)
    sns.rugplot(df.JAN_tem,
                vertical=True,
                 ax=ax,
                color='b')

    # ax.set(xlim=(-1, 1),
    #        # ylim=(-25,45)
    #        )
# f.subplots_adjust(0, 0, 1, 1, .08, .08)
kdeplot_fig = f.get_figure()
kdeplot_fig.savefig(str(time.strftime("%Y%m%d%H%M%S")))
end_time = time.time()
print('cost_time',end_time-start_time,'s')