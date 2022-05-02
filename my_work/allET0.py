import pandas as pd
import matplotlib as plt
import os
from scipy import stats
import math
import numpy as np
from pandas import Series
import seaborn as sns

names = os.listdir(r'D:\TD\my_work\data')
# print(names)
# all_ET0 = pd.DataFrame(ET0_PMT_CF=ET0_PMT_CF,)
ET0_PMT_CF = 0
ET0_PMT_G = 0
ET0_PMT = 0
for name in names:
    print(name)
    # ea = []
    df_raw = pd.read_excel('D:\TD\my_work\data\\'+name)
    # print(type(df_raw.ET0_PMT_CF))

    ET0_PMT_CF += df_raw.ET0_PMT_CF
    ET0_PMT_G += df_raw.ET0_PMT_G
    ET0_PMT += df_raw.ET0_PMT


all_data = pd.DataFrame(dict(ET0_PMT_CF=ET0_PMT_CF,ET0_PMT_G=ET0_PMT_G,ET0_PMT=ET0_PMT,))
# plt.plot(all_data.ET0_PMT,all_data.ET0_PMT_CF)
# plt.plot(all_data.ET0_PMT,all_data.ET0_PMT_G)
# plt.show()
res1 = stats.linregress(list(all_data.ET0_PMT_CF),list(all_data.ET0_PMT))
print(res1,res1.rvalue**2,len(all_data),np.average(all_data.ET0_PMT_CF))
res2 = stats.linregress(list(all_data.ET0_PMT_G),list(all_data.ET0_PMT))
print(res2,res2.rvalue**2)