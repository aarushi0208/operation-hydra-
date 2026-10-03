import csv
from collections import defaultdict

FILE_PATH = "04_Financial_Fraud/logs/transactions.csv"

transactions = []

with open(FILE_PATH, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["amount"] = float(row["amount"])
        transactions.append(row)

print("=== OPERATION HYDRA: TRANSACTION ANALYSIS ===")
print()

# Total transaction value
total_value = sum(t["amount"] for t in transactions)
print(f"Total transaction value: ₹{total_value:,.2f}")

# Transactions by account
outgoing = defaultdict(float)

for transaction in transactions:
    outgoing[transaction["source_account"]] += transaction["amount"]

print("\nOutgoing amount by account:")
for account, amount in outgoing.items():
    print(f"{account}: ₹{amount:,.2f}")

# Identify accounts receiving funds
incoming = defaultdict(float)

for transaction in transactions:
    incoming[transaction["destination_account"]] += transaction["amount"]

print("\nIncoming amount by account:")
for account, amount in incoming.items():
    print(f"{account}: ₹{amount:,.2f}")

# Identify crypto transfers
crypto_transactions = [
    t for t in transactions
    if t["method"].upper() == "CRYPTO"
]

print("\nCrypto-related transfers:")
for transaction in crypto_transactions:
    print(
        f"{transaction['transaction_id']}: "
        f"{transaction['source_account']} -> "
        f"{transaction['destination_account']} "
        f"₹{transaction['amount']:,.2f}"
    )

# Identify successful transactions
successful = [
    t for t in transactions
    if t["status"].upper() == "SUCCESS"
]

print(f"\nSuccessful transactions: {len(successful)}")

print("\nAnalysis completed successfully.")