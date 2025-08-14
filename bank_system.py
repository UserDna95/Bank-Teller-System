import logging
from datetime import datetime
from models.bank_account import BankAccount
from models.transaction import TransactionType
from utils.helpers import is_valid_account_number, get_valid_amount
from utils.persistence import save_accounts, load_accounts

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")

# Load existing accounts
accounts = load_accounts()

def transfer_between_accounts(sender, receiver, amount, min_balance=-500.0):
    if not sender.can_withdraw(amount, min_balance):
        logging.warning("Transaction denied. Cannot exceed overdraft limit of -$500")
        return False
    sender.add_transaction(TransactionType.TRANSFER_OUT.value, amount, datetime.now())
    receiver.add_transaction(TransactionType.TRANSFER_IN.value, amount, datetime.now())
    logging.info(f"Transferred ${amount: .2f} to Acct #{receiver.account_number}")
    return True

def account_menu(account):
    min_balance = -500.0

    while True:
        logging.info(f"\nAccount Menu for {account.first_name} {account.last_name} (Acct #{account.account_number})")
        logging.info("1. Deposit Money")
        logging.info("2. Withdraw Money")
        logging.info("3. Transfer Between Existing Accounts")
        logging.info("4. View Transaction History")
        logging.info("5. View Account Balance")
        logging.info("6. Return to System Menu")

        choice = input("Select an option (1-6): ").strip()
        restricted = not account.can_withdraw(0, min_balance)

        if restricted and choice == "2":
            logging.warning("Withdrawals disabled due to overdraft limit.")
            continue

        if choice == "1":
            amount = get_valid_amount("Enter deposit amount: ")
            account.add_transaction(TransactionType.DEPOSIT.value, amount, datetime.now())

        elif choice == "2":
            amount = get_valid_amount("Enter withdrawal amount: ")
            if account.can_withdraw(amount, min_balance):
                account.add_transaction(TransactionType.WITHDRAW.value, amount, datetime.now())
            else:
                logging.warning("Transaction denied. Cannot exceed overdraft limit of -$500")

        elif choice == "3":
            if len(accounts) < 2:
                logging.warning("Need at least two accounts to transfer money")
                continue

            to_acct = input("Enter recipient's 5-digit account number: ").strip()
            if not is_valid_account_number(to_acct) or to_acct not in accounts:
                logging.warning("Recipient account not found")
                continue
            if to_acct == account.account_number:
                logging.warning("Cannot transfer to the same account")
                continue

            amount = get_valid_amount("Enter amount to transfer: ")
            receiver = accounts[to_acct]
            transfer_between_accounts(account, receiver, amount)

        elif choice == "4":
            transactions = account.get_transaction_history()
            if not transactions:
                logging.info("No transactions available")
            else:
                for tns in transactions:
                    logging.info(tns)

        elif choice == "5":
            logging.info(f"Current balance: ${account.get_balance(): .2f}")

        elif choice == "6":
            logging.info("Returning to System Menu")
            break

        else:
            logging.warning("Invalid option, please choose between 1 and 6")

def bank_teller_interface():
    logging.info("Welcome to the Bank Teller System\n")

    while True:
        logging.info("\nSystem Menu")
        logging.info("1. Access Existing Account")
        logging.info("2. Create New Account")
        logging.info("3. View All Accounts")
        logging.info("4. Exit System")

        choice = input("Select an option (1-4): ").strip()

        if choice == "1":
            account_number = input("Enter account number: ").strip()
            if account_number in accounts:
                account_menu(accounts[account_number])
            else:
                logging.warning("Account not found")

        elif choice == "2":
            first_name = input("Enter customer's first name: ")
            last_name = input("Enter customer's last name: ")
            account_number = input("Enter 5-digit account number: ").strip()

            if not is_valid_account_number(account_number):
                logging.warning("Account number must be exactly 5 digits")
                continue

            if account_number in accounts:
                logging.warning("Account already exists")
            else:
                initial_balance = get_valid_amount("Enter initial deposit amount: ", allow_zero=True)
                account = BankAccount(first_name, last_name, account_number, initial_balance)
                accounts[account_number] = account
                logging.info("Account created")
                account_menu(account)

        elif choice == "3":
            if not accounts:
                logging.info("No accounts in the system")
            else:
                for acct in accounts.values():
                    logging.info(f"\nAcct #{acct.account_number} | {acct.first_name} | {acct.last_name} | Balance: ${acct.get_balance(): .2f}")
                    transactions = acct.get_transaction_history()
                    if transactions:
                        logging.info("  Transactions:")
                        for tsn in transactions:
                            logging.info(f"     {tsn}")
                    else:
                        logging.info("No transactions recorded")

        elif choice == "4":
            save_accounts(accounts)
            logging.info("Exiting Bank Teller System.")
            break

        else:
            logging.warning("Invalid option. Please choose between 1 and 4")

# Start the system
if __name__ == "__main__":
    bank_teller_interface()
