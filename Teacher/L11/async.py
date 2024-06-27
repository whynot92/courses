import asyncio

async def timer1():
    seconds = 0
    while True:
        print("timer1: ", seconds)
        await asyncio.sleep(1)
        seconds += 1

async def timer2():
    seconds = 0
    while True:
        print("timer2: ", seconds)
        await asyncio.sleep(5)
        seconds += 5

async def main():
    task1 = asyncio.create_task(timer1())
    taks2 = asyncio.create_task(timer2())

    await task1
    await taks2

asyncio.run(main())