def is_valid_account_number(acct_num):
    return acct_num.isdigit() and len(acct_num) == 5

def get_valid_amount(prompt, allow_zero=False):
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0 or (amount == 0 and not allow_zero):
                print("Amount must be a positive number")
            else:
                return amount
        except ValueError:
            print("Invalid input, only enter in a numeric value")
