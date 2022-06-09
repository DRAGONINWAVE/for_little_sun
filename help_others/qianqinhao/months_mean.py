import pandas as pd
import os

# from my_work.temperature_change import s1_T, data0

filepath = r'D:\TD\help_others\qianqinhao\二步处理\\'
Filename = 'cleared_dropna'
df = pd.read_excel(filepath+ Filename +'.xlsx')
names = df.columns.values
print(names)
counts = 0
s23_T = 0
m78_T = 0
average_s23_T = []
average_7_8 = []
average_y_T = []
year = []
season23 = list(range(4, 10))
season7_8 = list(range(7,9))
print(df)
for i in range(1951,2018):
    y_T = 0
    day = 0
    day23 = 0
    day78 = 0
    for days in range(1,31*12):
        if i ==df.年[counts]:
            y_T = y_T + df.平均[counts]
            if df.月[counts] in season23:
                s23_T = s23_T + df.平均[counts]
                day23 = day23 + 1
            if df.月[counts] in season7_8:
                m78_T = m78_T + df.平均[counts]
                day78 = day78 + 1
            day = day + +1
            counts = counts + 1
        if counts == len(df.年):
            break

    if day != 0 and day23 != 0:
        y_T = y_T /day
        s23_T = s23_T /day23
        m78_T = m78_T / day78

        average_y_T.append(y_T)
        average_s23_T.append(s23_T)
        average_7_8.append(m78_T)
        year.append(df.年.values[counts - 1])

data0 = pd.DataFrame(dict(Year=year,Tmean=average_y_T,S23=average_s23_T,M78=average_7_8))
print(data0)
data0.to_excel('YearMean.xlsx',index=False)
print('ok')



