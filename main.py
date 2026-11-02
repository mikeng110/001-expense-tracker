import os 
import json

#list of dictionary instead, how does that affect file?
expense_items = {}

#takes dict format where identical keys store a list instead of number
#convert dict into a list of dictionary
#given key_str, val_str the name of dictionary keys
def list_to_dict(l, key_str, val_str):
    d = {}
    for item in l:
        key = item[key_str]
        val = item[val_str]

        if key in d:
            if not isinstance(d[key], list):
                d[key] = [d[key]]
            
            d[key].append(val)
        else:
            d[key] = val
     
    return d

def dict_to_list(d, key_str, val_str):
    l = []
    for key, val in d.items():
        if isinstance(val, list):
            for v in val:
                l.append({key_str:key, val_str:v})
        else:
            l.append({key_str:key, val_str:val})

    return l



def load_expenses():
    if os.path.exists("expense.json"):
        with open("expense.json", 'r') as f:
            expense_items = json.load(f)
    else:
        expense_items = {}

    return expense_items


def save_expenses(expense_items):
    with open ("expense.json",  'w') as f:
        json.dump(expense_items, f)

def add_expense(expense_items, desc, exp):
    expense_items[desc] = exp
    print(f"\nItem added: {desc} : {exp} SEK")

def list_expenses(expense_items):
    print("--------------------------------")

    for i, (desc,exp) in enumerate(expense_items.items()):
        print(f"{i+1}. {desc} \t\t {exp}")

    print("--------------------------------")
    print(f"Total: \t\t\t {calculate_total(expense_items)}")


def calculate_total(expense_items):
    return sum(expense_items.values())

def main():
    expense_items = load_expenses()

    #testing conversion out
    l = [
    {"description": "Lunch", "amount": 120},
    {"description": "Groceries", "amount": 450},
    {"description": "Lunch", "amount": 150}
    ]

    d = list_to_dict(l, "description", "amount")

    l2 = dict_to_list(d, "description", "amount" )

    #l = dict_to_list(expense_items, "")


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

            add_expense(expense_items, description, expense)

            save_expenses(expense_items)
        elif option == 2:
            list_expenses(expense_items)

        elif option == 3:
            print("--------------------------------")
            print(f"Total: \t\t\t {calculate_total(expense_items)}")
            print("--------------------------------")

        else:
            print("Invalid option")
        

if __name__ == "__main__":
    main()