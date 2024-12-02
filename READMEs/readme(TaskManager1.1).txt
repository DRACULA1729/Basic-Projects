# Task Management System

## Overview
This Python script implements a simple task management system that allows users to add, edit, delete, print, save, and load tasks. Each task consists of a title, description, deadline, and priority level. The tasks are stored in a list and can be serialized to a JSON file for persistent storage.

## Functions

### 1. `add_task(title, description, deadline, priority)`
- **Description**: Adds a new task to the tasks list.
- **Parameters**:
  - `title` (str): The title of the task.
  - `description` (str): A brief description of the task.
  - `deadline` (str): The deadline for the task (format: YYYY-MM-DD).
  - `priority` (int): The priority level of the task (lower numbers indicate higher priority).
- **Returns**: None
- **Prints**: A confirmation message indicating the task has been added.

### 2. `edit_task(title, new_title=None, new_description=None, new_deadline=None, new_priority=None)`
- **Description**: Edits an existing task based on the title provided.
- **Parameters**:
  - `title` (str): The title of the task to be edited.
  - `new_title` (str, optional): The new title for the task.
  - `new_description` (str, optional): The new description for the task.
  - `new_deadline` (str, optional): The new deadline for the task (format: YYYY-MM-DD).
  - `new_priority` (int, optional): The new priority level for the task.
- **Returns**: None
- **Prints**: A confirmation message if the task is found and edited, or an error message if the task is not found.

### 3. `print_tasks()`
- **Description**: Prints all the tasks in the tasks list.
- **Parameters**: None
- **Returns**: None
- **Prints**: Each task's title, description, deadline, and priority. If no tasks are available, it prints a message indicating that.

### 4. `arrange_tasks_by_priority()`
- **Description**: Sorts and prints the tasks based on their priority level.
- **Parameters**: None
- **Returns**: None
- **Prints**: A list of tasks arranged by priority, showing the title and priority level.

### 5. `delete_task(title)`
- **Description**: Deletes a task from the tasks list based on the title provided.
- **Parameters**:
  - `title` (str): The title of the task to be deleted.
- **Returns**: None
- **Prints**: A confirmation message indicating the task has been deleted.

### 6. `save_task(filename)`
- **Description**: Saves the current tasks list to a specified JSON file.
- **Parameters**:
  - `filename` (str): The name of the file to save the tasks.
- **Returns**: None
- **Prints**: A confirmation message indicating the tasks have been saved successfully.

### 7. `load_task(filename)`
- **Description**: Loads tasks from a specified JSON file into the tasks list.
- **Parameters**:
  - `filename` (str): The name of the file to load the tasks from.
- **Returns**: None
- **Prints**: A confirmation message if tasks are loaded successfully, or an error message if the file is not found.

## User Interaction
The script interacts with the user through a series of prompts, allowing them to:
1. Enter the number of tasks to add.
2. Input task details (name, description, deadline, priority).
3. Edit existing tasks.
4. Arrange tasks by priority.
5. Delete tasks.
6. Print the final list of tasks.
7. Save tasks to a file.
8. Load tasks from a file.

## Example Usage
1. The user is prompted to enter the number of tasks.
2. For each task, the user inputs the title, description, deadline, and priority.
3. The user can choose to edit, arrange, delete, print, save, or load tasks as needed.

## Conclusion
This task management system provides a straightforward way to manage tasks through a command-line interface, making it suitable for users looking for a simple yet effective tool for task organization.
