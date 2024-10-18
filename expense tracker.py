import json

class ExpenseTracker:
    def __init__(self, filename='expenses.json'):
        self.filename = filename
        self.expenses = self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_expenses(self):
        with open(self.filename, 'w') as file:
            json.dump(self.expenses, file, indent=4)

    def add_expense(self, amount, category, description):
        expense = {
            'amount': amount,
            'category': category,
            'description': description
        }
        self.expenses.append(expense)
        self.save_expenses()

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return
        
        for i, expense in enumerate(self.expenses):
            print(f"{i + 1}. Amount: ${expense['amount']}, Category: {expense['category']}, Description: {expense['description']}")
        
        total = sum(exp['amount'] for exp in self.expenses)
        print(f"\nTotal Expenses: ${total:.2f}")

    def summarize_expenses(self):
        summary = {}
        for expense in self.expenses:
            category = expense['category']
            summary[category] = summary.get(category, 0) + expense['amount']
        
        print("\nExpense Summary by Category:")
        for category, total in summary.items():
            print(f"{category}: ${total:.2f}")

def main():
    tracker = ExpenseTracker()
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Summarize Expenses")
        print("4. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            description = input("Enter description: ")
            tracker.add_expense(amount, category, description)
            print("Expense added.")
        
        elif choice == '2':
            tracker.view_expenses()
        
        elif choice == '3':
            tracker.summarize_expenses()
        
        elif choice == '4':
            print("Exiting the Expense Tracker.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
