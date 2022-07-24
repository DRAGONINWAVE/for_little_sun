#Though it's not my first sight,async is so charming.And I love her deeply.
import asyncio
# from asyncio import sleep
import time

async def hello():
    print('Hello...')
    await asyncio.sleep(1)
    print('...async')

async def main():
    await asyncio.gather(hello(),hello(),hello())

#记录开始时间
start_time = time.perf_counter()
#开始运行
asyncio.run(main())
#记录结束时间
elapsed_time = time.perf_counter() - start_time
print('执行时间 %f s'%elapsed_time)
#执行结果：
# Hello...
# Hello...
# Hello...
# async
# async
# async
# 执行时间 1.010781 s