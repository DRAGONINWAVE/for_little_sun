import pandas as pd
import pandas_profiling as pp


vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')
report = pp.ProfileReport(vehicle)
report.to_file('vehicles.html')