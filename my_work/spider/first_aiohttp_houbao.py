import aiohttp
import asyncio

#test footprint
# async def main():
#
#     async with aiohttp.ClientSession() as session:
#         async with session.get('http://python.org') as response:
#
#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])
#
#             html = await response.text()
#             print("Body:", html[:15], "...")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

async def main():
    async with aiohttp.ClientSession() as session:
        async with session.get('http://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())


asyncio.run(main())