import argparse, random
import pandas as pd
from faker import Faker

fake = Faker()
MERCHANTS = ['Walmart', 'Amazon', 'Starbucks', 'Shell', 'Netflix', 'LocalMarket', 'InsuranceCo']

def gen_row():
    # Pick a label with some weighting
    label = random.choices(
        ['normal', 'groceries', 'utilities', 'entertainment', 'fraudulent'],
        weights=[0.6, 0.15, 0.1, 0.1, 0.05]
    )[0]

    # Stronger rules so labels correlate with features
    if label == 'fraudulent':
        merchant = random.choice(['Amazon', 'InsuranceCo'])
        amount = round(random.uniform(1000, 3000), 2)
    elif label == 'groceries':
        merchant = random.choice(['Walmart', 'LocalMarket'])
        amount = round(random.uniform(20, 300), 2)
    elif label == 'utilities':
        merchant = random.choice(['Shell', 'InsuranceCo'])
        amount = round(random.uniform(50, 500), 2)
    elif label == 'entertainment':
        merchant = random.choice(['Netflix', 'Starbucks'])
        amount = round(random.uniform(5, 200), 2)
    else:  # normal
        merchant = random.choice(MERCHANTS)
        amount = round(random.uniform(1, 800), 2)

    desc = fake.sentence(nb_words=6)

    return {
        'amount': amount,
        'merchant': merchant,
        'description': desc,
        'label': label   # ✅ only keep essential fields
    }

def main(out, n):
    rows = [gen_row() for _ in range(n)]
    df = pd.DataFrame(rows)
    df.to_csv(out, index=False)
    print(f"Wrote {len(df)} rows to {out}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--out', default='ml_service/data/demo.csv')
    parser.add_argument('--n', type=int, default=2000)
    args = parser.parse_args()
    main(args.out, args.n)
