#improvents, use dictionary as data structue
#move into functions 
#add clear for cleaner interface in temrinal
#validate input check that it is correct

expense_items = {}

while True:
    print("--------------------------------")
    print("Welcome To Expense Tracker!")
    print("1. Add expense")
    print("2. List expenses")
    print("3. Show total")
    print("4. Exit")
    print("--------------------------------")

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
        

    print("\n")

    






