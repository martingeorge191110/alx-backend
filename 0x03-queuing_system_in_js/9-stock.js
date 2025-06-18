import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5
  },

];

const app = express();
const client = createClient();

const getItemById = (id) => {
  for (const product of listProducts) {
    if (product.id === id) {
      return product;
    }
  }
};

const reserveStockById = async (itemId, stock) => {
  return promisify(client.set).bind(client)(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
  return promisify(client.get).bind(client)(`item.${itemId}`);
};

app.get('/list_products', (_, res) => {
  return res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = req.params.itemId * 1;
  const product = getItemById(itemId);
  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  const reservedStock = Number.parseInt(await getCurrentReservedStockById(itemId) || 0);
  const currentQunatity = product.stock - reservedStock;
  return res.json({ ...product, currentQunatity });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = req.params.itemId * 1;
  const product = getItemById(itemId);
  if (!product) {
    return res.json({ status: 'Product not found' });
  }
  const reservedStock = Number.parseInt(await getCurrentReservedStockById(itemId) || 0);
  const currentQunatity = product.stock - reservedStock;

  if (currentQunatity > 0) {
    await reserveStockById(itemId, reservedStock + 1);
    return res.json({ status: 'Reservation confirmed', itemId });
  } else {
    return res.json({ status: 'Not enough stock available', itemId });
  }
});

app.listen(1245);
