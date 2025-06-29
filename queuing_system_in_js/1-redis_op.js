import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis Client Error', err));

async function setNewSchool(schoolName, value) {
  try {
    const reply = await client.set(schoolName, value);
    console.log('Reply:', reply); // Should print 'OK'
  } catch (err) {
    console.error('Error setting value:', err);
  }
}

async function displaySchoolValue(schoolName) {
  try {
    const value = await client.get(schoolName);
    console.log(value);
  } catch (err) {
    console.error('Error getting value:', err);
  }
}

async function main() {
  await client.connect();
  console.log('Redis client connected to the server');

  await displaySchoolValue('Holberton');
  await setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');

  await client.quit();
}

main();
