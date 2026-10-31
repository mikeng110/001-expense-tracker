#improvents, use dictionary as data structue
#move into functions 
#add clear for cleaner interface in temrinal
#validate input check that it is correct

#imrpovement, do not overwrite entire json each update

#ability to save 
import os 
import json

expense_items = {}

while True:
    print("--------------------------------")
    print("Welcome To Expense Tracker!")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Show total")
    print("4. Exit")
    print("--------------------------------")

    #load from file 
    with open("expense.json", 'r') as f:
        expense_items = json.load(f)

    #todo validate input
    option = int(input("Choose an option: "))
    print("\n")

    if option == 4:
        break
    elif option == 1:

        description = input("Name of item: ")
        expense = int(input(f"{description} cost in SEK?: "))

        expense_items[description] = expense

        print(f"\nItem added: {description} : {expense} SEK")

        #save to file 

        with open ("expense.json",  'w') as f:
            json.dump(expense_items, f)

    elif option == 2:
        total = 0
        print("--------------------------------")

        for i, (desc,exp) in enumerate(expense_items.items()):
            print(f"{i+1}. {desc} \t\t {exp}")
            total += exp

        print("--------------------------------")
        print(f"Total: \t\t\t {total}")

    elif option == 3:
        total = 0
        for exp in expense_items.values():
            total += exp
        print("--------------------------------")
        print(f"Total: \t\t\t {total}")
        print("--------------------------------")
    






