import json
import os

FILENAME = "data.json"

def load_data():
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as file:
            json.dump([], file)  # initialize as empty list
    with open(FILENAME, "r") as file:
        return json.load(file)

def save(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

def main():
    print("\n========== Welcome to National Bank ==========")
    print("1- Open a new account")
    print("2- Close an account")
    print("3- Deposit cash")
    print("4- Withdraw cash")
    print("5- Check balance")
    print("6- Apply for loan")
    print("7- Exit")

    val = input("Enter the number: ")

    if not val.isdigit():
        print("Error: Enter a valid number!")
        return main()
    
    choice = int(val)
    if choice == 1:
        open_account()
    elif choice == 2:
        delete_account()
    elif choice == 3:
        deposit()
    elif choice == 4:
        withdraw()
    elif choice == 5:
        check_balance()
    elif choice == 6:
        applyLoan()
    elif choice == 7:
        print("Thanks. Goodbye!")
        exit()
    else:
        print("Error: Invalid option!")
        main()

def open_account():
    data = load_data()
    print("\n==== Open New Account ====")
    name = input("Enter your full name: ")
    age = input("Enter your age: ")
    adhaar = input("Enter your Aadhaar number: ")
    pancard = input("Enter your PAN number: ")

    balance = int(input("Enter initial deposit amount: "))
    password = input("Create a password: ")

    account_number = len(data) + 1  # simple account number generation

    account = {
        "acc-no.": account_number,
        "name": name,
        "age": age,
        "adhaar": adhaar,
        "pancard": pancard,
        "balance": balance,
        "password": password,
        "operation": "active",
        "transactions": []
    }

    data.append(account)
    save(data)

    print(f"Account created successfully! Your Account No. is {account_number}")
    main()

def find_account(acc_no, password):
    data = load_data()
    for account in data:
        if account["acc-no."] == acc_no and account["password"] == password and account["operation"] == "active":
            return account, data
    return None, data

def delete_account():
    print("\n==== Close Account ====")
    acc_no = int(input("Enter your account number: "))
    password = input("Enter your password: ")

    account, data = find_account(acc_no, password)
    if account:
        account["operation"] = "deleted"
        save(data)
        print(f"Account {acc_no} closed successfully!")
    else:
        print("Invalid account number or password!")
    main()

def deposit():
    print("\n==== Deposit Money ====")
    acc_no = int(input("Enter your account number: "))
    password = input("Enter your password: ")

    account, data = find_account(acc_no, password)
    if account:
        amount = int(input("Enter deposit amount: "))
        account["balance"] += amount
        account["transactions"].append(f"Deposited {amount}")
        save(data)
        print(f"Deposited {amount}. New Balance: {account['balance']}")
    else:
        print("Invalid account number or password!")
    main()

def withdraw():
    print("\n==== Withdraw Money ====")
    acc_no = int(input("Enter your account number: "))
    password = input("Enter your password: ")

    account, data = find_account(acc_no, password)
    if account:
        amount = int(input("Enter withdrawal amount: "))
        if account["balance"] >= amount:
            account["balance"] -= amount
            account["transactions"].append(f"Withdrew {amount}")
            save(data)
            print(f"Withdrawn {amount}. New Balance: {account['balance']}")
        else:
            print("Insufficient balance!")
    else:
        print("Invalid account number or password!")
    main()

def check_balance():
    print("\n==== Check Balance ====")
    acc_no = int(input("Enter your account number: "))
    password = input("Enter your password: ")

    account, data = find_account(acc_no, password)
    if account:
        print(f"Your balance is: {account['balance']}")
    else:
        print("Invalid account number or password!")
    main()

def applyLoan():
    print("\nCurrently, loans are not available!")
    main()

if __name__ == "__main__":
    main()
