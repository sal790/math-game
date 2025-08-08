print("Welcome to the do-list manager")

todo_list=[]

while True:
    print("\n choose an option:")
    print("1.Add a task")
    print("2.View task")
    print("3.Remove task")
    print("4.Exit")
     choice= input(" Enter your choice (1,2,3,4)")


     if choice == "1":
         task=input("enter a task")
         todo_list.append(task)
         print(f"{task} has been added")

