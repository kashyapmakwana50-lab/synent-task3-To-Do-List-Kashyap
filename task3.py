tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n===== YOUR TASKS =====")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
