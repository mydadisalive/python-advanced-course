import asyncio

async def fetch_data(task_name, delay):
    print(f"{task_name} - Fetching data...")
    await asyncio.sleep(delay)
    print(f"{task_name} - Data fetched")
    return {f"{task_name}_data": f"Sample data after {delay} seconds"}

async def main():
    # Run multiple coroutines concurrently
    tasks = [
        fetch_data("Task 1", 2),
        fetch_data("Task 2", 3),
        fetch_data("Task 3", 1)
    ]
    
    results = await asyncio.gather(*tasks)
    print("All tasks completed")
    for result in results:
        print(result)

asyncio.run(main())
