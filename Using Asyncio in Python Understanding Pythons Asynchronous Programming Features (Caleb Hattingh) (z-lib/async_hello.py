#Though it's not my first sight,async is so charming.And I love her deeply.
import asyncio
# from asyncio import sleep


async def main():
    print('Hello ...')
    await asyncio.sleep(10)
    print('...async')

asyncio.run(main())