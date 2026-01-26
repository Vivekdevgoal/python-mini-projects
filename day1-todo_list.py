import os

task_file = 'task.txt'
tasks = []

def load_task():
    if os.path.exists(task_file):
        with open(task_file,'r') as tf:
            for line in tf:
                tasks.append(line.strip())

def save_task():
    with open(task_file, 'w') as wf:
        for task in tasks:
            wf.write(task + '\n')

def view_task():
    if not tasks:
        print("no tasks available.")
        return 

    print("\nyour tasks: ")
    for i, task in enumerate(tasks,start = 1):
        print(f"{i} -> {task}")

def add_task():
    task = input("enter the task to add: ")
    tasks.append(task)
    save_task()
    print('task added successfully.')

def delete_task():
    view_task()
    if not tasks:
        return
    
    try:
        task_no = int(input("enter the task number to delete:"))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            save_task()
            print("task removed: ", removed)
        else:
            print("invalid task number")
    except ValueError:
        print("enter valid value")

def main():
    load_task()
    while True:
        print("\nTodo list menu:")
        print("1. View tasks")
        print("2. Add tasks")
        print("3. Delete tasks")
        print("4. exit")

        choice = input("enter the task number to perform from menu: ")
        if choice == "1":
            view_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task() 
        elif choice == "4":
            print("@@exiting to-do list@@")
            break   
        else:
            print("enter the valid value? wtf are you doint can't see menu !!!")
if __name__ == "__main__":
    main()

