import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

vehicle = pd.read_csv(r'D:\迅雷下载\vehicles.csv.zip')

print(
    vehicle.city08.cov(vehicle.highway08)
)
print(
    vehicle.city08.corr(vehicle.highway08)
)


