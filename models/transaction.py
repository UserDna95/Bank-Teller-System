from datetime import datetime
from enum import Enum

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER_IN = "transfer-in"
    TRANSFER_OUT = "transfer-out"

    @staticmethod
    def is_valid(t_type):
        return t_type.lower() in [t.value for t in TransactionType]

class Transaction:
    def __init__(self, transaction_type, amount, timestamp=None):
        if not isinstance(transaction_type, str) or not TransactionType.is_valid(transaction_type):
            raise ValueError(f"Invalid transaction type. Must be one of: {[t.value for t in TransactionType]}")
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero")
        if timestamp is not None and not isinstance(timestamp, datetime):
            raise TypeError("Timestamp must be a datetime object")

        self.transaction_type = transaction_type.lower()
        self.amount = amount
        self.timestamp = timestamp if timestamp else datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} | {self.transaction_type.title()} | ${self.amount: .2f}"
