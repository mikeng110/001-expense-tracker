import os 
import json

expense_items = {}

def load_expenses():
    global expense_items
    if os.path.exists("expense.json"):
        with open("expense.json", 'r') as f:
            expense_items = json.load(f)
    else:
        expense_items = {}


def save_expenses():
    with open ("expense.json",  'w') as f:
        json.dump(expense_items, f)

def add_expense(desc, exp):
    expense_items[desc] = exp
    print(f"\nItem added: {desc} : {exp} SEK")

def list_expenses():
    print("--------------------------------")

    for i, (desc,exp) in enumerate(expense_items.items()):
        print(f"{i+1}. {desc} \t\t {exp}")

    print("--------------------------------")
    print(f"Total: \t\t\t {calculate_total()}")


def calculate_total():
    return sum(expense_items.values())

def main():
    load_expenses()

    while True:
        print("--------------------------------")
        print("Welcome To Expense Tracker!")
        print("1. Add expense")
        print("2. List expenses")
        print("3. Show total")
        print("4. Exit")
        print("--------------------------------")

        try:
            option = int(input("Choose an option:"))
        except ValueError:
            option = 0

        print("\n")

        if option == 4: #Exit
            break
        elif option == 1: 

            description = input("Name of item: ")
            expense = int(input(f"{description} cost in SEK?: "))

            add_expense(description, expense)

            save_expenses()
        elif option == 2:
            list_expenses()

        elif option == 3:
            print("--------------------------------")
            print(f"Total: \t\t\t {calculate_total()}")
            print("--------------------------------")

        else:
            print("Invalid option")
        

if __name__ == "__main__":
    main()