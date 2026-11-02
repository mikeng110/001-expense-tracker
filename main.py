import os 
import json

def load_expenses():
    if os.path.exists("expense.json"):
        with open("expense.json", 'r') as f:
            expense_items = json.load(f)
    else:
        expense_items = []

    return expense_items

def save_expenses(expense_items):
    with open ("expense.json",  'w') as f:
        json.dump(expense_items, f)

def add_expense(expense_items, desc, exp):
    expense_items.append({"Description": desc , "Amount": exp})
    print(f"\nItem added: {desc} : {exp} SEK")

def list_expenses(expense_items):
    print("--------------------------------")

    for i, item in enumerate(expense_items):
        print(f"{i+1}. {item['Description']} \t\t {item['Amount']}")

    print("--------------------------------")
    print(f"Total: \t\t\t {calculate_total(expense_items)}")


def calculate_total(expense_items):
    return sum(item['Amount'] for item in expense_items)

def main():
    expense_items = load_expenses()

    while True:
        print("--------------------------------")
        print("Welcome To Expense Tracker!")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Show total")
        print("4. Delete expense")
        print("5. Exit")
        print("--------------------------------")

        try:
            option = int(input("Choose an option:"))
        except ValueError:
            option = 0

        print("\n")

        if option == 5: #Exit
            break
        elif option == 1: 
            description = input("Name of item: ")

            if description.strip() == "": #blank name
                print("An item require a name")
                continue

            try:
                expense = int(input(f"{description} cost in SEK?: "))
            except ValueError:
                print("Invalid input, cost is a positive number\n")
                continue

            if expense < 0:
                print("Invalid input, cost is a positive number\n")
                continue

            add_expense(expense_items, description, expense)

            save_expenses(expense_items)
        elif option == 2:
            if not expense_items:
                print("no items to be listed")
                continue
            list_expenses(expense_items)

        elif option == 3:
            print("--------------------------------")
            print(f"Total: \t\t\t {calculate_total(expense_items)}")
            print("--------------------------------")

        elif option == 4:

            if not expense_items:
                print("no items to be deleted")
                continue
            list_expenses(expense_items)
            try:
                option = int(input("Select item to delete: "))

            except ValueError:
                print("Invalid input, expected integer")
                continue
            if option > 0 and option <= len(expense_items):
                deleted = expense_items.pop(option -1)
                save_expenses(expense_items)
                print(f"Deleted {deleted["Description"]}")
            else:
                print("Invalid Selection")

        else:
            print("Invalid option")
        

if __name__ == "__main__":
    main()