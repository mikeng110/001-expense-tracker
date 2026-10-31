
#what datastructure to use? Start simple 
#for now assume they are always in sync
descriptions  = []
expenses = []

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

        descriptions.append(description)
        expenses.append(expense)

        print(f"\nItem added: {description} : {expense} SEK")

    elif option == 2:
        total = 0
        print("--------------------------------")
        for i, desc in enumerate(descriptions):
            print(f"{i+1}. {desc} \t\t {expenses[i]}")
            total += expenses[i]
        print("--------------------------------")
        print(f"Total: \t\t\t {total}")

    elif option == 3:
        total = 0
        for expense in expenses:
            total += expense

        print("--------------------------------")
        print(f"Total: \t\t\t {total}")
        print("--------------------------------")
        

    print("\n")

    






