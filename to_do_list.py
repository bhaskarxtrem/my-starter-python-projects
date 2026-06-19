tasks = []

#FUNCTION FOR SHOWING TASKS
def show_tasks():
    for i in range(1,len(tasks)+1):
        if tasks[i-1]["done"]:
            status = "DONE"
        else:
            status = "NOT DONE"
        print(f"{i}. {tasks[i-1]['name']} — {status}")


#FUNCTION FOR ADDING TASKS
def add_tasks():
    while True:
        addtasks = input("Enter the tasks you wanna add or say 'done' : ")

        if addtasks == "done":
            print("—"*10,"TASK ADDED!","—"*10)
            print("CHOOSE YOUR OPERATION YOU WANNA DO AGAIN...")
            break
        else:
            tasks.append({"name" : addtasks , "done" : False })


#FUNCTIONS FOR REMOVING TASKS		
def remove_tasks():
    if tasks:
        print("\nCHOSE THE TASK NUMBER YOU WANNA REMOVE")
        show_tasks()
        while True:
            try:
                remove = int(input(f"\nSelect the task to remove in these 1 to {len(tasks)}: "))
                if 1 <= remove <= len(tasks):
                    tasks.pop(remove-1)
                    print("—"*10,"TASK DELETED","—"*10)
                    input("Enter to continue")
                    print("CHOOSE THE OPERATION YOU WANNA DO AGAIN...")
                    break
            except:
                print("Chose only task number...")
    else:
        print("NO TASKS ADDED YET...")
        input("Enter to continue")
        print("CHOOSE THE OPERATION YOU WANNA DO")
        
def view_tasks():
    if tasks:
        print("\nHERE IS ALL YOUR TASKS...")
        show_tasks()
        input("Enter to continue")
        print("CHOSE THE OPERATION YOU WANNA DO AGAIN...")
    else:
        print("No tasks added yet...")
        input("Enter to continue")
        print("CHOOSE THE OPERATION YOU WANNA DO AGAIN...")

        
#FUNCTION FOR MARKING TASKS        
def mark_tasks():
    if tasks:
        print("\nCHOSE THE TASK NUMBER YOU WANNA MARK AS DONE ")
        show_tasks()
        while True:
            try:
                mark = int(input("ENTER THE TASK NUMBER YOU WANNA MARK AS DONE:"))
                if 1 <= mark <= len(tasks):
                    break
                else:
                    print("Enter valid task number...")
                    continue
            except:
                print("Only type number...")
        
        if 1 <= mark <= len(tasks):
            if tasks[mark-1]["done"] == False:
                tasks[mark-1]["done"] = True
            else:
                tasks[mark-1]["done"] = False
            
            if tasks[mark-1]["done"] == True:
                print("—"*10,f"TASK {mark} IS MARKED AS DONE","—"*10)
            else:
                print("—"*10,f"TASK {mark} IS MARKED AS NOT DONE","—"*10)
            input("Enter to continue...")
            print("CHOOSE THE OPERATION YOU WANNA DO AGAIN...")
        
        else:
            print("Enter valid task number")
    else:
        print("No tasks added yet...")
        input("Enter to continue...")
        print("CHOSE THE OPERATION YOU WANNA DO...")

	    
#FUNCTION FOR EDITING TASKS	    
def edit_tasks():
    if tasks:
        print("\nHERE ARE ALL OF YOUR TASKS: ") 
        show_tasks()
        while True:
            try:
                edit = int(input("ENTER THE TASK NUMBER YOU WANNA EDIT: "))
                if 1 <= edit <= len(tasks):
                    break
                else:
                    print("Enter valid task number...")
            except:
                print("Type only number...")
        new_name = input("ENTER THE NEW TASK NAME YOU WANNA EDIT: ")
        tasks[edit-1]['name'] = new_name
        print("—"*10, f"TASK {edit} EDITED","—"*10)
        input("Enter to continue...")
        print("\n CHOOSE THE OPERATION YOU WANNA DO AGAIN: ")
    else:
        print("No tasks added yet...")
        input("Enter to continue...")

 
#FUNCTION TO SEE PROGRESS 
def progress():
    count = 0
    if tasks:
        print("HERE IS YOUR PROGRESS: ")
        print(f"Total tasks: {len(tasks)}")
        
        for task in tasks:
            if task["done"] == True:
                count += 1
        
        print(f"Completed tasks: {count}")
        print(f"Remaining tasks: {len(tasks) - count}")
        input("\nEnter to continue")
    else:
        print("No tasks added yet...")
        input("Enter to continue...")	


#FUNCTION FOR SEARCH BAR
def search():
    
    if tasks:
        keyword = input("Enter keyword to search task: ").lower()
        found = False
        
        for index, task in enumerate(tasks, start = 1):
            if task["done"]:
                status = "DONE"
            else:
                status = "NOT DONE"
            
            task_name = task["name"].lower()
            if keyword in task_name:
                print(f"{index}. {task['name']} — {status}")
                found = True
            
        if not found:
            print("No match found...")
    else:
        print("No tasks added yet...")
        input("Enter to continue...")
    
    input("Enter to continue...")
    print("ENTER THE OPERATION YOU WANNA DO AGAIN: ")


#LOADING AND ARANGING FILE IN LIST		
try:
    with open("app.txt","r") as file:
        for line in file:
            line = line.strip()
            parts = line.split("—")
            name = parts[0].strip()
            done = parts[1].strip()
            if done == "True":
                done = True
            else:
                done = False
            tasks.append({"name" : name, "done" : done})
except:
    pass

print("—"*30)
print(" "*9,"TO DO LIST"," "*9)
print("—"*30)


#MENU BAR
while True:
    print("1. Add tasks")
    print("2. Search tasks")
    print("3. Remove tasks")
    print("4. View tasks")
    print("5. Mark if it's done")
    print("6. Edit tasks")
    print("7. Show progress")
    print("8. Exit")

    choice = input("\n——> WHAT OPERATION YOU WANNA DO?: ")

    if choice == "1":
        add_tasks()
    if choice == "2":
        search()
    if choice == "3":
        remove_tasks()
    if choice == "4":
        view_tasks()
    if choice == "5":
        mark_tasks()
    if choice == "6":
        edit_tasks()
    if choice == "7":
        progress()
    if choice == "8":
        with open("app.txt","w") as file:
            for task in tasks:
                file.write(f"{task['name']} — {task['done']} \n")		
        print("—"*50)
        print(" "*9,"THANKYOU FOR USING MY PROGRAM"," "*9)
        print("—"*50)
        break