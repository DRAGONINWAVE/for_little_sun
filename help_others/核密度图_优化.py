import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import time


start_time = time.time()
season = ['春','夏','秋','冬']
# #导入数据
# raw_data = pd.read_excel(r'D:\piles\冬季温度及其各类影响指数.xlsx')
# #清理数据，删除所有存在空白数据的行
# cleared_data = raw_data.dropna()
#保存数据到当前文件夹
# for i in range(4):
#     path = 'D:\\piles\\'+season[i]+'季温度及其各类影响指数.xlsx'
#     raw_data = pd.read_excel(path)
#     cleared_data = raw_data.dropna()
#     cleared_data.to_excel(season[i]+'季温度及其各类影响指数优.xlsx')
# end_time = time.time()
# # print(end_time-start_time)
#
#
# # JAN_NDVI_c = cleared_data['JAN_NDVI_c'] #自变量
# # JAN_NDBI_C = cleared_data['JAN_NDBI_C'] #自变量
# # JAN_MNDWI_ = cleared_data['JAN_MNDWI_'] #自变量
# # y = cleared_data.iloc[:,4].values  #因变量
# # print(type(y),y)

#设置大的画图背景，为白色
sns.set_theme(style='dark')
f, axes = plt.subplots(3,4, figsize=(27,20),
                       # sharex = True
                       )
i = 5
k = 1
l = 0
for ax, s in zip(axes.flatten(order='F'), np.linspace(0, 3, 12)):
    # print(ax)
    plt.sca(ax)
    cmaps = sns.cubehelix_palette(start=s,light=1,as_cmap=True)
    season = ['春','夏','秋','冬']
    cleared_data1 = pd.read_excel('D:\\TD\\help_others\\'+season[l]+'季温度及其各类影响指数优.xlsx')
    ls = cleared_data1.columns.values[-4:]
    y = cleared_data1.iloc[:,4].values  #因变量
    x = cleared_data1.iloc[:,i].values
    df = pd.DataFrame(dict(x1 = x,JAN_tem=y))
    sns.kdeplot(
        x = 'x1' , y = 'JAN_tem',
        data = df,
        cmap = cmaps,
        levels = 10,
        fill = True,
        thresh=.2,
        ax=ax,
    )
    x1_1 = list(x)

    slope1, intercept1, r1, p1_1, std_err1 = stats.linregress(x1_1, y)
    print(slope1, intercept1, r1, p1_1, std_err1)
    p = sns.regplot(x='x1', y='JAN_tem', data=df,ci=None,scatter=False,
                label=f'y={slope1:.2f}*x+{intercept1:.2f}',
                ax=ax
                )
    plt.xlabel(ls[k])
    plt.ylabel(ls[0]+'℃')
    p.legend()
    k = k + 1
    i = i + 1
    if k == 4:
      k = 1
      l = l + 1
      i = 5
    p.legend()
    sns.rugplot(df.x1,
                color="b",
                ax=ax)
    sns.rugplot(df.JAN_tem,
                vertical=True,
                 ax=ax,
                color='b')

ax.set(xlim=(-1, 1), ylim=(-12, 26))
f.subplots_adjust(0, 0, 1, 1, .08, .08)
kdeplot_fig = f.get_figure()
kdeplot_fig.savefig(str(time.strftime("%Y%m%d%H%M%S")))
end_time = time.time()
print('cost_time',end_time-start_time,'s')