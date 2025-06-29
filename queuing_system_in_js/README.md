How to run a Redis server on your machine
Download and compile Redis from redis.io.

Run src/redis-server to start the server (default port 6379).

You can check if it’s running by opening another terminal and running src/redis-cli ping, which should return PONG.

To stop the server, use kill [PID] where PID is the Redis server process ID.

How to run simple operations with the Redis client
Use the Redis CLI: src/redis-cli

Common commands:

SET key value — store a string value

GET key — retrieve the value for a key

HSET hash field value — set a field in a hash

HGET hash field — get a field value from a hash

These commands allow simple key-value or hash manipulations directly in the terminal.

How to use a Redis client with Node JS for basic operations
Install Redis client for Node.js (e.g., redis package).

Connect to the Redis server using the client.

Use async calls like client.set(key, value) and client.get(key) to interact.

Handle connection success and errors with event listeners or try/catc

How to store hash values in Redis
Use commands like HSET and HGET to store and retrieve hash data.

In Node.js Redis client:

js
Copy code
await client.hSet('myhash', 'field1', 'value1');
const val = await client.hGet('myhash', 'field1');
console.log(val); // 'value1'
Hashes are useful for storing related key-value pairs under one Redis key.

How to deal with async operations with Redis
Redis client operations are asynchronous.

Use async/await or promises to wait for operations to complete.

Handle errors with try/catch blocks.

Make sure to properly connect (await client.connect()) before making calls.

How to use Kue as a queue system
Kue is a popular Redis-backed priority job queue for Node.js.

Install kue package.

Create jobs and save them to the queue, and workers to process jobs.

Jobs can have types and priorities, allowing for scalable background job processing.

Example:

js
Copy code
import kue from 'kue';

const queue = kue.createQueue();

const job = queue.create('email', {
  title: 'Send welcome email',
  to: 'user@example.com',
}).save();
How to build a basic Express app interacting with a Redis server
Set up Express server with routes.

Use Redis client inside route handlers to get/set data.

For example, create a GET route that retrieves a value from Redis and sends it as a response.

Example:

js
Copy code
import express from 'express';
import { createClient } from 'redis';

const app = express();
const client = createClient();

await client.connect();

app.get('/', async (req, res) => {
  const value = await client.get('key');
  res.send(`Value for key is: ${value}`);
});

app.listen(3000, () => console.log('Server running on port 3000'));
How to build a basic Express app interacting with a Redis server and queue
Combine Express routes with Kue for background processing.

Route creates jobs in the Redis-backed queue.

Workers listen to the queue to process jobs asynchronously.

This decouples request handling from long-running background tasks.

Example:

js
Copy code
// In route:
app.post('/send_email', (req, res) => {
  const job = queue.create('email', req.body).save();
  res.send(`Job ${job.id} queued`);
});

// In worker script:
queue.process('email', (job, done) => {
  sendEmail(job.data, done);
});
