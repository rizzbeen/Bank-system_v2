# Online Banking System V2.0.0

This is an Online Banking Simulator created using Python.
It supports account creation, deposit/withdraw transactions, transaction history, and crypto analytics.

---

## Features

* Create Bank Account.
* Deposit & Withdraw Money.
* Check Balance.
* View Transaction History.
* User Profile Management.
* Auto-login after account creation.
* Crypto Analytics (Top 5 coins, search coin by name).
* Transaction record with timestamp.
* Terminal-based interface with colors and emojis for better readability.

---

## Prerequisites

Be sure you have the following installed on your development machine:

* Python >= 3.9
* Git
* pip
* Virtualenv (virtualenvwrapper is recommended)

---

## Install Required Packages

Install the required Python packages using pip:

```bash
pip install colorama pwinput requests
```

## Project Installation

To setup a local development environment:

### Clone GitHub Project:

```bash
git@github.com:rizzbeen/bank-system-v2.git
cd bank-system-v2
```

### Create a virtual environment and activate it:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / MacOS
source venv/bin/activate
```

### Install development dependencies:

```bash
pip install -r requirements.txt
```

### Run the application:

```bash
python main.py
```

## JSON Data

The user accounts and transactions are stored in:

```bash
data/users.json
```

This JSON file is automatically created when you first run the application.
All transactions are timestamped using the format `DD-MM-YY HH-MM-SS`.

---

## Terminal Interface

The simulator uses `colorama` and `pwinput` to enhance terminal readability:

* Green: Success messages.
* Red: Errors or invalid input.
* Cyan / Blue / Magenta: Menus and labels.
* Emojis: 👤💵💰🏧📜 for intuitive user interface.

---

## Crypto Analytics

The simulator integrates Coinranking API to provide:

* Top 5 coins by market cap.
* Search coins by name with price display.

---

## Screenshots

**Welcome Screen:**

```bash
💰 WELCOME TO BANK SYSTEM v2 💰
====================================
1️⃣  Create New Account
2️⃣  Login to Existing Account
3️⃣  CRYPTO ANALYTICS
4️⃣  Exit
====================================
```

**User Menu After Login:**

```bash
👋 WELCOME BACK, John
🔹 Account ID: 1234
===================================
1️⃣  Check Balance 💵
2️⃣  Deposit Money 💰
3️⃣  Withdraw Money 🏧
4️⃣  Transaction History 📜
5️⃣  USER PROFILE 👤
6️⃣  Logout 🚪
===================================
```

**Transaction History Example:**

```bash
TIME: 25-08-25 12-30-00 | TYPE: DEPOSIT | AMOUNT: 500
TIME: 25-08-25 12-45-00 | TYPE: WITHDRAW | AMOUNT: 200
```

---

## Notes

* Make sure your machine has an active internet connection for Crypto Analytics.
* All user data is persisted in `data/users.json`.
* PIN input is masked for security.

---

## License

This project is for educational purposes. Feel free to modify and expand it.
