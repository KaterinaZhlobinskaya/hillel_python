import asyncio

background_tasks = set()


async def get_primes_amount(num: int) -> int:
    result = 0
    for i in range(1, num):
        counter = 0
        for j in range(1, i):
            if i % j == 0:
                counter += 1
            if counter > 2:
                break
        if counter < 3:
            result += 1
    return result


async def print_async(num: int):
    r = await get_primes_amount(num)
    print(r)


async def manager():
    global background_tasks
    await asyncio.gather(*background_tasks)


loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

# numbers = [40000, 400, 1000000, 700]
numbers = [4000, 40, 100, 7]
for i in numbers:
    background_tasks.add(print_async(i))

loop.run_until_complete(manager())