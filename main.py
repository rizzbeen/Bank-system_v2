from modules.bank_system import account
from modules.function import black, red, green, yellow, blue, magenta, cyan, white, create_pin, ask_pin, save_json, read_json, generate_userid
from modules.crypto import top5_coin, search_coin
import time
import sys

# Terminal Welcome
print(green("\n  💰 WELCOME TO BANK SYSTEM v2 💰"))
print("====================================")
print(cyan("1️⃣  Create New Account"))
print(cyan("2️⃣  Login to Existing Account"))
print(cyan("3️⃣  CRYPTO ANALYTICS"))
print(cyan("4️⃣  Exit"))
print("====================================\n")

# USER INPUT FOR INITIAL MENU
while True:  
    ask = input(green("ENTER YOUR CHOICE:\t")).lower().strip()
    
    if not ask or ask not in ["1", "2", "3", "4"]:
        print(red(" PLEASE ENTER A VALID CHOICE"))
        continue

    if ask == "1":  # Create New Account
        user_data = read_json()
        if not user_data:
            user_data = {}

        user = account.create_account()  # Call create_account classmethod
        uniqueid = generate_userid(user_data)  # Generate unique ID
        user_data[uniqueid] = user.to_dict()  # Save user to dictionary
        save_json(user_data)  # Saving data in  json

        print(green("\nACCOUNT CREATED SUCCESSFULLY"))
        print("\nLOADING.....")
        time.sleep(1)

        # Auto login after creation
        user, uniqueid = account.login_account()
        break

    if ask == "2":  # Login Existing Account
        user, uniqueid = account.login_account()
        break

    if ask == "3":  # Crypto Analytics
        top5_coin()  # Show top 5 coins

        while True:
            ask = input(cyan("\nENTER A CRYPTO/STOCK NAME:\t")).lower().strip()

            if not ask.strip():
                print("ENTER A VALID CRYPTO")
                continue

            try:
                search_coin(ask)  # Search coin by name
            except Exception:
                print("\nSOMETHING WENT WRONG PLEASE TRY AGAIN LATER")

    if ask == "4":  # Exit Program
        print("THANKS FOR USING THIS SIMULATOR")
        sys.exit()


# USER MENU AFTER LOGIN
print(blue(f'\n👋 WELCOME BACK, {user.name}'))
print(magenta("🔹 Account ID:"), uniqueid)
print(cyan("==================================="))
print(green("1️⃣  Check Balance 💵"))
print(green("2️⃣  Deposit Money 💰"))
print(green("3️⃣  Withdraw Money 🏧"))
print(green("4️⃣  Transaction History 📜"))
print(green("5️⃣  USER PROFILE 👤"))
print(green("6️⃣  Logout 🚪"))
print(cyan("===================================\n"))

# USER MENU LOOP
while True:
    user_data = read_json()
    choice = input("\nENTER YOUR CHOICE:\t").strip()

    if not choice or choice not in ["1", "2", "3", "4", "5", "6"]:
        print("PLEASE ENTER A VALID CHOICE")
        continue

    if choice == "1":  # Check Balance
        user.balance()

    if choice == "2":  # Deposit Money 
        pin = ask_pin("\nENTER YOUR PIN TO DEPOSIT")  # Ask for user's PIN

        try:
            amount = int(input("\nENTER THE AMOUNT TO DEPOSIT:\t"))  # Input deposit amount
            deposit_data = user.deposit(pin, amount)  # Call deposit method from account class

        except ValueError as v:  # If PIN invalid or deposit failed
            print(str(v))
            continue

        if deposit_data:  # If deposit succeeded or failed (returns dict)
            # Preserve previous transaction history
            old_transactions = user_data.get(uniqueid, {}).get("transaction", [])

            # Update the user's data with the new balance
            user_data[uniqueid] = user.to_dict()

            # Ensure "transaction" key exists in json
            if "transaction" not in user_data[uniqueid]:
                user_data[uniqueid]["transaction"] = []

            # Add old transactions with the new deposit
            user_data[uniqueid]["transaction"] = old_transactions
            user_data[uniqueid]["transaction"].append(deposit_data)  # Add new transaction

            save_json(user_data)  # Save everything back to json

    if choice == "3":  # Withdraw Money 
        pin = ask_pin("\nENTER YOUR PIN TO WITHDRAW")  # Ask for PIN

        try:
            amount = int(input("\nENTER THE AMOUNT TO WITHDRAW:\t"))  # Withdraw amount
            withdraw_data = user.withdraw(pin, amount)  # Call withdraw method

        except ValueError as v:  # If PIN invalid
            print(str(v))

        if withdraw_data:  # If withdraw succeeded or failed (returns dict)
            # Preserve previous transaction history
            old_transactions = user_data.get(uniqueid, {}).get("transaction", [])

            # Update user JSON with new balance
            user_data[uniqueid] = user.to_dict()

            # Ensure transaction key exists
            if "transaction" not in user_data[uniqueid]:
                user_data[uniqueid]["transaction"] = []

            # Merge old transactions with new withdraw record
            user_data[uniqueid]["transaction"] = old_transactions
            user_data[uniqueid]["transaction"].append(withdraw_data)  # Add new transaction

            save_json(user_data)  # Save everything back

    if choice == "4":  # Transaction History 
        try: 
            for data in user_data[uniqueid]["transaction"]:
                print(f'\nTIME: {data["time"]} | TYPE: {data["type"]} | AMOUNT: {data["amount"]}')
        except:
            print("\nNO TRANSACTION AVAILABLE")

    if choice == "5":  # User Profile 
        print(f'{str(user)}\n📁  ID: {uniqueid}')

    if choice == "6":  # Logout 
        print("THANKS FOR USING THIS SIMULATOR")
        sys.exit()







    
 

