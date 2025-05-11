Python Async Function
This project explores asynchronous programming in Python using asyncio. You'll learn how to define, execute, and manage asynchronous functions and tasks.

Concepts Covered
async / await syntax

Running async programs with asyncio

Concurrent execution of coroutines

Creating and using asyncio.Task

Generating random delays with random.uniform

Tasks Summary
0. Basic async syntax
Created wait_random, an async function that returns a random delay.

1. Concurrent coroutines
Built wait_n, which runs multiple wait_random coroutines concurrently and returns the delays in ascending order.

2. Measure runtime
Measured the execution time of wait_n and returned the average delay per coroutine.

3. Tasks
Created a non-async function task_wait_random that returns an asyncio.Task wrapping wait_random.

4. Tasks continuation
Wrote task_wait_n using task_wait_random, to run tasks concurrently and return sorted delays.