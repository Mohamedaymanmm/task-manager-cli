print("Task Manager!")

tasks = []

def save_tasks():
    with open("tasks.txt", "w") as f:
        for task in tasks:
            line = f"{task['title']}|{task['done']}\n"
            f.write(line)


def  load_tasks():
    global tasks

    try:
        with open("tasks.txt", "r") as f:
            tasks = []
            for line in f:
                line = line.strip()
                title, done = line.split("|")
                tasks.append({
                    "title": title,
                    "done": True if done == "True" else False
                })
    except FileNotFoundError:
        tasks = []

load_tasks()

while True:
    print("(1) Add Task. (2) View Tasks. (3) Mark Task as Done. (4) Delete Task. (5) Exit")
    choice = input("Select the function needed: ")
    if choice in ["1","2","3","4","5"]:
        if choice == "1":
            print("Add task selected: ")
            task = input("Add the task you need: ")
            tasks.append({"title": task, "done": False})
            save_tasks()
            print("Task added successfully!")
        elif choice == "2":
            print("View Tasks selected: ")
            if len(tasks) == 0:
                print("No tasks available.")
            else:
                for i,task in enumerate(tasks, start=1):
                    status = "✔" if task["done"] else "❌"
                    print(f"{i}. {task['title']} {status}")
        elif choice == "3":
            print("Mark Task as Done selected")

            if len(tasks) == 0:
                print("No tasks available.")
            else:
                for i, task in enumerate(tasks, start=1):
                    status = "✔" if task["done"] else "❌"
                    print(f"{i}. {task['title']} {status}")

                try:
                    task_no = int(input("Choose task number: "))
                    index = task_no - 1

                    if index >= 0 and index < len(tasks):
                        tasks[index]["done"] = True
                        print("Task marked as done!")
                        save_tasks()
                    else:
                        print("Invalid task number")
                except ValueError:
                    print("Invalid input")
        elif choice == "4":
            print("Delete Task selected")
            if len(tasks) == 0:
                print("No tasks to delete")
            else:
                for i,task in enumerate(tasks, start=1):
                    status = "✔" if task["done"] else "❌"
                    print(f"{i}. {task['title']} {status}")
                try:
                    task_no = int(input("Enter task number: "))
                    index = task_no - 1
                    if index >= 0 and index < len(tasks):
                        tasks.pop(index)
                        print("Task deleted successfully!")
                        save_tasks()
                except ValueError:
                    print("Invalid input")
                    continue
        elif choice == "5":
            print("You exited")
            break
    else:
        print("Invalid choice")
