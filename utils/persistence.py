import pickle

def save_accounts(accounts, filename="data/accounts.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(accounts, f)

def load_accounts(filename="data/accounts.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return {}
