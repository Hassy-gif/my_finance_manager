from finance_manager.budget import Budget
from finance_manager.expenses import Expense, ExpenseManager
from finance_manager.income import Income, IncomeManager

class FinanceManager:
    def __init__(self):
        self.budget = Budget()
        self.expense_manager = ExpenseManager()
        self.income_manager = IncomeManager()

    def set_budget(self):
        income = float(input("Enter your monthly income: "))
        self.budget.set_income(income)

    def add_expense(self):
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        expense = Expense(name, amount)
        self.expense_manager.add_expense(expense)
        self.budget.add_expense(amount)

    def add_income(self):
        source = input("Enter income source: ")
        amount = float(input("Enter income amount: "))
        income = Income(source, amount)
        self.income_manager.add_income(income)

    def calculate_balance(self):
        self.budget.calculate_balance()


    def display_summary(self):
        print("*****Budget Summary*****")
        print(f"Income: {self.budget.income}")
        print(f"Expenses: {self.budget.expenses}")
        print(f"Balance: {self.budget.get_balance()}")
        print("Expenses:")
        for expense in self.expense_manager.get_expenses():
            print(f"{expense.name}: {expense.amount}")
        print("Incomes:")
        for income in self.income_manager.get_incomes():
            print(f"{income.source}: {income.amount}")

def main():
    finance_manager = FinanceManager()
    while True:
        print("1. Set Budget")
        print("2. Add Expense")
        print("3. Add Income")
        print("4. Calculate Balance")
        print("5. Display Summary")
        print("6. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            finance_manager.set_budget()
        elif choice == "2":
            finance_manager.add_expense()
        elif choice == "3":
            finance_manager.add_income()
        elif choice == "4":
            finance_manager.calculate_balance()
        elif choice == "5":
            finance_manager.display_summary()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()