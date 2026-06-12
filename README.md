## 📝Simple Python Expense Tracker

Expense Tracker is a lightweight desktop budgeting app for recording income and expenses, viewing the current balance, and checking totals by category. It stores transactions locally in `expenses.json`, so the app can be used without an account, server, or database setup.

## 🛠️Tech Stack

 - Python - Language used throughout the whole project (picked for ease of programming back-end logic)
 - Tkinter - Library used for the front-end GUI.
 - JSON - Used for the application data storage (locally saved)

## 🚀Features

- Add income and expense transactions with an amount, category, and description.
- View the total balance in a dedicated balance window.
- Review category totals to see where money is coming from or going.
- Compare total income, total expenses, and net balance in one summary view.
- Save transactions locally to `expenses.json` when exiting the app.
- Load saved transactions automatically when the app starts.

## ⚡How to Run

Install Python 3, then run the app from the project folder:

```bash
cd studious-fishstick
python main.py
```

## 👀Preview

The app opens to a simple menu with options to add a transaction, view the balance, view the category summary, or save and exit. Data is kept in the local JSON file so the next launch restores the previous transaction list.