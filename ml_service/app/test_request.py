import requests

payload = {
    "amount": 50,
    "merchant": "Amazon",
    "description": "groceries",
    "timestamp": "2025-09-16T00:00:00Z"  # optional but good for consistency
}

resp = requests.post("http://127.0.0.1:8000/predict/transaction", json=payload)

print("Status code:", resp.status_code)
print("Response JSON:", resp.json())
