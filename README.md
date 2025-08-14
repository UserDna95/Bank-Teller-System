# Bank-Teller-System
A simple terminal-based banking system that models customer accounts, transactions, and teller operations. This project is designed with modularity, input validation, and persistent storage using Python's `pickle` module. It serves as a foundational framework for simulating real-world banking operations.

---

## Project Overview

This system allows a bank teller to:
- Create and manage multiple customer bank accounts
- Record deposits, withdrawals, and transfers between accounts
- View transaction history and account balances
- Enforce overdraft limits
- Persist account data across sessions using file serialization
- Reset all data (optional feature)

Accounts are stored in a global dictionary keyed by a 5-digit account number. Transactions are modeled using a dedicated class with built-in validation and formatting. The Teller System acts as the interface for navigating and managing these accounts.

---

### Interpretation

The system is composed of three main components:

- **Transaction Class**: Models individual financial actions with type, amount, and timestamp.
- **BankAccount Class**: Represents a customer account, tracks personal details, transaction history, and balance updates.
- **Teller System**: A CLI interface that allows the teller to manage multiple accounts, perform transactions, and transfer funds.

### Analysis

The Teller System introduces:
- A centralized account registry using a dictionary
- Input validation for all operations
- Overdraft protection using helper functions
- Session persistence using `pickle`
- Modular design for scalability and clarity

This architecture allows the teller to manage multiple accounts with error handling and data integrity.

### Algorithm Summary

#### Transaction Class
- Validate transaction type and amount
- Format timestamp or default to current time
- Provide string representation for display
- Collect user input via static method

#### BankAccount Class
- Validate 5-digit account number
- Store personal details and balance
- Record transactions using the Transaction class
- Update balance based on transaction type
- Display transaction history and balance
- Collect user input via static method

#### Teller System
- Load existing accounts using `pickle`
- Create new accounts and store them in a dictionary
- Access accounts by account number
- Perform deposits, withdrawals, and transfers
- Display account details and transaction history
- Save updated account data after each session
- Optional: Delete all data using `os.remove`

---

## Testing

Unit tests cover:
- Transaction creation and validation
- BankAccount balance updates
- Overdraft enforcement
- Transfer logic
- Edge cases (zero/negative amounts, invalid account numbers)
- Teller System navigation and persistence

Run tests with:

```bash
python -m unittest test_bank_system.py
```
---

## Project Structure

bank-teller-system/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── bank_system.py
├── models/
│   ├── transaction.py
│   └── bank_account.py
├── teller/
│   └── teller_interface.py
├── utils/
│   ├── helpers.py
│   └── persistence.py
├── tests/
│   └── test_bank_system.py
└── data/
    └── accounts.pkl

## Modules used

- datetime for timestamps
- pickle for data persistence
- os for file management
- unittest for testing
- logging for output control

## More features to add to enhance the system

- GUI interface using Tkinter 
- Export transaction history to CSV
- Monthly summaries and analytics
- Password protection for accounts
- Integration with a database (e.g., SQLite)
- Teller authentication and role-based access

## Acknowledgements 

This project was built as a foundational exercise for an introductory Python programming course in object-oriented programming, input validation, and system design. It reflects a student's approach to modeling real-world banking operations in Python, with a lot of room for future enhancements.
