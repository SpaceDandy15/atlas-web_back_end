Python Async Comprehension
This project explores asynchronous programming in Python using async generators, comprehensions, and concurrency with asyncio.

Tasks
0. Async Generator
Create a coroutine async_generator that yields 10 random floats between 0 and 10.

Wait 1 second between each yield using await asyncio.sleep().

1. Async Comprehensions
Write a coroutine async_comprehension that uses async comprehension to collect 10 values from async_generator.

Return the collected values as a list.

2. Run Time for Four Parallel Comprehensions
Write a coroutine measure_runtime that runs async_comprehension 4 times in parallel using asyncio.gather.

Measure and return the total runtime (~10 seconds due to parallel execution).

Concepts Covered
Async generators and comprehensions

async and await syntax

Running coroutines concurrently with asyncio.gather

Type hinting async functions