print("===== Study Planner =====")
tasks=[]
while True:
    task=input("Enter the study task:")

    if task.lower()=="exit":
        break
    tasks.append(task)
    print("\n your study Task:")
    for i , task in enumerate(tasks,1):
        print(i,task)

        print("Total Tasks:",len(tasks))
