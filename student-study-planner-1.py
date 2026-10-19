print("===== Study Planner =====")
tasks=[]
while True:
    print("1 Add Tasks")
    print("2. View Tasks")
    print("3.complete Task")
    print("4.Delete Task")
    print("5.View progress")
    print("6.Exit")

    choice=input("Enter choice:")

    if choice =="1":
        name=input("Enter study task:")

        tasks.append({"name":name,"done":False})
        print("Task added!")

    elif choice=="2":
        if not tasks:
            print("No task found!")

            for i,task in enumerate(tasks,1):
                status="completed" if task["done"] else "pending"
                print(i,task["name"],"-",status)

    elif choice=="3":
        try:
            n=int(input("Enter task number to complete:"))
            if 1<=n<= len(tasks):
                tasks[n-1]["done"]=True
                print("Task completed!")
            else:
                print("Invalid task number!")

        except ValueError:
            print("Enter a valid number!")

    elif choice=="4":
        try:
            n=int(input("Enter task number to delete:"))
            if 1<=n<= len(tasks):
                removed=tasks.pop(n-1)
                print("Deleted:",removed["name"])
            else:
                print("Invalid task number!")
        except ValueError:
            print("Enter a valid number!")

    elif choice=="5":
        total=len(tasks)
        completed=sum(task["done"]
for task in tasks)
        pending=total-completed
        print("Total:",total)
        print("Completed:",completed)
        print("pending:",pending)

        if total:
            print("progress:",round(completed/total*100),"%")

    elif choice=="6":
        print("Good luck with your studies!")
        break
    else:
        print("Invalid choice!")