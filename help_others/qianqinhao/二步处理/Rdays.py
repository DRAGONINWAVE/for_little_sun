import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import time
from scipy import stats

file = 'D:\TD\help_others\qianqinhao\二步处理\\Rmean3.xlsx'
df = pd.read_excel(file)
sns.set_theme(style='white')
f1 = plt.figure()
s = '五到八月日照时数'
plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
# color = ['black','orange','blue','red','green','yellow','magenta','cyan']
# p = p.clear()
# if name[i] = ''
p = sns.lineplot(
data=df,
x = '年',
y = s,
marker = 'o',
color = 'black',
label =f'{s}'
)
y = df[s].values
res = stats.linregress(list(df.年), list(y))
# print(res)
p = sns.regplot(x='年', y=s, data=df, ci=None, scatter=False,
                    label=f' y = {res.slope:.4f}x+{res.intercept:.2f} ',
                          # f'\n R\u00b2= {res.rvalue ** 2:.2f}',
                    # ,\n r = {res.rvalue:.2f}',

                    # locals = 'right',
                    # ax=ax,
                    color='black',
                    # ls='-'
                    # lw = 10,
                    )
font1 = {'family': 'SimSun','size':8}
plt.tick_params(labelsize=8,tickdir='in', length=3, width=2, colors='black',bottom='True',left='True',
           grid_color='r', grid_alpha=1)
plt.xlabel(u'年代')
plt.ylabel(s)
# font1 = {'family': 'Times New Roman','size':8}
p.legend(loc='upper right', fontsize=8, prop=font1)
# p.set_ylim(bottom=0.)

p1 = f1.get_figure()
p1.savefig('D:\TD\help_others\qianqinhao\\二步处理\\' + s + str(time.strftime("%Y%m%d%H%M%S")),
           dpi=200
           )