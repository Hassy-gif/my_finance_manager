class Budget:
    def __init__(self):
        self.income = 0
        self.expenses = 0
        self.balance = 0

    def set_income(self, amount):
        self.income = amount

    def add_expense(self, amount):
        self.expenses += amount

    def calculate_balance(self):
        self.balance = self.income - self.expenses

    def get_balance(self):
        return self.balance
