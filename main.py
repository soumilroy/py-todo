"""Todo List Manager: A simple app to add, view, update, and delete tasks. Use JSON or a text file for storage."""

import uuid

tasks = []

def add_new_task():
    print(":::Add new task:::")
    task = input();
    task_object = {
        "id": str(uuid.uuid4())[0:8],
        "task": task
    }
    tasks.append(task_object)
    print(f"Added: {task}")
    print(f"Tasks: {tasks}")
    print("\n\n")

def view_tasks():
    print(":::View tasks:::")
    if len(tasks) == 0:
        print("No tasks found")
    else:
        for task in tasks:
            print(f"ID: {task['id']} - Task: {task['task']}")
    print("\n\n")

def options_menu():
    print("Welcome to the Todo List Manager!")
    print("---------------------------------")
    print("1. Add a new task")
    print("2. View task(s)")
    print("3. Update task(s)")
    print("4. Delete task(s)")
    print("---------------------------------")
    print("Add any other character to exit...\n\n")

available_opts = ["1", "2", "3", "4"]
should_continue = True

while should_continue:
    options_menu();
    choice = input("Enter your choice: ")

    if choice in available_opts:    
        if choice == "1":
            add_new_task()
        elif choice == "2":
            view_tasks();
        elif choice == "3":
            print("Updating task(s)...")
        elif choice == "4":
            print("Deleting task(s)...")
    else:
        print("Exiting...")
        should_continue = False
    