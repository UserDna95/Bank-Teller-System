import unittest
from datetime import datetime
from models.bank_account import BankAccount
from models.transaction import Transaction, TransactionType

class TestTransaction(unittest.TestCase):
    def test_transaction_creation(self):
        t = Transaction(TransactionType.DEPOSIT.value, 100.0, datetime(2025, 8, 14, 10, 0))
        self.assertEqual(t.transaction_type, "DEPOSIT")
        self.assertEqual(t.amount, 100.0)
        self.assertEqual(t.timestamp, datetime(2025, 8, 14, 10, 0))
        self.assertIn("DEPOSIT", str(t))

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount("Alice", "Smith", "12345", 500.0)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 500.0)

    def test_deposit(self):
        self.account.add_transaction(TransactionType.DEPOSIT.value, 200.0, datetime.now())
        self.assertEqual(self.account.get_balance(), 700.0)

    def test_withdraw(self):
        self.account.add_transaction(TransactionType.WITHDRAW.value, 100.0, datetime.now())
        self.assertEqual(self.account.get_balance(), 400.0)

    def test_overdraft_limit(self):
        self.assertTrue(self.account.can_withdraw(900.0, min_balance=-500.0))
        self.assertFalse(self.account.can_withdraw(1100.0, min_balance=-500.0))

    def test_transaction_history(self):
        self.account.add_transaction(TransactionType.DEPOSIT.value, 50.0, datetime.now())
        self.account.add_transaction(TransactionType.WITHDRAW.value, 20.0, datetime.now())
        history = self.account.get_transaction_history()
        self.assertEqual(len(history), 2)
        self.assertIn("DEPOSIT", history[0])
        self.assertIn("WITHDRAW", history[1])

class TestTransfers(unittest.TestCase):
    def setUp(self):
        self.sender = BankAccount("Bob", "Jones", "11111", 300.0)
        self.receiver = BankAccount("Carol", "Lee", "22222", 100.0)

    def test_successful_transfer(self):
        result = self.sender.can_withdraw(200.0, min_balance=-500.0)
        self.assertTrue(result)
        self.sender.add_transaction(TransactionType.TRANSFER_OUT.value, 200.0, datetime.now())
        self.receiver.add_transaction(TransactionType.TRANSFER_IN.value, 200.0, datetime.now())
        self.assertEqual(self.sender.get_balance(), 100.0)
        self.assertEqual(self.receiver.get_balance(), 300.0)

    def test_failed_transfer_due_to_overdraft(self):
        result = self.sender.can_withdraw(900.0, min_balance=-500.0)
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
