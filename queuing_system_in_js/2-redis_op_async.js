import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis Client Error', err);
});

// setNewSchool function using callbacks
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

// displaySchoolValue function using callbacks
function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, reply) => {
    if (err) {
      console.log('Error:', err);
      return;
    }
    console.log(reply);
  });
}

// Usage
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
