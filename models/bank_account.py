from models.transaction import Transaction, TransactionType
from datetime import datetime

class BankAccount:
    def __init__(self, first_name, last_name, account_number, initial_balance=0.0):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.balance = float(initial_balance)
        self.transactions = []

        if initial_balance > 0:
            self.add_transaction(TransactionType.DEPOSIT.value, initial_balance, datetime.now())

    def can_withdraw(self, amount, min_balance=-500.0):
        return self.balance - amount >= min_balance

    def add_transaction(self, transaction_type, amount, timestamp):
        transaction = Transaction(transaction_type, amount, timestamp)
        self.transactions.append(transaction)

        if transaction_type in [TransactionType.DEPOSIT.value, TransactionType.TRANSFER_IN.value]:
            self.balance += amount
        elif transaction_type in [TransactionType.WITHDRAW.value, TransactionType.TRANSFER_OUT.value]:
            self.balance -= amount
        else:
            raise ValueError("Invalid transaction type")

    def get_transaction_history(self):
        return self.transactions

    def get_balance(self):
        return self.balance
