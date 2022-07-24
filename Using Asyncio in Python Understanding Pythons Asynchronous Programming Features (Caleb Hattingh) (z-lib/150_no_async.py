import requests
import time

start = time.perf_counter() # 開始測量執行時間

for number in range(1, 151):
    pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(pokemon_url)
    pokemon = resp.json()
    print("%d：%s" % (number, pokemon['name']))

elapsed = time.perf_counter() - start # 計算程式執行時間
print("執行時間：%f 秒" % elapsed)