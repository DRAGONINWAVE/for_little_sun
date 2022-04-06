import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import time


start_time = time.time()
# #导入数据
# raw_data = pd.read_excel(r'D:\piles\冬季温度及其各类影响指数.xlsx')
# #清理数据，删除所有存在空白数据的行
# cleared_data = raw_data.dropna()
#保存数据到当前文件夹
cleared_data = pd.read_excel('冬季温度及其各类影响指数_c1.xlsx')
# JAN_NDVI_c = cleared_data['JAN_NDVI_c'] #自变量
# JAN_NDBI_C = cleared_data['JAN_NDBI_C'] #自变量
# JAN_MNDWI_ = cleared_data['JAN_MNDWI_'] #自变量
y = cleared_data.iloc[:,4].values  #因变量
# print(type(y),y)

#设置大的画图背景，为白色
sns.set_theme(style='dark')
f, axes = plt.subplots(3, 1, figsize=(9,18),
                       # sharex = True
                       )
i = 5
k = 0
for ax, s in zip(axes.flat, np.linspace(0, 3, 10)):
    # print(ax)
    plt.sca(ax)
    cmaps = sns.cubehelix_palette(start=s,light=1,as_cmap=True)
    ls = ['JAN_NDVI_c','JAN_NDBI_C','JAN_MNDWI_']
    x = cleared_data.iloc[:,i].values
    df = pd.DataFrame(dict(x1 = x,JAN_tem=y))
    sns.kdeplot(
        x = 'x1' , y = 'JAN_tem',
        data = df,
        cmap = cmaps,
        levels = 10,
        fill = True,
        thresh=.2,
        ax=ax,
        # x_label = x_label
    )
    x1_1 = list(x)

    slope1, intercept1, r1, p1_1, std_err1 = stats.linregress(x1_1, y)
    print(slope1, intercept1, r1, p1_1, std_err1)
    p = sns.regplot(x='x1', y='JAN_tem', data=df,ci=None,scatter=False,
                label=f'y={slope1:.2f}*x+{intercept1:.2f}',
                ax=axes[k]
                )
    plt.xlabel(ls[k])
    p.legend()
    sns.rugplot(df.x1,
                color="b",
                ax=ax)
    sns.rugplot(df.JAN_tem,
                vertical=True,
                 ax=ax,
                color='b')
    i = i + 1
    k = k + 1
kdeplot_fig = f.get_figure()
kdeplot_fig.savefig(str(time.strftime("%Y%m%d%H%M%S")))
end_time = time.time()
print('cost_time',end_time-start_time,'s')