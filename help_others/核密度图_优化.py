import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import scipy as stats
import time



#导入数据
raw_data = pd.read_excel(r'D:\piles\冬季温度及其各类影响指数.xlsx')
#清理数据，删除所有存在空白数据的行
cleared_data = raw_data.dropna()
#保存数据到当前文件夹
cleared_data.to_excel('冬季温度及其各类影响指数_c1.xlsx')
# JAN_NDVI_c = cleared_data['JAN_NDVI_c'] #自变量
# JAN_NDBI_C = cleared_data['JAN_NDBI_C'] #自变量
# JAN_MNDWI_ = cleared_data['JAN_MNDWI_'] #自变量
y = cleared_data.loc[3].values  #因变量
print(type(y),y)

#设置大的画图背景，为白色
sns.set_theme(style='white')

#设置plt的参数
f , axes = plt.subplot(1,2,figsize=(6,12),sharex=True)

for ax, s in zip(axes.flat,np.linspace(0,3,10)):
    i = 4
    cmap = sns.cubehelix_palette(start=s,light=1,as_cmap=True)
    x = np.ndarray(cleared_data[i])
    print(x)
    sns.kdeplot(
        x = x , y = y,
        levels = 15,
        fill = True
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







