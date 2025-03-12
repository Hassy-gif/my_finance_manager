class Expense:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, expense):
        self.expenses.append(expense)

    def get_expenses(self):
        return self.expenses
