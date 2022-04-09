import pandas as pd

File = pd.read_excel(r'D:\TD\help_others\g50468.xlsx')
names = File.columns.values
# print(File)
print(names)
lRs = []
lS = []
lN = []
lyRs = []
lyS = []
lyN = []
counts = 0
for i in range(1977,2017):
    y_Rs = 0
    y_S = 0
    y_N = 0
    if i == File.year[counts]:
        # print(File.year[counts])
        for month in range(1,13):
            day = 0
            m_Rs = 0
            m_S = 0
            m_N = 0
            for days in range(1,32):
                if month == File.mouth[counts]:
                    m_Rs = m_Rs + File.RS[counts]
                    # print(m_Rs)
                    m_S = m_S + File.S[counts]
                    m_N = m_N + File.N[counts]
                    counts = counts + 1
                    day = day + 1
                else:
                    break
            RSmonth_mean = m_Rs / day
            Smonth_mean = m_S / day
            Nmonth_mean = m_N / day
            y_Rs = y_Rs + RSmonth_mean
            y_S = y_S + Smonth_mean
            y_N = y_N + Nmonth_mean
            lRs.append(RSmonth_mean)
            lS.append(Smonth_mean)
            lN.append(Nmonth_mean)
        lyRs.append(y_Rs)
        lyS.append(y_S)
        lyN.append(y_N)
month = list(range(1,13))*40
year = list(range(1977,2017))
month_mean = {'月':month,'RSmonth_mean':lRs,'Smonth_mean':lS,'Nmonth_mean':lN}
# print(month_mean)
year_sum = {'年':year,'y_Rs':lyRs,'y_S':lyS,'y_N':lyN}
# print(year_sum)
MM = pd.DataFrame(data=month_mean)
MM.to_excel('月平均.xlsx')
YM = pd.DataFrame(data=year_sum)
YM.to_excel('年总和.xlsx')
