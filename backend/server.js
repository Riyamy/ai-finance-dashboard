const express = require('express');
const cors = require('cors');
const mongoose = require('mongoose');
const transactions = require('./routes/transactions');

const app = express();
app.use(cors());
app.use(express.json());

const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/pfinance';
mongoose.connect(MONGO_URI)
  .then(()=> console.log('Connected to MongoDB'))
  .catch(err=> console.error('MongoDB connection error', err));

app.use('/api/transactions', transactions);

app.get('/api/health', (req, res) => res.json({ status: 'ok' }));

const PORT = process.env.PORT || 4000;
app.listen(PORT, ()=> console.log(`Backend running on ${PORT}`));
