import asyncio
import time

#@asyncio.coroutine
async def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    res = await asyncio.sleep(1)
    # time.sleep(1)
    # r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()