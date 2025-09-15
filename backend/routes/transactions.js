const express = require('express');
const router = express.Router();
const axios = require('axios');

let TX_STORE = []; // simple in-memory transaction store

// --- POST /api/transactions/ingest ---
router.post('/ingest', async (req, res) => {
  const tx = req.body;

  try {
    // 1. Classification
    const clfResp = await axios.post(
      'http://127.0.0.1:8000/predict/transaction',
      tx,
      { timeout: 5000 }
    );
    const clf = clfResp.data;

    // 2. Anomaly detection (✅ wrap in array, unwrap response)
    const anResp = await axios.post(
      'http://127.0.0.1:8000/anomaly/check',
      [tx],
      { timeout: 5000 }
    );
    const an = anResp.data;

    // --- Enriched transaction ---
    const enrichedTx = {
      ...tx,
      category: clf.label,
      prob: clf.prob,
      is_anomaly: an.results[0].is_anomaly
    };

    // Store last 200 transactions
    TX_STORE.push(enrichedTx);
    if (TX_STORE.length > 200) TX_STORE.shift();

    res.json(enrichedTx);
  } catch (e) {
    console.error('ML call failed', e.message);
    const fallbackTx = {
      ...tx,
      category: null,
      prob: null,
      is_anomaly: null,
      note: 'ML service unavailable'
    };
    TX_STORE.push(fallbackTx);
    if (TX_STORE.length > 200) TX_STORE.shift();
    res.status(200).json(fallbackTx);
  }
});

// --- GET /api/transactions ---
router.get('/', (req, res) => {
  res.json(TX_STORE.slice(-200)); // return last 200
});

module.exports = router;
