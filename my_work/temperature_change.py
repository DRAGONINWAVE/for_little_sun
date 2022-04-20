import os
import pandas as pd
import time

start_time = time.time()

path = 'D:\TD\my_work\data\\'
names  = os.listdir(path)
for name in names:
    df = pd.read_excel(path+name)
    counts = 0
    year = list(range(1967,2017))
    average_T = []
    j = 0
    # print(df.year.values)
    for i in range(1966,2017):
        average_temperature = 0
        for days in range(1,366):
            if i == df.year.values[counts]:
                # print(df.year.values[counts])
                average_temperature = average_temperature + df.Tmean.values[counts]
                counts = counts + 1
            else:
                average_temperatureY = average_temperature/days
                # print(average_temperature)
                average_T.append(average_temperatureY)
                counts = counts + 1
                break

        # print(counts)
    print(len(df.year),366*51,df.year.values[counts])


end_time = time.time()
print(end_time-start_time,'s')