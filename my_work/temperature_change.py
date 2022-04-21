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
    counts = 0
    s1_T = 0
    s2_T = 0
    s3_T = 0
    s4_T = 0
    year = []
    average_T = []
    average_s1_T = []
    average_s2_T = []
    average_s3_T = []
    average_s4_T = []
    # print(len(df.year))
    for i in range(1966,2017):
        y_T = 0
        day = 0
        day1 = 0
        day2 = 0
        day3 = 0
        day4 = 0
        season1 = list(range(1,4))
        season2 = list(range(4,7))
        season3 = list(range(7,10))
        season4 = list(range(10,13))
        for days in range(1,31*12):
            # print(df.year[counts],i)
            if i == df.year[counts]:
                # print(i,df.year[counts])
                # print(df.year.values[counts])
                y_T = y_T + df.Tmean[counts]
                # print(df.year.values[counts])
                if df.month[counts] in season1:
                    s1_T = s1_T + df.Tmean[counts]
                    # print(i,df.month[counts])
                    day1 = day1 + 1
                if df.month[counts] in season2:
                    s2_T = s2_T + df.Tmean[counts]
                    day2 = day2 + 1
                if df.month[counts] in season3:
                    s3_T = s3_T + df.Tmean[counts]
                    day3 = day3 + 1
                if df.month[counts] in season4:
                    s4_T = s4_T + df.Tmean[counts]
                    day4 = day4 + 1
                day = day + 1
                counts = counts + 1
            # print(day)
            if counts == len(df.year):
                break

        if day != 0 and day1 != 0 and day2 != 0  and day3 != 0 and day4 != 0:
            y_T = y_T / day
            s1_T = s1_T / day1
            s2_T = s2_T / day2
            s3_T = s3_T / day3
            s4_T = s4_T / day4
            average_T.append(y_T)
            average_s1_T.append(s1_T)
            average_s2_T.append(s2_T)
            average_s3_T.append(s3_T)
            average_s4_T.append(s4_T)
            year.append(df.year.values[counts-1])
            # print(year)
            # print(average_T)
        # if counts == len(df.year):
        #     break

    if k == 0:
        data0 = pd.DataFrame(dict(Year=year,Tmean=average_T,S1=average_s1_T,S2=average_s2_T,S3=average_s3_T,S4=average_s4_T))
        # print(len(data0))
        data0.to_excel('D:\TD\my_work\data1\\' + 'YearMean'+names[0],index=False)

    if k == 1:
        data1 = pd.DataFrame(dict(Year=year,Tmean=average_T,S1=average_s1_T,S2=average_s2_T,S3=average_s3_T,S4=average_s4_T))
        data1.to_excel('D:\TD\my_work\data1\\' + 'YearMean'+names[1],index=False)
        # print(len(data1))

    if k == 2:
        data2 = pd.DataFrame(dict(Year=year,Tmean=average_T,S1=average_s1_T,S2=average_s2_T,S3=average_s3_T,S4=average_s4_T))
        data2.to_excel('D:\TD\my_work\data1\\' + 'YearMean'+names[2],index=False)
        # print(len(data2))

    if k == 3:
        data3 = pd.DataFrame(dict(Year=year,Tmean=average_T,S1=average_s1_T,S2=average_s2_T,S3=average_s3_T,S4=average_s4_T))
        data3.to_excel('D:\TD\my_work\data1\\' + 'YearMean'+names[3],index=False)
        # print(len(data3))

    if k == 4:
        data4 = pd.DataFrame(dict(Year=year,Tmean=average_T,S1=average_s1_T,S2=average_s2_T,S3=average_s3_T,S4=average_s4_T))
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