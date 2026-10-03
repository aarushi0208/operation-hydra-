# Financial Fraud Investigation & Money Flow Analysis

## 1. Objective

The objective of this investigation is to analyze a simulated financial
fraud scenario associated with Operation Hydra and trace the movement of
funds through multiple intermediary accounts.

All accounts, transaction identifiers, and wallet identifiers used in
this investigation are fictional demonstration data.

---

## 2. Data Sources

The investigation used two simulated datasets:

1. `transactions.csv` — records simulated financial transactions.
2. `access_logs.csv` — records simulated account-access activity.

No real banking, UPI, cryptocurrency, or personal financial information
was used.

---

## 3. Transaction Summary

A total of 7 successful transactions were recorded.

The simulated transactions show funds moving from a victim account
through intermediary mule accounts and finally to a demonstration
cryptocurrency wallet.

The total value of all recorded transactions is:

**₹83,999**

---

## 4. Simulated Money Flow

The primary flow identified in the transaction data is:

Victim Account
       |
       | ₹25,000
       v
Mule Account 1
       |
       | ₹15,000
       v
Mule Account 2
       |
       | ₹12,000
       v
Demo Crypto Wallet

A second simulated transfer sequence is:

Victim Account
       |
       | ₹10,000
       v
Mule Account 1
       |
       | ₹8,000
       v
Mule Account 2
       |
       | ₹7,000
       v
Demo Crypto Wallet

---

## 5. Transaction Evidence

| Transaction | Source | Destination | Amount | Method |
|---|---|---|---:|---|
| TXN001 | victim001@demo | merchant001@demo | ₹4,999 | UPI |
| TXN002 | victim001@demo | mule001@demo | ₹25,000 | UPI |
| TXN003 | mule001@demo | mule002@demo | ₹15,000 | UPI |
| TXN004 | mule002@demo | crypto_demo_wallet | ₹12,000 | CRYPTO |
| TXN005 | victim001@demo | mule001@demo | ₹10,000 | UPI |
| TXN006 | mule001@demo | mule002@demo | ₹8,000 | UPI |
| TXN007 | mule002@demo | crypto_demo_wallet | ₹7,000 | CRYPTO |

---

## 6. Access-Log Analysis

The simulated access logs show the following sequence:

1. Successful login by `victim001`.
2. Account information was accessed.
3. A UPI request was created.
4. A new beneficiary was added.
5. Multiple transactions were initiated.

The same documentation/test IP address,
`192.0.2.10`, appears in the simulated access records.

This IP is used only as a documentation example and is not evidence of
real attacker infrastructure.

---

## 7. Mule Account Analysis

The transaction records indicate that `mule001@demo` and `mule002@demo`
act as intermediary accounts in the simulated money trail.

The movement can be summarized as:

Victim → Mule 1 → Mule 2 → Demo Crypto Wallet

Such an intermediary structure is useful for demonstrating how
investigators can reconstruct transaction relationships using timestamps,
transaction IDs, account identifiers, and transaction amounts.

---

## 8. Cryptocurrency Transfer Analysis

Two simulated transactions move funds from `mule002@demo` to
`crypto_demo_wallet`.

These transfers are:

- TXN004 — ₹12,000
- TXN007 — ₹7,000

Total simulated transfer to the demonstration crypto wallet:

**₹19,000**

The wallet identifier is fictional and does not correspond to a real
cryptocurrency wallet.

---

## 9. Investigation Methodology

The financial investigation followed these steps:

1. Collect transaction logs.
2. Verify transaction status.
3. Sort transactions chronologically.
4. Identify source and destination accounts.
5. Group transactions by account.
6. Identify intermediary accounts.
7. Trace downstream transfers.
8. Identify cryptocurrency-related transactions.
9. Correlate transaction activity with access logs.
10. Document the simulated money trail.

---

## 10. Findings

The simulated dataset demonstrates several indicators that may warrant
investigation in a real-world case:

- Multiple transfers occurring within a short time period.
- Funds moving through intermediary accounts.
- Rapid downstream movement of funds.
- Conversion or transfer of funds to a cryptocurrency destination.
- Account activity occurring immediately before financial transactions.

These observations are part of the simulated academic scenario and do
not establish that an actual financial crime occurred.

---

## 11. Evidence Limitations

This investigation uses entirely fictional data.

The account names, transaction IDs, wallet identifier, timestamps, and
IP address are demonstration values.

Therefore, the findings cannot be used to attribute criminal activity
to any real person, organization, account, IP address, or cryptocurrency
wallet.

---

## 12. Conclusion

The simulated financial-fraud investigation successfully demonstrates
how transaction and access logs can be correlated to reconstruct a
multi-stage money trail.

The analysis identified the following conceptual flow:

**Victim → Mule Account 1 → Mule Account 2 → Demonstration Crypto Wallet**

This demonstrates the importance of transaction correlation, temporal
analysis, account-link analysis, and evidence preservation during a
financial cybercrime investigation.