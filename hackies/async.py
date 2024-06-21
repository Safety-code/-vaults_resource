import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(1) #Simulating some time-consuming operation
    print("Task 1 Completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2) #Simulating another time-consuming operation
    print("Task 2 Completed")

async def main():
    #creating tasks and scheduling them
    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    #allowing tasks to run consurrently
    await asyncio.gather(t1, t2)

#running the main function
asyncio.run(main())

