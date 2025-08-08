print("Welcome to the to-do list manager")

todo_list = []

while True:
    print("\nChoose an option:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1, 2, 3, 4): ")

    if choice == "1":
        task = input("Enter a task: ")
        todo_list.append(task)
        print(f"{task} has been added.")
    elif choice == "2":
        if not todo_list:
            print("your list is empty")
        else :
            print("your to do list ")
            for i, task in enumerate(todo_list,1):
                print(f"{i}.{task}")
    elif choice=="3":
        if not todo_list:
            print("your list is empty")
        else :
            print("your to do list ")
            for i, task in enumerate(todo_list,1):
                print(f"{i}.{task}")
            try:
                task_num= int(input("enter a task number to remove"))
                if 1 <= task_num <= len(todo_list):
                   removed = todo_list.pop(task_num - 1)
                   print(f"'{removed}' has been removed.")
                else:
                     print("Invalid task number.")
            except ValueError:
             print("Please enter a valid number.")
    elif choice=="4":
        print("Good Bye")
        break
         


