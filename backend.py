import json
import os

class Transaction:
    def __init__(self, amount: float, category: str, description: str):
        self.amount = amount
        self.category = category
        self.description = description

class ExpenseTracker:
    def __init__(self):
        self.transactions = []

        # always point to the JSON file in the same folder as backend.py
        self.filepath = os.path.join(os.path.dirname(__file__), "expenses.json")

    def get_filepath(self, filename="expenses.json"):
        if filename == "expenses.json":
            return self.filepath
        return os.path.join(os.path.dirname(__file__), filename)

    def add_transaction(self, transaction: Transaction):
        self.transactions.append(transaction)

    def obj_to_dict(self):
        new_list = []
        for t in self.transactions:
            transaction_dict = {}
            
            transaction_dict["amount"] = t.amount
            transaction_dict["category"] = t.category
            transaction_dict["description"] = t.description
            
            new_list.append(transaction_dict)
        return new_list

    def total_balance(self):
        return sum(t.amount for t in self.transactions)

    def total_income(self):
        return sum(t.amount for t in self.transactions if t.amount > 0)

    def total_expenses(self):
        return sum(t.amount for t in self.transactions if t.amount < 0)

    def category_summary(self):
        summary_dict = {}
        for t in self.transactions:
            if t.category not in summary_dict:
                summary_dict[t.category] = 0

            summary_dict[t.category] += t.amount
        return summary_dict

    def load_from_file(self, filename="expenses.json"):
        filepath = self.get_filepath(filename)
        try:
            with open(filepath, "r") as f:
                stored_list = json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            stored_list = []

        self.transactions = []
        for d in stored_list:
            new_transaction = Transaction(float(d["amount"]), d["category"], d["description"])
            self.transactions.append(new_transaction)

    def save_to_file(self, filename="expenses.json"):
        filepath = self.get_filepath(filename)
        list_to_save = self.obj_to_dict()
        with open(filepath, "w") as f:
            json.dump(list_to_save, f, indent=4)
