import pandas as pd
import os

filepath = r'D:\TD\help_others\qianqinhao\二步处理'
# print(len(os.listdir(filepath)))
# for Filename in os.listdir(filepath):
    # print(Filename)
Filename = 'cleared_dropna'
File = pd.read_excel('D:\TD\help_others\qianqinhao\\'+ Filename +'.xlsx')
names = File.columns.values
print(Filename)
print(names)
lRs = []
lS = []
lN = []
lTmean = []
lyRs = []
lyS = []
lyN = []
lyTmean = []

counts = 0
for i in range(1951,2018):
    # print(Filename)
    # y_Rs = 0
    # y_S = 0
    # y_N = 0
    y_Tmean = 0
    # print(str(File.date[counts]).split('-'))
    if i == int(str(File.年[counts])):
        # print(str(File.date[counts]).split('/')[0])
        # print(File.year[counts])
        for month in range(4,10):
            day = 0
            # m_Rs = 0
            # m_S = 0
            # m_N = 0
            m_Tmean = 0
            for days in range(1,32):
                # print(str(File.date[counts]).split('-')[1])
                if month in int(str(File.月[counts])):
                    # print((str(File.date[counts]).split('-')[:]))
                    # m_Rs = m_Rs + File.RS[counts]
                    # print(m_Rs)
                    # m_S = m_S + File.S[counts]
                    # m_N = m_N + File.N[counts]
                    m_Tmean = m_Tmean+ File.平均[counts]
                    counts = counts + 1
                    day = day + 1
                else:
                    break
            if day != 0:
                # RSmonth_mean = m_Rs / day
                # Smonth_mean = m_S / day
                # Nmonth_mean = m_N / day
                Tmonth_mean = m_Tmean / day
                # y_Rs = y_Rs + RSmonth_mean
                # y_S = y_S + Smonth_mean
                # y_N = y_N + Nmonth_mean
                y_Tmean = y_Tmean + Tmonth_mean
                # lRs.append(RSmonth_mean)
                # lS.append(Smonth_mean)
                # lN.append(Nmonth_mean)
                lTmean.append(Tmonth_mean)
        # lyRs.append(y_Rs)
        # lyS.append(y_S)
        # lyN.append(y_N)
        lyTmean.append(y_Tmean/12)
month = list(range(1,13))*40
year = list(range(1951,2018))
month_mean = {
              # '月':month,
              # 'RSmonth_mean':lRs,
              # 'Smonth_mean':lS,
              # 'Nmonth_mean':lN,
              '月平均气温':lTmean
              }
# print(len(month),len(lRs),len(lS),len(lN))
year_sum = {
            '年':year,
            # 'y_Rs':lyRs,
            # 'y_S':lyS,
            # 'y_N':lyN
            '年平均气温':lyTmean
            }
# print(year_sum)
print(len(lTmean),len(lyTmean))
MM = pd.DataFrame(data=month_mean)
MM.to_excel('D:\TD\help_others\qianqinhao\二步处理\\'+Filename+'月平均.xlsx')
# YM = pd.DataFrame(data=year_sum)
# YM.to_excel('D:\TD\help_others\qianqinhao\二步处理\\'+Filename+'年总和.xlsx',index=False)
print(counts)
# counts = 0
