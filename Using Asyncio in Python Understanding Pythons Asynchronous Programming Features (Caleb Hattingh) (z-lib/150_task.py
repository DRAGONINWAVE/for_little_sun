import aiohttp
import asyncio
import time
from tqdm import tqdm

# 抓取指定編號的網址
async def get_pokemon(session, number):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    # await asyncio.sleep(0.5)
    async with session.get(url) as resp:
        pokemon = await resp.json()
        return "%d：%s" % (number, pokemon['name'])

async def main():
    async with aiohttp.ClientSession() as session:
        # 建立 Task 列表
        tasks = []
        for number in tqdm(range(1, 151)):
            tasks.append(asyncio.create_task(get_pokemon(session, number)))

        # 同時執行所有 Tasks
        original_pokemon = await asyncio.gather(*tasks)

        # 輸出結果
        for pokemon in tqdm(original_pokemon):
            print(pokemon)

start = time.perf_counter() # 開始測量執行時間

# 執行協同程序
asyncio.run(main())

elapsed = time.perf_counter() - start # 計算程式執行時間
print("執行時間：%f 秒" % elapsed)