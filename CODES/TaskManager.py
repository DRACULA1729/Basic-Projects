'''
Create a list -Store a list of tasks
create functions for adding tasks(title, description,deadline and priority, print title of tasks and say task added sucessfully), editing tasks, give priority to each part.
create a function to print, arrange tasks according to priority as output.
create a function for deleting tasks.
'''
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
print("THANK YOU FOR USING IT! \n HOPE YOU HAVE A GREAT DAY \n B BYE \n YEETS!")
