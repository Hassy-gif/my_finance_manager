class Income:
    def __init__(self, source, amount):
        self.source = source
        self.amount = amount

class IncomeManager:
    def __init__(self):
        self.incomes = []

    def add_income(self, income):
        self.incomes.append(income)

    def get_incomes(self):
        return self.incomes
