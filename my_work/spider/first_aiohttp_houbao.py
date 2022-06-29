import aiohttp
import asyncio
import ujson

async def main():
    async with aiohttp.ClientSession() as session:
        # async with session.get('/get'):
        #     pass
        # async with session.post('/post', data=b'data'):
        #     pass
        # async with session.put('/put', data=b'data'):
        #     pass
        # params = [('key', 'value1'), ('key', 'value2')]
        # async with session.get('http://httpbin.org/get',
        #                        params=params) as r:
        #     expect = 'http://httpbin.org/get?key=value2&key=value1'
        #     assert str(r.url) == expect
        # async with session.get('https://api.github.com/events') as resp:
        #     print(resp.status)
        #     print(await resp.read())
        # async with aiohttp.ClientSession() as session:
        #     async with session.post(url, json={'test': 'object'})
    # async with aiohttp.ClientSession(
    #         json_serialize=ujson.dumps) as session:
    #
    #     await session.post(url, json={'test': 'object'})
    #     async with session.get('https://api.github.com/events') as resp:
    #         print(await resp.json())
    #     async with session.get('https://api.github.com/events') as resp:
    #         await resp.content.read(10)
        payload = {'key1': 'value1', 'key2': 'value2'}
        async with session.post('http://httpbin.org/post',
                                data=payload) as resp:
            print(await resp.text())

asyncio.run(main())