
import { createClient, print } from 'redis';
import { promisify } from 'util';

const client = createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.toString()}`);
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  const get = await promisify(client.get).bind(client);
  get(schoolName)
    .then((value) => {
      console.log(value);
    })
    .catch((err) => {
      console.log(err);
    });
};

const main = async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
};

main();
