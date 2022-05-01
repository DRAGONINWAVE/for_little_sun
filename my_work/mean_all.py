import pandas as pd
import os

# from my_work.temperature_change import y_ET0

filepath = r'D:\TD\my_work\data'
# print(len(os.listdir(filepath)))
for Filename in os.listdir(filepath):
    print(Filename)
    File = pd.read_excel('D:\TD\my_work\data\\'+ Filename)
    names = File.columns.values
    # print(Filename)
    # print(names)
    # lRs = []
    # lS = []
    # lN = []
    # lyRs = []
    # lyS = []
    # lyN = []
    mET0 = []
    yET0 = []
    counts = 0
    for i in range(1967,2017):
        # print(Filename)
        # y_Rs = 0
        # y_S = 0
        # y_N = 0
        y_ET0 = 0
        # print(str(File.date[counts]).split('-'))
        if i == int(str(File.year[counts])):
            # print(str(File.date[counts]).split('/')[0])
            # print(File.year[counts])
            for month in range(1,13):
                day = 0
                # m_Rs = 0
                # m_S = 0
                # m_N = 0
                m_ET0 = 0
                for days in range(1,32):
                    # print(str(File.date[counts]).split('-')[1])
                    if month == int(str(File.month[counts])):
                        # print(counts)
                        # print((str(File.date[counts]).split('-')[:]))
                        # m_Rs = m_Rs + File.RS[counts]
                        # # print(m_Rs)
                        # m_S = m_S + File.S[counts]
                        # m_N = m_N + File.N[counts]
                        m_ET0 = m_ET0 + File.ET0_PMT[counts]
                        counts = counts + 1
                        day = day + 1
                    else:
                        break
                if day != 0:
                    #     RSmonth_mean = m_Rs / day
                    #     Smonth_mean = m_S / day
                    #     Nmonth_mean = m_N / day
                    ET0_mean = m_ET0 / day
                    #     y_Rs = y_Rs + RSmonth_mean
                    #     y_S = y_S + Smonth_mean
                    #     y_N = y_N + Nmonth_mean
                    y_ET0 = y_ET0 + ET0_mean
                    #     lRs.append(RSmonth_mean)
                    #     lS.append(Smonth_mean)
                    #     lN.append(Nmonth_mean)
                    mET0.append(ET0_mean)
                # lyRs.append(y_Rs)
                # lyS.append(y_S)
                # lyN.append(y_N)
            yET0.append(y_ET0)
    month = list(range(1,13))*40
    year = list(range(1967,2017))
    month_mean = {
                  # '月':month,
                  'ET0mean':mET0
                  # 'RSmonth_mean':lRs,'Smonth_mean':lS,'Nmonth_mean':lN
                  }
    # print(len(month),len(lRs),len(lS),len(lN))
    year_sum = {
                # '年':year,
                'y_ET0':yET0,
                # 'y_S':lyS,'y_N':lyN
                }
    print(len(mET0))
    print(len(yET0))
    MM = pd.DataFrame(data=month_mean)
    MM.to_excel('D:\TD\my_work\月和年\\'+Filename.split('.')[0]+'月平均.xlsx',index=False)
    YM = pd.DataFrame(data=year_sum)
    YM.to_excel('D:\TD\my_work\月和年\\'+Filename.split('.')[0]+'年总和.xlsx',index=False)
    # print(counts)
    # counts = 0
