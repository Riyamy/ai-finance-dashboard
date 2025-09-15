import React, { useEffect, useState } from 'react';
import { fetchTransactions, ingestTransaction, checkAnomaly } from '../api';
import { LineChart, Line, XAxis, YAxis, Tooltip, PieChart, Pie } from 'recharts';

export default function Dashboard() {
  const [tx, setTx] = useState([]);
  const [loading, setLoading] = useState(true);
  const [anomaly, setAnomaly] = useState(null);

  useEffect(() => {
    load();
  }, []);

  const load = async () => {
    setLoading(true);
    const data = await fetchTransactions();
    setTx(data);
    setLoading(false);
  };

  const simulateIngest = async () => {
    const sample = {
      amount: Math.round(Math.random() * 200),
      merchant: 'Demo',
      description: 'demo tx',
      timestamp: new Date().toISOString(),
    };
    await ingestTransaction(sample);
    load();
  };

  const runAnomalyCheck = async () => {
    if (tx.length === 0) {
      alert('No transactions to check');
      return;
    }
    const lastTx = tx[tx.length - 1]; // check latest transaction
    const result = await checkAnomaly(lastTx);
    setAnomaly(result);
  };

  // Chart data
  const lineData = tx.slice(-30).map((t, i) => ({ name: i, amount: t.amount || 0 }));

  const categoryMap = {};
  tx.forEach((t) => {
    const cat = t.category || 'uncategorized';
    categoryMap[cat] = (categoryMap[cat] || 0) + (t.amount || 0);
  });
  const pieData = Object.keys(categoryMap).map((k) => ({ name: k, value: categoryMap[k] }));

  return (
    <div>
      <div style={{ marginBottom: 10 }}>
        <button onClick={simulateIngest}>Simulate ingest</button>
        <button onClick={runAnomalyCheck} style={{ marginLeft: 10 }}>
          Run Anomaly Check
        </button>
      </div>

      {anomaly && (
        <div style={{ marginBottom: 10 }}>
          <strong>Last Tx Anomaly:</strong>{' '}
          {anomaly.is_anomaly ? '⚠️ Suspicious' : '✅ Normal'}
        </div>
      )}

      <h3>Recent Transactions ({tx.length})</h3>
      {loading ? (
        <div>Loading...</div>
      ) : (
        <>
          <div style={{ display: 'flex', gap: 20 }}>
            <div>
              <LineChart width={500} height={300} data={lineData}>
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="amount" stroke="#8884d8" />
              </LineChart>
            </div>
            <div>
              <PieChart width={300} height={300}>
                <Pie data={pieData} dataKey="value" nameKey="name" outerRadius={80} label />
              </PieChart>
            </div>
          </div>

          {/* ✅ New Transactions Table */}
          <table border="1" cellPadding="5" style={{ marginTop: 20, width: '100%' }}>
            <thead>
              <tr>
                <th>Amount</th>
                <th>Merchant</th>
                <th>Description</th>
                <th>Category</th>
                <th>Anomaly</th>
              </tr>
            </thead>
            <tbody>
              {tx.slice(-10).reverse().map((t, i) => (
                <tr key={i}>
                  <td>{t.amount}</td>
                  <td>{t.merchant}</td>
                  <td>{t.description}</td>
                  <td>{t.category || 'uncategorized'}</td>
                  <td>{t.is_anomaly ? '⚠️' : '✅'}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </>
      )}
    </div>
  );
}
