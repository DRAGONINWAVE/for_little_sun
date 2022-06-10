import pandas as pd
import os

# from my_work.temperature_change import s1_T, data0
from PIL.ImageChops import difference

filepath = r'D:\TD\help_others\qianqinhao\二步处理\\'
Filename = 'cleared_dropna'
df = pd.read_excel(filepath+ Filename +'.xlsx')
p = pd.read_excel('D:\TD\help_others\qianqinhao\\P_cleared_dropna.xlsx')
names1 = df.columns.values
names2 = p.columns.values
print(names1,names2)
counts = 0
s23_T = 0
m78_T = 0
average_s23_T = []
average_7_8 = []
average_y_T = []
day_all_35_y = []
day78_35_y = []
AT_49_y = []
P_49_y = []
year = []
start_y = []
end_y = []
difference_y = []
season23 = list(range(4, 10))
season7_8 = list(range(7,9))
for i in range(1951,2018):
    y_T = 0
    AT_49  = 0
    day = 0
    day23 = 0
    day78 = 0
    day_all_35 = 0
    day78_35 = 0
    start = 0
    end = 0
    start1 = 0
    end1 = 0
    b = 0
    c = 0
    for days in range(1,31*12):
        if i ==df.年[counts]:
            start = start + 1
            end = end + 1
            y_T = y_T + df.平均[counts]
            if df.最高[counts]>=35:
                day_all_35 = day_all_35 + 1
            if df.月[counts] in season23:
                s23_T = s23_T + df.平均[counts]
                day23 = day23 + 1
                if df.平均[counts] >= 13:
                    if b == 0:
                        start_y.append(start)
                        start1 = start
                        b = 1
            if df.月[counts] >= 8 :
                if df.平均[counts] <= 20:
                    if c == 0 and end > start1:
                        end_y.append(end)
                        end1 = end
                        c = 1
            if df.月[counts] in season7_8:
                m78_T = m78_T + df.平均[counts]
                day78 = day78 + 1
                if df.最高[counts] >= 35:
                    day78_35 = day78_35 + 1
                if df.平均[counts] >= 13:
                    AT_49 = AT_49 + df.平均[counts]
            day = day + 1
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
        day_all_35_y.append(day_all_35)
        AT_49_y.append(AT_49)
        day78_35_y.append(day78_35)
        difference_y.append(end1-start1)

dayP_49_y = []
dayP_6_y = []
counts1 = 0
for l in range(1951,2018):
    dayP_49 = 0
    dayP_6 = 0
    for days in range(1,31*12):
        if l == p.年[counts1]:
            if p.月[counts1] in season23:
                dayP_49 = dayP_49 + p.累计降水量[counts1]
                # print(dayP_49)
            if p.月[counts1] == 6 :
                dayP_6 = dayP_6 + p.累计降水量[counts1]
            counts1 = counts1 + 1
        if counts1 == len(p.年):
            break
    dayP_49_y.append(dayP_49)
    dayP_6_y.append(dayP_6)

R = pd.read_excel('D:\TD\help_others\qianqinhao\\R_cleared_dropna.xlsx')
month58=list(range(5,9))
dayR_58_y = []
y = list(range(1953,2018))
counts2 = 0
for a in range(1951,2018):
    dayR_58 = 0
    for days in range(1,31*12):
        if a == R.年[counts2]:
            if R.月[counts2] in month58:
                dayR_58 = dayR_58 + R.日照时数[counts2]
                # print(dayP_49)1
            counts2 = counts2 + 1
        if counts2 == len(R.年):
            break
    dayR_58_y.append(dayR_58)
print(len(start_y),len(end_y))
data0 = pd.DataFrame(dict(
                          年=year,
                          年平均气温=average_y_T,
                          四到九月平均气温=average_s23_T,
                          七八月平均气温=average_7_8,
                          日最高气温大于35度日数=day_all_35_y,
                          四到九月大于13度的积温=AT_49_y,
                          七八月大于35度日数=day78_35_y,
                          四到九月降水量=dayP_49_y,
                          六月降水量=dayP_6_y,
                          五到八月日照时数=dayR_58_y,
                          起始日序=start_y,
                          终日日序=end_y,
                          持续天数=difference_y
                    ))

print(data0)
data0.to_excel('YearMean2.xlsx',index=False)
print('ok')



