from modules.function import black, date_time, red, green, yellow, blue, magenta, cyan, white, create_pin, ask_pin, save_json, read_json
import sys

# Bank account class handling user data and transactions
class account:
    def __init__(self, name, email, pin, balance=0):
        self.name = name
        self.email = email
        self.__pin = pin
        self.__balance = balance

    # Validate the PIN entered by user
    def validate(self, entered_pin):
        if entered_pin == self.__pin:
            return True
        raise ValueError(red("❌ PIN DIDN'T MATCH"))

    # Convert object to dictionary for JSON saving
    def to_dict(self):
        return {"name": self.name, "email": self.email, "pin": self.__pin, "balance": self.__balance}

    # Create a new user account
    @classmethod
    def create_account(cls):
        while True:
            name = input("\nENTER YOUR NAME:\t").strip()
            if not name or not name.isalpha():
                print(red("❌ NAME NOT AVAILABLE"))
                continue

            email = input("\nENTER YOUR EMAIL:\t").strip()
            if not email.strip() or not "@" in email:
                print(red("❌ PLEASE ENTER A VALID EMAIL"))
                continue

            # Create a secure PIN
            pin = create_pin()

            # Re-enter PIN for confirmation
            retry_pin = ask_pin("\nPLEASE RE-ENTER YOUR PIN")
            if retry_pin != pin:
                print(red("❌ PIN DIDN'T MATCH"))
                continue

            print(green("\n✅ ACCOUNT CREATED SUCCESSFULLY"))
            return cls(name, email, retry_pin, 0)

    # Login an existing account
    @classmethod
    def login_account(cls):
        user_data = read_json()
        attempt = 3

        while True:
            if not user_data:
                print(red("❌ CREATE AN ACCOUNT FIRST TO LOGIN"))
                continue

            ask = input("\nENTER ID/NAME/EMAIL:\t").strip()
            if not ask:
                print(red("❌ CANNOT BE EMPTY"))
                continue

            # Search for user
            for id, userinfo in user_data.items():
                if ask == id or ask == userinfo["name"] or ask == userinfo["email"]:
                    found_id = id
                    found_user = userinfo
                    break
            else:
                print(red("❌ ACCOUNT NOT FOUND"))
                continue

            # PIN verification attempts
            while attempt > 0:
                pin = ask_pin("\nENTER YOUR PIN TO LOGIN")
                if pin == found_user["pin"]:
                    print(green(f"\n✅ LOGIN SUCCESSFUL. WELCOME {found_user['name']}"))
                    return cls(found_user["name"], found_user["email"], found_user["pin"], found_user["balance"]), found_id
                else:
                    attempt -= 1
                    print(red(f"❌ INCORRECT PIN, {attempt} ATTEMPTS LEFT"))

            print(red("❌ TOO MANY ATTEMPTS, ACCOUNT LOCKED"))
            sys.exit()

    # Display current balance
    def balance(self):
        print(blue(f'\n💵 YOUR CURRENT BALANCE IS {self.__balance:.2f}'))

    # Deposit money into account
    def deposit(self, pin, amount):
        self.validate(pin)

        if amount <= 0:
            print(red("❌ AMOUNT MUST BE POSITIVE"))
            return {"time": date_time(), "type": "FAILED_DEPOSIT", "amount": amount, "balance": self.__balance}
        else:
            self.__balance += amount
            print(green(f"\n✅ SUCCESSFULLY DEPOSITED {amount:.2f}"))

        return {"time": date_time(), "type": "DEPOSIT", "amount": amount}

    # Withdraw money from account
    def withdraw(self, pin, amount):
        self.validate(pin)

        if amount <= self.__balance:
            self.__balance -= amount
            print(green(f"\n✅ SUCCESSFULLY WITHDRAWN {amount:.2f}"))
            return {"time": date_time(), "type": "WITHDRAW", "amount": amount}
        else:
            print(red("\n❌ INSUFFICIENT FUNDS"))
            return {"time": date_time(), "type": "FAILED_WITHDRAW", "amount": amount, "balance": self.__balance}

    # String representation of account
    def __str__(self):
        return f"👤  NAME: {self.name}\n✉️   EMAIL: {self.email}\n💵  BALANCE: {self.__balance}"

             

    



       
