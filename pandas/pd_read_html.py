import pandas as pd

url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/"

df = pd.read_html(url)

print(df)