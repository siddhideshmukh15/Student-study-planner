
tasks = []

while True:
    print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter study task: ")
        tasks.append({"name": name, "done": False})
        print("Task added!")

    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            status = "Done" if task["done"] else "Pending"
            print(i, task["name"], "-", status)

    elif choice == "3":
        try:
            n = int(input("Enter task number: "))
            if 1 <= n <= len(tasks):
                tasks[n - 1]["done"] = True
                print("Task completed!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Enter a valid number!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")

