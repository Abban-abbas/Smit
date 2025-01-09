import os

# Helper function to write transactions to a file
def log_transaction(account_name, transaction):
    filename = f"{account_name}_transactions.txt"
    with open(filename, "a") as file:
        file.write(transaction + "\n")

# Function to create an account
def create_account(name):
    account = {
        "name": name,
        "balance": 0.0,
        "transactions": []
    }
    print(f"Account for {name} created with balance $0.0.")
    return account

# Function to deposit money
def deposit(account, amount):
    if amount <= 0:
        print("Deposit amount must be positive.")
        return account

    account["balance"] += amount
    transaction = f"Deposit: ${amount}. New Balance: ${account['balance']}"
    account["transactions"].append(transaction)
    log_transaction(account["name"], transaction)
    print(transaction)
    return account

# Function to withdraw money
def withdraw(account, amount):
    if amount <= 0:
        print("Withdrawal amount must be positive.")
        return account

    if amount > account["balance"]:
        print("Insufficient balance.")
        return account

    account["balance"] -= amount
    transaction = f"Withdrawal: ${amount}. New Balance: ${account['balance']}"
    account["transactions"].append(transaction)
    log_transaction(account["name"], transaction)
    print(transaction)
    return account

# Function to check balance
def check_balance(account):
    print(f"Current balance: ${account['balance']}")
    return account["balance"]

# Function to print transaction statement
def print_statement(account):
    print(f"Account statement for {account['name']}:")
    if not account["transactions"]:
        print("No transactions found.")
        return

    for transaction in account["transactions"]:
        print(f"- {transaction}")

# Example usage
if __name__ == "__main__":
    # Create an account
    account = create_account("John Doe")

    # Deposit money
    account = deposit(account, 500)

    # Withdraw money
    account = withdraw(account, 200)

    # Check balance
    check_balance(account)

    # Print statement
    print_statement(account)

