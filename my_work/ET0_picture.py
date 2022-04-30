import seaborn as sns
import os
import pandas as pd
# import numpy as np
import time
from scipy import stats
from matplotlib.ticker import MaxNLocator
# import unicode
import matplotlib.pyplot as plt

start_time = time.time()
path = 'D:\TD\my_work\data1\\'
names = os.listdir(path)
df = pd.read_excel(path + 'all.xlsx')
# print(df)
i = 1
k = 0
sns.set_theme(style='white')
f1 = plt.figure(figsize=(80,70),
                      # sharex= True,
                )
plt.rcParams['font.sans-serif']=['SimSun'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号