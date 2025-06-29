import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => console.log('Redis Client Error', err));

client.on('connect', () => {
  console.log('Redis client connected to the server');

  // Use hset to set multiple fields in the HolbertonSchools hash
  client.hset('HolbertonSchools', 'Portland', '50', redis.print);
  client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
  client.hset('HolbertonSchools', 'New York', '20', redis.print);
  client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
  client.hset('HolbertonSchools', 'Cali', '40', redis.print);
  client.hset('HolbertonSchools', 'Paris', '2', redis.print);

  // After setting, get and print all values with hgetall
  client.hgetall('HolbertonSchools', (err, res) => {
    if (err) {
      console.error('Error fetching hash:', err);
    } else {
      console.log(res);
    }
    client.quit(); // Close the client connection
  });
});
