from turtle import color

import matplotlib.pylab as plt
import seaborn as sns
import pandas as pd
import datetime,time

from pandas import array
from scipy import stats
from sklearn import linear_model
import numpy as np
import scipy.stats as st
import statsmodels.api as sm
from matplotlib.pyplot import subplot
#读取数据
AF = pd.read_excel(r'D:\piles\冬季温度及其各类影响指数.xlsx')
BF = AF.dropna()
JAN_NDVI_c = BF['JAN_NDVI_c']
JAN_NDBI_C = BF['JAN_NDBI_C']
JAN_tem = BF['     JAN.tem']
JAN_MNDWI_ = BF['JAN_MNDWI_']
# print(max(JAN_tem)) #25+
# print(min(JAN_tem)) #-11-
#开始绘图


p1 = plt.figure(1,figsize=(6,12),sharex=True)
cmaps = sns.cubehelix_palette(start=0,as_cmap=True)
#核密度图，圈圈
y = list(JAN_tem)
ax1 = plt.subplot(3,1,1)
ax2 = plt.subplot(3,1,2)
ax3 = plt.subplot(3,1,3)
plt.sca(ax1)
sns.kdeplot(x=JAN_NDVI_c,y=JAN_tem,
            levels= 15 ,
            cmap=cmaps,
            linewidths=1,
            # color = 'w',
            # thresh=0,
            fill = True,
            )
x1 = list(JAN_NDVI_c)

slope1, intercept1, r1, p1_1, std_err1 = stats.linregress(x1, y)
def myfunc1(x1):
  return slope1 * x1 + intercept1
# print(slope, intercept, r, p, std_err)
mymodel1 = list(map(myfunc1, x1))

plt.plot(x1,mymodel1,linestyle="--")

kdeplot_fig = p1.get_figure()
kdeplot_fig.savefig(str(time.strftime("%Y%m%d%H%M%S")))
#
# p2 = plt.figure()
plt.sca(ax2)
#核密度图，圈圈
sns.kdeplot(x=JAN_NDBI_C,y=JAN_tem,data=AF,
            levels=15,
            cmap=cmaps,
            linewidths=1,
            # color = 'w',
            # thresh=0,
            fill = True,
            )
x2 = list(JAN_NDBI_C)

slope2, intercept2, r2, p2, std_err2 = stats.linregress(x2, y)
def myfunc2(x2):
  return slope2 * x2 + intercept2
# print(slope, intercept, r, p, std_err)
mymodel2 = list(map(myfunc2, x2))

# plt.scatter(x, y)
plt.plot(x2, mymodel2)
#按照时间来保存图片
# kdeplot_fig.savefig(str(time.strftime("%Y%m%d%H%M%S")))
# plt.show()
# plt.close()

plt.sca(ax3)
#核密度图，圈圈
sns.kdeplot(x=JAN_MNDWI_,y=JAN_tem,data=AF,
            levels=15,
            cmap=cmaps,
            linewidths=1,
            # color = 'w',
            # thresh=0,
            fill = True,
            )
x3 = list(JAN_MNDWI_)

slope3,intercept3, r3, p3, std_err3 = stats.linregress(x3, y)

def myfunc3(x3):
  return slope3 * x3 + intercept3

mymodel3 = list(map(myfunc3, x3))

# plt.scatter(x, y)
plt.plot(x3, mymodel3)
#按照时间来保存图片
kdeplot_fig = p1.get_figure()
kdeplot_fig.savefig(str(time.strftime("%Y%m%d%H%M%S")),dpi=500)
plt.show()
plt.close()