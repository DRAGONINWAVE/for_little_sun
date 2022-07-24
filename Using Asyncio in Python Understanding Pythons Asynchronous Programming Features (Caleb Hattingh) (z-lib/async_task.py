import asyncio
import time


async def hello(x):
    await asyncio.sleep(1)
    return x*x


async def main():
    task = []
    task.append(asyncio.create_task(hello(1)))
    task.append(asyncio.create_task(hello(2)))
    task.append(asyncio.create_task(hello(3)))

    result = await asyncio.gather(*task)

    for r in result:
        print(r)

start_time = time.perf_counter()
asyncio.run(main())
elapsed_time = time.perf_counter() - start_time
print('执行时间%fs'%elapsed_time)

