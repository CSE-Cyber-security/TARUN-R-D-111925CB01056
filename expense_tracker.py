
import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"


# Create CSV file if it does not exist
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Date", "Category",
                             "Amount", "Description"])


# Add a new expense
def add_expense():
    try:
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("Amount must be greater than zero.")
            return

        category = input("Enter category: ")
        description = input("Enter description: ")
        date = datetime.now().strftime("%Y-%m-%d")

        with open(FILE_NAME, "r", newline="") as file:
            records = list(csv.reader(file))

        expense_id = len(records)

        with open(FILE_NAME, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                expense_id, date, category, amount, description
            ])

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


# View all expenses
def view_expenses():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.reader(file)
        records = list(reader)

    if len(records) <= 1:
        print("No expenses found.")
        return

    print("\nID | Date | Category | Amount | Description")
    print("-" * 65)

    for row in records[1:]:
        print(" | ".join(row))


# Calculate daily expenses
def daily_summary():
    today = datetime.now().strftime("%Y-%m-%d")
    total = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Date"] == today:
                total += float(row["Amount"])

    print(f"\nToday's Expenses: ₹{total:.2f}")


# Calculate monthly expenses
def monthly_summary():
    month = datetime.now().strftime("%Y-%m")
    total = 0

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["Date"].startswith(month):
                total += float(row["Amount"])

    print(f"\nThis Month's Expenses: ₹{total:.2f}")


# Category-wise summary
def category_summary():
    categories = {}

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            category = row["Category"]
            amount = float(row["Amount"])

            categories[category] = (
                categories.get(category, 0) + amount
            )

    print("\nCategory-wise Expenses:")

    if not categories:
        print("No expenses found.")
        return

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


# Delete an expense
def delete_expense():
    expense_id = input("Enter Expense ID to delete: ")
    
    with open(FILE_NAME, "r", newline="") as file:
        records = list(csv.reader(file))

    updated_records = [
        records[0]
    ]

    found = False

    for row in records[1:]:
        if row[0] == expense_id:
            found = True
        else:
            updated_records.append(row)

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(updated_records)

        print("Expense deleted successfully!")
    else:
        print("Expense ID not found.")


# Main menu
def main():
    initialize_file()

    while True:
        print("\n===== DAILY EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Daily Summary")
        print("4. Monthly Summary")
        print("5. Category Summary")
        print("6. Delete Expense")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            daily_summary()
        elif choice == "4":
            monthly_summary()
        elif choice == "5":
            category_summary()
        elif choice == "6":
            delete_expense()
        elif choice == "7":
            print("Thank you for using Expense Tracker!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
