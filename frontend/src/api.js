import axios from 'axios';

const API_BASE = process.env.REACT_APP_API_BASE || 'http://localhost:4000/api';

export const fetchTransactions = async () => {
  const r = await axios.get(`${API_BASE}/transactions`);
  return r.data;
};

export const ingestTransaction = async (tx) => {
  const r = await axios.post(`${API_BASE}/transactions/ingest`, tx);
  return r.data;
};

// ✅ NEW: check anomaly
export const checkAnomaly = async (tx) => {
  const r = await axios.post(`${API_BASE}/anomaly/check`, tx);
  return r.data;
};
