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

def delete_expense(expense_items, option):
    deleted = expense_items.pop(option -1)
    save_expenses(expense_items)
    print(f"Deleted {deleted["Description"]}")

def list_expenses(expense_items):
    print("--------------------------------")

    for i, item in enumerate(expense_items):
        print(f"{i+1}. {item['Description']} \t\t {item['Amount']}")

    print("--------------------------------")

    
def list_total(expense_items):
    print(f"Total: \t\t\t {calculate_total(expense_items)}")


def calculate_total(expense_items):
    return sum(item['Amount'] for item in expense_items)

def add_expense_workflow(expense_items):
    description = input("Name of item: ")
    if description.strip() == "": #blank name
        print("An item require a name")
        return

    try:
        expense = int(input(f"{description} cost in SEK?: "))
    except ValueError:
        print("Invalid input, cost is a positive number\n")
        return

    if expense < 0:
        print("Invalid input, cost is a positive number\n")
        return

    add_expense(expense_items, description, expense)
    save_expenses(expense_items)


def delete_expense_workflow(expense_items):
    if not expense_items:
        print("No items to delete")
        return 
    
    list_expenses(expense_items)
    
    try:
        option = int(input("Select item to delete by number:"))
        if 1 <= option <= len(expense_items):
            delete_expense(expense_items, option)
        else: 
            print("Invalid Option")

    except ValueError:
        print("Invalid Option")


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
            add_expense_workflow(expense_items)
            
        elif option == 2:
            if not expense_items:
                print("no items to be listed")
                continue
            list_expenses(expense_items)
            list_total(expense_items)

        elif option == 3:
            print("--------------------------------")
            list_total(expense_items)
            print("--------------------------------")

        elif option == 4:
            delete_expense_workflow(expense_items)
        

if __name__ == "__main__":
    main()