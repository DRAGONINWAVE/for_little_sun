import matplotlib.pyplot as plt
import pandas as pd
import time

file = 'D:\TD\help_others\qianqinhao\二步处理\\YearMean3.xlsx'
df = pd.read_excel(file)
# print(df)
names = ['四到九月平均气温距平','七八月平均气温距平','四到九月大于十三度的积温距平','四到九月降水量距平','五到八月日照时数距平']
# s = names[i]
f1 = plt.figure()
plt.rcParams['font.sans-serif'] = ['SimSun']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
print(df.年)
plt.bar(df.年,df.四到九月平均气温距平,fc='black')
plt.xlabel(u'年份')
plt.ylabel(u'气温距平（℃）')
# plt.show()
f1.savefig('bar' +'四到九月平均气温距平'+ str(time.strftime("%Y%m%d%H%M%S")),dpi = 200)