import os
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt

start_time = time.time()

path = 'D:\TD\my_work\data\\'
names  = os.listdir(path)
for k in range(len(names)):
    df = pd.read_excel(path+names[k])
    # print(k)
    print(df)
    counts = 0
    s1_T = 0
    s2_T = 0
    s3_T = 0
    s4_T = 0
    s1_RH = 0
    s2_RH = 0
    s3_RH = 0
    s4_RH = 0
    s1_ET0 = 0
    s2_ET0 = 0
    s3_ET0 = 0
    s4_ET0 = 0
    s11_ET0 = 0
    s22_ET0 = 0
    s33_ET0 = 0
    s44_ET0 = 0
    year = []
    average_T = []
    average_s1_T = []
    average_s2_T = []
    average_s3_T = []
    average_s4_T = []
    average_RH = []
    average_s1_RH = []
    average_s2_RH = []
    average_s3_RH = []
    average_s4_RH = []
    average_ET0 = []
    average_s1_ET0 = []
    average_s2_ET0 = []
    average_s3_ET0 = []
    average_s4_ET0 = []
    average_s11_ET0 = []
    average_s22_ET0 = []
    average_s33_ET0 = []
    average_s44_ET0 = []
    average_ET0_PMT_G = []
    average_ET0_PMT_CF = []
    # print(len(df.year))
    for i in range(1967,2017):
        y_T = 0
        y_RH = 0
        y_ET0 = 0
        y_ET0_PMT_G = 0
        y_ET0_PMT_CF =  0
        day = 0
        day1 = 0
        day2 = 0
        day3 = 0
        day4 = 0
        season1 = list(range(1,4))
        season2 = list(range(4,7))
        season3 = list(range(7,10))
        season4 = list(range(10,13))
        day5 = 0
        day6 = 0
        day7 = 0
        day8 = 0
        S1 = list(range(3,6))
        S2 = list(range(6,9))
        S3 = list(range(9,12))
        S4 = [1,2,12]
        for days in range(1,31*12):
            # print(df.year[counts],i)
            if i == df.year[counts]:
                # print(i,df.year[counts])
                # print(df.year.values[counts])
                y_T = y_T + df.Tmean[counts]
                y_RH = y_RH + df.RH[counts]
                y_ET0 = y_ET0 + df.ET0_PMT[counts]
                y_ET0_PMT_G = y_ET0_PMT_G + df.ET0_PMT_G[counts]
                y_ET0_PMT_CF = y_ET0_PMT_CF + df.ET0_PMT_CF[counts]
                # print(df.year.values[counts])
                if df.month[counts] in season1:
                    s1_T = s1_T + df.Tmean[counts]
                    s1_RH = s1_RH + df.RH[counts]
                    s11_ET0 = s11_ET0 + df.ET0_PMT[counts]
                    # print(i,df.month[counts])
                    day1 = day1 + 1
                if df.month[counts] in season2:
                    s2_T = s2_T + df.Tmean[counts]
                    s2_RH = s2_RH + df.RH[counts]
                    s22_ET0 = s22_ET0 + df.ET0_PMT[counts]
                    day2 = day2 + 1
                if df.month[counts] in season3:
                    s3_T = s3_T + df.Tmean[counts]
                    s3_RH = s3_RH + df.RH[counts]
                    s33_ET0 = s33_ET0 + df.ET0_PMT[counts]
                    day3 = day3 + 1
                if df.month[counts] in season4:
                    s4_T = s4_T + df.Tmean[counts]
                    s4_RH = s4_RH + df.RH[counts]
                    s44_ET0 = s44_ET0 + df.ET0_PMT[counts]
                    day4 = day4 + 1
                if df.month[counts] in S1:
                    s1_ET0 = s1_ET0 + df.ET0_PMT[counts]
                    day5 = day5 + 1
                if df.month[counts] in S2:
                    s2_ET0 = s2_ET0 + df.ET0_PMT[counts]
                    day6 = day6 + 1
                if df.month[counts] in S3:
                    s3_ET0 = s3_ET0 + df.ET0_PMT[counts]
                    day7 = day7 + 1
                if df.month[counts] in S4:
                    s4_ET0 = s4_ET0 + df.ET0_PMT[counts]
                    day8 = day8 + 1
                day = day + 1
                counts = counts + 1
            # print(day)
            if counts == len(df.year):
                break

        if day != 0 and day1 != 0 and day2 != 0  and day3 != 0 and day4 != 0 and day5 != 0 and day6 != 0 and day7 !=0 and day8 !=0 :
            y_T = y_T / day
            s1_T = s1_T / day1
            s2_T = s2_T / day2
            s3_T = s3_T / day3
            s4_T = s4_T / day4
            y_RH = y_RH / day
            s1_RH = s1_RH / day1
            s2_RH = s2_RH / day2
            s3_RH = s3_RH / day3
            s4_RH = s4_RH / day4
            y_RH = y_RH / day
            s1_RH = s1_RH / day1
            s2_RH = s2_RH / day2
            s3_RH = s3_RH / day3
            s4_RH = s4_RH / day4
            y_ET0 = y_ET0 / day
            s1_ET0 = s1_ET0 / day5
            s2_ET0 = s2_ET0 / day6
            s3_ET0 = s3_ET0 / day7
            s4_ET0= s4_ET0 / day8
            s11_ET0 = s11_ET0 / day1
            s22_ET0 = s22_ET0 / day2
            s33_ET0 = s33_ET0 / day3
            s44_ET0= s44_ET0 / day4
            y_ET0_PMT_G = y_ET0_PMT_G / day
            y_ET0_PMT_CF = y_ET0_PMT_CF / day
            average_T.append(y_T)
            average_s1_T.append(s1_T)
            average_s2_T.append(s2_T)
            average_s3_T.append(s3_T)
            average_s4_T.append(s4_T)
            average_RH.append(y_RH)
            average_s1_RH.append(s1_RH)
            average_s2_RH.append(s2_RH)
            average_s3_RH.append(s3_RH)
            average_s4_RH.append(s4_RH)
            average_ET0.append(y_ET0)
            average_s1_ET0.append(s1_ET0)
            average_s2_ET0.append(s2_ET0)
            average_s3_ET0.append(s3_ET0)
            average_s4_ET0.append(s4_ET0)
            average_s11_ET0.append(s11_ET0)
            average_s22_ET0.append(s22_ET0)
            average_s33_ET0.append(s33_ET0)
            average_s44_ET0.append(s44_ET0)
            average_ET0_PMT_G.append(y_ET0_PMT_G)
            average_ET0_PMT_CF.append(y_ET0_PMT_CF)
            year.append(df.year.values[counts-1])
            # print(year)
            # print(average_T)
        # if counts == len(df.year):
        #     break

    if k == 0:
        data0 = pd.DataFrame(dict(Year=year,Tmean=average_T,S1=average_s1_T,S2=average_s2_T,S3=average_s3_T,S4=average_s4_T,
                                  RHmean = average_RH,s1_RH = average_s1_RH,s2_RH=average_s2_RH,s3_RH = average_s3_RH,s4_RH = average_s4_RH,
                                  ETOmean = average_ET0,s1_ET0 = average_s1_ET0,s2_ET0=average_s2_ET0,s3_ET0 = average_s3_ET0,s4_ET0 = average_s4_ET0,
                                  ET0_PMT_G = average_ET0_PMT_G,ET0_ET0_PMT_CF = average_ET0_PMT_CF,s11_ET0 = average_s11_ET0,s22_ET0=average_s22_ET0,s33_ET0 = average_s33_ET0,s44_ET0 = average_s44_ET0
                                  ))
        # print(len(data0))
        data0.to_excel('D:\TD\my_work\data1\\' + 'YearMean'+names[0],index=False)

    if k == 1:
        data1 = pd.DataFrame(dict(Year=year,Tmean=average_T,S1=average_s1_T,S2=average_s2_T,S3=average_s3_T,S4=average_s4_T,
                                  RHmean=average_RH, s1_RH=average_s1_RH, s2_RH=average_s2_RH, s3_RH=average_s3_RH,s4_RH=average_s4_RH,
                                  ETOmean=average_ET0, s1_ET0=average_s1_ET0, s2_ET0=average_s2_ET0,
                                  s3_ET0=average_s3_ET0, s4_ET0=average_s4_ET0,
                                  ET0_PMT_G=average_ET0_PMT_G, ET0_ET0_PMT_CF=average_ET0_PMT_CF,s11_ET0 = average_s11_ET0,s22_ET0=average_s22_ET0,s33_ET0 = average_s33_ET0,s44_ET0 = average_s44_ET0
                                  ))
        data1.to_excel('D:\TD\my_work\data1\\' + 'YearMean'+names[1],index=False)
        # print(len(data1))

    if k == 2:
        data2 = pd.DataFrame(dict(Year=year,Tmean=average_T,S1=average_s1_T,S2=average_s2_T,S3=average_s3_T,S4=average_s4_T,
                                  RHmean=average_RH, s1_RH=average_s1_RH, s2_RH=average_s2_RH, s3_RH=average_s3_RH,
                                  ETOmean=average_ET0, s1_ET0=average_s1_ET0, s2_ET0=average_s2_ET0,
                                  s3_ET0=average_s3_ET0, s4_ET0=average_s4_ET0,
                                  ET0_PMT_G=average_ET0_PMT_G, ET0_ET0_PMT_CF=average_ET0_PMT_CF,s11_ET0 = average_s11_ET0,s22_ET0=average_s22_ET0,s33_ET0 = average_s33_ET0,s44_ET0 = average_s44_ET0
                                  ))
        data2.to_excel('D:\TD\my_work\data1\\' + 'YearMean'+names[2],index=False)
        # print(len(data2))

    if k == 3:
        data3 = pd.DataFrame(dict(Year=year,Tmean=average_T,S1=average_s1_T,S2=average_s2_T,S3=average_s3_T,S4=average_s4_T,
                                  RHmean=average_RH, s1_RH=average_s1_RH, s2_RH=average_s2_RH, s3_RH=average_s3_RH,
                                  s4_RH=average_s4_RH,
                                  ETOmean=average_ET0, s1_ET0=average_s1_ET0, s2_ET0=average_s2_ET0,
                                  s3_ET0=average_s3_ET0, s4_ET0=average_s4_ET0,
                                  ET0_PMT_G=average_ET0_PMT_G, ET0_ET0_PMT_CF=average_ET0_PMT_CF,s11_ET0 = average_s11_ET0,s22_ET0=average_s22_ET0,s33_ET0 = average_s33_ET0,s44_ET0 = average_s44_ET0
                                  ))
        data3.to_excel('D:\TD\my_work\data1\\' + 'YearMean'+names[3],index=False)
        # print(len(data3))

    if k == 4:
        data4 = pd.DataFrame(dict(Year=year,Tmean=average_T,S1=average_s1_T,S2=average_s2_T,S3=average_s3_T,S4=average_s4_T,
                                  RHmean=average_RH, s1_RH=average_s1_RH, s2_RH=average_s2_RH, s3_RH=average_s3_RH,
                                  s4_RH=average_s4_RH,
                                  ETOmean=average_ET0, s1_ET0=average_s1_ET0, s2_ET0=average_s2_ET0,
                                  s3_ET0=average_s3_ET0, s4_ET0=average_s4_ET0,
                                  ET0_PMT_G=average_ET0_PMT_G, ET0_ET0_PMT_CF=average_ET0_PMT_CF,s11_ET0 = average_s11_ET0,s22_ET0=average_s22_ET0,s33_ET0 = average_s33_ET0,s44_ET0 = average_s44_ET0
                                  ))
        data4.to_excel('D:\TD\my_work\data1\\' + 'YearMean'+names[4],index=False)

# counts = 0
# counts0 = 0
# counts2 = 0
# Tmean1_collection = []
# for y in range(1966,2017):
#     Tmean1 = 0
#     print(y,data1.Year[counts])
#     if y == data1.Year[counts] and y == data3.Year[counts] and y == data4.Year[counts] and y == data0.Year[counts0] and y == data2.Year[counts2]:
#         # print(counts)
#         Tmean1 = data0.Tmean[counts0] + data1.Tmean[counts] + data2.Tmean[counts2] + data3.Tmean[counts] + data4.Tmean[counts]
#         Tmean1 = Tmean1 / 4
#         Tmean1_collection.append(Tmean1)
#         counts = counts + 1
#     if y != data0.Year[counts0]:
#         counts0 = counts0 + 1
#     if y != data2.Year[counts2]:
#         counts2 = counts2 + 1
#     if counts == len(data0):
#         break
#
# print(Tmean1_collection)


print(len(data0),len(data1),len(data2),len(data3),len(data4))
end_time = time.time()
print(end_time-start_time,'s')