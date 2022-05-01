import matplotlib.pyplot as plt
import pandas as pd
import time

df = pd.read_excel('C:\\Users\Administrator\Desktop\ETO.xlsx')
# print(df)
plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
print(df.月份)
plt.bar(df.月份,df.ET0,fc='black')
plt.xlabel(u'月份')
plt.ylabel(u'ET0' + u'mm/day')
# plt.show()
plt.savefig('bar' + str(time.strftime("%Y%m%d%H%M%S")),dpi = 200)