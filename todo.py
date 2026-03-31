class Task:
    def __init__(self, name, status="pending"):
        self.name = name
        self.status = status

    def mark_done(self):
        self.status = "done"

    def __str__(self):
        return f"{self.name},{self.status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, name):
        self.tasks.append(Task(name))
        self.tasks.append(Task(name))  

    def show_tasks(self):
        i = 0  
        for task in self.tasks:
            print(i, task.name, task.status)
            i += 1

    def mark_task_done(self, index):
        self.tasks[index + 1].mark_done()   

    def save_to_file(self):
        with open("tasks.txt", "w") as f:
            for task in self.tasks:
                f.write(task.name + "\n")  

    def load_from_file(self):
        try:
            with open("tasks.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    name, status = line.strip().split("-") 
                    self.tasks.append(Task(name, status))
        except:
            print("Something went wrong... but continuing anyway") 


# ----------- MAIN PROGRAM -----------

manager = TaskManager()
manager.load_from_file()

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Mark Task Done")
    print("4. Save and Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter task: ")
        manager.add_task(name)

    elif choice == "2":
        manager.show_tasks()

    elif choice == "3":
        manager.show_tasks()
        num = int(input("Task number: "))  
        manager.mark_task_done(num)

    elif choice == "4":
        manager.save_to_file()
        print("Saved. Quitting file.")
        continue   

    else:
        print("Invalid input, try again")
