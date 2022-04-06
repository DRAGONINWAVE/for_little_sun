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
print(type(y),y)

#设置大的画图背景，为白色
sns.set_theme(style='white')
f, axes = plt.subplots(3, 1, figsize=(9,18), sharex=True)
i = 5
for ax, s in zip(axes.flat, np.linspace(0, 3, 10)):
    cmaps = sns.cubehelix_palette(start=s,light=1,as_cmap=True)
    x = cleared_data.iloc[:,i].values
    # print(x)
    # print(y)
    sns.kdeplot(
        x = x , y = y,
        cmap = cmaps,
        levels = 15,
        fill = True,
        # clip=(-5, 5), cut=10,
        thresh=0,
        # ax=ax,
    )
    x1 = list(x)

    slope1, intercept1, r1, p1_1, std_err1 = stats.linregress(x1, y)
    def myfunc1(x1):
        return slope1 * x1 + intercept1
    # print(slope, intercept, r, p, std_err)

    mymodel1 = list(map(myfunc1, x1))
    plt.plot(x1, mymodel1, linestyle="--")
    i = i + 1
kdeplot_fig = f.get_figure()
kdeplot_fig.savefig(str(time.strftime("%Y%m%d%H%M%S")))
end_time = time.time()
print('cost_time',end_time-start_time,'s')







