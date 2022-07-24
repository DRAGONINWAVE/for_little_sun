import aiohttp
import asyncio
import time

async def main():
    async with aiohttp.ClientSession() as session:
        # 抓取 150 個網址
        for number in range(1, 151):
            # 指定網站網址
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            # 以 aiohttp 擷取網頁資料
            async with session.get(pokemon_url) as resp:
                # 取得 JSON 資料
                pokemon = await resp.json()
                print("%d：%s" % (number, pokemon['name']))


start = time.perf_counter() # 開始測量執行時間

# 執行協同程序
asyncio.run(main())

elapsed = time.perf_counter() - start # 計算程式執行時間
print("執行時間：%f 秒" % elapsed)