import json
tasks = []

def add_task(title, description, deadline, priority):
    task = {'title': title, 'description': description, 'deadline': deadline, 'priority': priority}
    tasks.append(task)
    print(f"Task '{title}' added successfully")

def edit_task(title, new_title=None, new_description=None, new_deadline=None, new_priority=None):
    for task in tasks:
        if task['title'] == title:
            if new_title:
                task['title'] = new_title
            if new_description:
                task['description'] = new_description
            if new_deadline:
                task['deadline'] = new_deadline
            if new_priority:
                task['priority'] = new_priority
            print(f"Task '{title}' edited successfully")
            return
    print(f"Task '{title}' not found")

def print_tasks():
    if not tasks:
        print("No tasks available.")
        return
    for task in tasks:
        print(f"Title: {task['title']}, Description: {task['description']}, Deadline: {task['deadline']}, Priority: {task['priority']}")

def arrange_tasks_by_priority():
    sorted_tasks = sorted(tasks, key=lambda x: x['priority'])
    print("Tasks arranged by priority:")
    for task in sorted_tasks:
        print(f"Title: {task['title']}, Priority: {task['priority']}")

def delete_task(title):
    global tasks
    tasks = [task for task in tasks if task['title'] != title]
    print(f"Task '{title}' deleted successfully")

def save_task(filename):
    with open(filename, 'w') as f:
        json.dump(tasks, f, indent=2)
    print(f"Tasks saved successfully to {filename}")

def load_task(filename):
    global tasks
    try:
        with open(filename, 'r') as f:
            tasks = json.load(f)
        print(f"Tasks loaded successfully from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    



n=int(input("Enter the number of tasks for now:"))
for i in range(n):
    name=input("Enter the name of task: ")
    description=input("Enter its description:")
    deadline=input("Enter deadline:")
    priority=int(input("Enter priority level:"))
    add_task(name,description,deadline,priority)

choice=input("Do you want to edit any task(y/n)? ").lower()
if choice=='y':
    name=input("Enter the name of task to edit: ")
    edit_task(name,input("Enter new name(Hit ENTER for no edits in this field): "),input("Enter new description (Hit ENTER for no edits in this field): "),input("deadline in YYYY-MM-DD format (Hit ENTER for no edits in this field): "),int(input("Enter new priority level (Hit ENTER for no edits in this field): ")))
    
choice=input("Do you want to arrange tasks by priority(y/n)? ").lower()
if choice=='y':
    arrange_tasks_by_priority()
choice=input("Do you want to delete any task(y/n)? ").lower()
if choice=='y':
        name=input("Enter the name of task to delete: ")
        delete_task(name)

choice=input("Wanna print the final list(y/n):").lower()
if choice=='y':
    print_tasks()

choice=input("Do you want to save the tasks(y/n)? ").lower()

if choice=='y':
    filename=input("Enter the name of file to save tasks: ")
    save_task(filename)
elif choice=='n':
    print("Tasks not saved.")
else:
    print("Invalid choice.")

choice=input("Do you want to load tasks from a file(y/n)? ").lower()

if choice=='y':
    filename=input("Enter the name of file to load tasks: ")
    load_task(filename)
else:
    print("Tasks not loaded.")
    
    
print("THANK YOU FOR USING IT! \n HOPE YOU HAVE A GREAT DAY \n B BYE \n YEETS!")
