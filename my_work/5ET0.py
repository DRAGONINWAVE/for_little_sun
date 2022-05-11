import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import time
from scipy import stats

file = 'D:\TD\my_work\data1\\all.xlsx'

df = pd.read_excel(file)
# print(df)

plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
for i in range(3):
    ET0 = ['ETOmean','ET0_PMT_G','ET0_PMT_CF']
    color = ['black','orange','blue']
    ET = ['ET0-PM','ET0-PMT(kRs_G)','ET0-PMT(kRs)']
    d = ET[i]
    s = ET0[i]
    sns.lineplot(data = df,
                 x = 'Year', y = s,
                 color = color[i],
                 marker='o',
                 # markersize=3,
                 # lw=3
                 )
    y = df[s].values
    res = stats.linregress(list(df.Year), list(y))
    # print(res)
    p = sns.regplot(x='Year', y=s, data=df, ci=None, scatter=False,
                        label=f'{d} y = {res.slope:.4f}x{res.intercept:.2f}',
                        # ,\n r = {res.rvalue:.2f}',

                        # locals = 'right',
                        # ax=ax,
                        color=color[i],
                        # ls='-'
                        # lw = 10,
                        )
    plt.xlabel(u'年代')
    plt.ylabel(u'ET0 mm a$^{-1}$')
    font1 = {'family': 'Times New Roman','size':8}
    p.legend(loc = 'lower right',fontsize = 8,prop=font1)
    p.set_ylim(bottom=0.)


p1 = p.get_figure()
p1.savefig('D:\TD\my_work\data1\\' + 'ET0' + str(time.strftime("%Y%m%d%H%M%S")),dpi = 200)