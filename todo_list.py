# todo_list.py

import json
import os

# Define the path to the file where tasks will be stored
FILE_PATH = 'todo_list.json'

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, task):
    """Add a new task to the list."""
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task added: {task}')

def remove_task(tasks, task_index):
    """Remove a task from the list by index."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f'Task removed: {removed_task}')
    else:
        print('Invalid task index.')

def view_tasks(tasks):
    """View all tasks."""
    if not tasks:
        print('No tasks to show.')
    else:
        for index, task in enumerate(tasks):
            print(f'{index}: {task}')

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            task = input("Enter the task to add: ")
            add_task(tasks, task)
        elif choice == '3':
            view_tasks(tasks)
            task_index = int(input("Enter the index of the task to remove: "))
            remove_task(tasks, task_index)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
