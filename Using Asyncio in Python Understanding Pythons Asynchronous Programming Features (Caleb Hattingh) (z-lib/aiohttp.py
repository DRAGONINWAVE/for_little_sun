import aiohttp
import asyncio

async def main():
    async with aiohttp.ClientSession() as session:
        # 指定網站網址
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        # 以 aiohttp 擷取網頁資料
        async with session.get(pokemon_url) as resp:
            # 取得 JSON 資料
            pokemon = await resp.json()
            print(pokemon['name'])

# 執行協同程序
asyncio.run(main())