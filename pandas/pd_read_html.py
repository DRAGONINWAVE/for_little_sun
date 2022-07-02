import pandas as pd

url = "http://www.tianqihoubao.com/lishi/beijing/month/201101.html"

df = pd.read_html(url)
# df.to_excel()
print(df)