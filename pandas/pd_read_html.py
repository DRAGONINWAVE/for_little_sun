import pandas as pd

# from spider.run2 import hh

# url = "http://www.tianqihoubao.com/lishi/beijing/month/201101.html"
# # xx=[]
# df = pd.read_html(url)
# # df.to_excel()
# print(df[0],type(df),df.tail())
# # data = pd.DataFrame(df)
dfs = pd.read_html('https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Sweden',
                  match='New COVID-19 cases in Sweden by county')
dfs[0].tail()