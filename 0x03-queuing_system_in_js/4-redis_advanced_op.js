import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error.toString()}`);
});


const setHash = (name, value) => {
  client.hset('HolbertonSchools', name, value, print);
};

const printHash = () => {
  client.hgetall('HolbertonSchools', (_err, values) => {
    console.log(values);
  });
};

const main = () => {
  const objs = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2,
  };

  for (const [key, value] of Object.entries(objs)) {
    setHash(key, value);
  }
  printHash();
};

client.on('connect', () => {
  console.log('Redis client connected to the server');
  main();
});
