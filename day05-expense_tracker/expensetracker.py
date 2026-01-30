import os
import json 
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

cat_file = "categories.json"
exp_file = "expense.json"
cat = []
expenses = []

def load_categories():
    global cat
    try:
        if os.path.exists(cat_file):
            with open(cat_file,'r') as cf:
                cat = json.load(cf)
    except(FileNotFoundError, json.JSONdecodeError):
        cat = []

def save_categories():
    with open(cat_file, "w") as cf:
        json.dump(cat, cf, indent=4)

def load_expenses():
  global expenses
  try:
    if os.path.exists(exp_file):
        with open(exp_file,'r') as ef:
            expenses = json.load(ef)
  except(FileNotFoundError, json.JSONDecodeError):
    expenses = []

def save_expenses():
    with open(exp_file,'w') as ef:
        json.dump(expenses,ef,indent = 4)

def add_category():
    new_cat = input("Enter new category name: ").strip()

    if not new_cat:
        print("Category cannot be empty.")
        return

    if new_cat in cat:
        print("Category already exists.")
        return

    cat.append(new_cat)
    save_categories()
    print("Category added successfully.")

def choose_category():
    print("\nAvailable Categories:")
    for i, cat in enumerate(cat, start=1):
        print(f"{i}. {cat}")

    try:
        choice = int(input("Choose category number: "))
        if 1 <= choice <= len(cat):
            return cat[choice - 1]
        else:
            print("Invalid category choice.")
            return None
    except ValueError:
        print("Enter a valid number.")
        return None

def add_expense():
    amount = float(input("Enter amount: "))

    category = choose_category()
    if not category:
        return

    date = input("Enter date (YYYY-MM-DD): ")
    note = input("Note (optional): ")

    expenses.append({
        "amount": amount,
        "category": category,
        "date": date,
        "note": note
    })

    save_expenses()
    print("Expense added successfully.")
    
def view_expenses():
    if not expenses:
        print("no expences.")
        return
    for idx,exp in enumerate(expenses,start = 1):
        print(f"expence {idx}:")
        print(f"\tamount = {exp['amount']}")
        print(f"\t category = {exp['category']}")
        print(f"\tdate = {exp['date']}\n")

def delete_expense():
    if not expenses:
        print("No expenses to delete.")
        return

    view_expenses()

    try:
        choice = int(input("Enter expense number to delete: "))

        if 1 <= choice <= len(expenses):
            removed = expenses.pop(choice - 1)
            save_expenses()
            print("Deleted expense:", removed)
        else:
            print("Invalid number.")

    except ValueError:
        print("Please enter a valid number.")

def daily_total():
    from collections import defaultdict
    daily_expenses = defaultdict(float)

    for exp in expenses:
        daily_expenses[exp['date']] += exp['amount']
    
    for date, total in daily_expenses.items():
        print(f"Total expenses on {date}: {total:.2f}")

def monthly_total():
    from collections import defaultdict

    monthly = defaultdict(int)

    for e in expenses:
        month = e["date"][:7]   
        monthly[month] += e["amount"]

    print("\nMonthly Expense Summary:")
    for month, total in sorted(monthly.items()):
        print(f"{month} → {total}")


def max_spend():
    import numpy as np

    if not expenses:
        print("No expenses recorded.")
        return

    amounts = np.array([e["amount"] for e in expenses])
    print("Maximum expense recorded:", np.max(amounts))


def visuals_expense():
    from collections import defaultdict

    daily = defaultdict(int)
    for e in expenses:
        daily[e["date"]] += e["amount"]

    dates = list(daily.keys())
    totals = list(daily.values())

    plt.bar(dates, totals)
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Daily Expenses")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def category_pie_chart():
    import matplotlib.pyplot as plt
    from collections import defaultdict

    if not expenses:
        print("No expenses to visualize.")
        return

    category_total = defaultdict(float)

    for e in expenses:
        category_total[e["category"]] += e["amount"]

    labels = list(category_total.keys())
    values = list(category_total.values())

    plt.figure()
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Category-wise Expense Distribution")
    plt.axis("equal")
    plt.show()

def view_statistics():
    while True:
        print("**********Expense Statistics**********")
        print("\n1. total daily expenses")
        print("2. total monthly expences")
        print("3. maximum amount spend at once")
        print("4. visuals of expences")
        print("5. visuals of category-vise expenses")
        print("6. exit\n")

        choice = input("enter task number: ")

        if choice == '1':
            daily_total()

        elif choice == '2':
            monthly_total()

        elif choice == '3':
            max_spend()
        
        elif choice == '4':
            visuals_expense()

        elif choice == '5':
            category_pie_chart()

        elif choice == '6':
            print("exiting the expense tracker.")
            break

        else:
            print("enter the valid task number!!!!")

def main():
    load_expenses()
    while True:
        print("**********Expense Tracker**********")
        print("\n1. add_expense")
        print("2. view_expenses")
        print("3. delete_expense")
        print("4. view_statistics")
        print("5. exit\n")

        choice = input("enter task number: ")

        if choice == '1':
            add_expense()

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            delete_expense()
        
        elif choice == '4':
            view_statistics()

        elif choice == '5':
            print("exiting the expense tracker.")
            break

        else:
            print("enter the valid task number!!!!")
    
if __name__ == "__main__":
    main()
