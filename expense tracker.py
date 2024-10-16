import csv
from collections import defaultdict

# File where expenses will be saved
FILE_NAME = 'expenses.csv'

# Class for Expense Tracker
class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    # Add an expense to the list
    def add_expense(self, amount, category, description):
        expense = {
            "amount": amount,
            "category": category,
            "description": description
        }
        self.expenses.append(expense)
        print(f"Added expense: {amount} in category '{category}' - {description}")
        self.save_expenses()

    # Display all expenses
    def view_expenses(self):
        if not self.expenses:
            print("No expenses to display.")
        else:
            print("\n--- All Expenses ---")
            for i, expense in enumerate(self.expenses, 1):
                print(f"{i}. {expense['amount']} | {expense['category']} | {expense['description']}")
            print()

    # Show total expenses by category
    def total_expenses_by_category(self):
        if not self.expenses:
            print("No expenses to summarize.")
        else:
            print("\n--- Total Expenses by Category ---")
            category_totals = defaultdict(float)
            for expense in self.expenses:
                category_totals[expense['category']] += float(expense['amount'])

            for category, total in category_totals.items():
                print(f"Category '{category}': Total = {total}")
            print()

    # Save expenses to CSV file
    def save_expenses(self):
        with open(FILE_NAME, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["amount", "category", "description"])
            writer.writeheader()
            writer.writerows(self.expenses)

    # Load expenses from CSV file (if exists)
    def load_expenses(self):
        try:
            with open(FILE_NAME, 'r') as file:
                reader = csv.DictReader(file)
                self.expenses = list(reader)
                print(f"Loaded {len(self.expenses)} expenses from file.")
        except FileNotFoundError:
            print("No saved expenses found.")

# Menu system to interact with the user
def menu():
    tracker = ExpenseTracker()
    tracker.load_expenses()

    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses by Category")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = input("Enter the amount: ")
            category = input("Enter the category (e.g., food, travel, shopping): ")
            description = input("Enter the description: ")
            tracker.add_expense(amount, category, description)

        elif choice == '2':
            tracker.view_expenses()

        elif choice == '3':
            tracker.total_expenses_by_category()

        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

# Run the program
if __name__ == "__main__":
    menu()
