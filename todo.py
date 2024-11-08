tasks = []

def add_task():
    task = input("Please enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the list.")



def list_tasks():
    if not tasks:
        print("There are no tasks currently, good job for being up to date!")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task #{index}. {task}")    


def delete_task():
    list_tasks()
    try:
        taskToDel = int(input("Enter the # to delete: "))
        if taskToDel >= 0 and taskToDel < len(tasks):
            tasks.pop(taskToDel)
            print(f"Task {taskToDel} has been removed. ")
        else:
            print(f"Task #{taskToDel} was not found.")
    except:
        print("Invalid input.")            

if __name__ == "__main__":
    # create a loop for running the prgoram #
    print("Welcome to the To-Do list")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if (choice == "1"):
            add_task()
        elif (choice == "2"):
            delete_task()
        elif (choice == "3"):
            list_tasks()
        elif (choice == "4"):
            break
        else:
            print("Invalid input. Please try again.")
    print("Goodbye!")        