"""Todo List Manager: A simple app to add, view, update, and delete tasks. Use JSON or a text file for storage."""


tasks = []

def add_new_task():
    print(":::Add new task:::")
    task = input();
    task_object = {
        "id": str(len(tasks) + 1),
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
    print("\n")

def update_task():
    view_tasks();
    task_id = input("Select task id::")
    
    selected_task = next((task for task in tasks if task['id'] == task_id), None)

    if selected_task is None:
        print("\nSeems like you added an invalid task id")
        return;

    print(f"\nYou're editing task {selected_task['id']}")
    print(f"\nUpdate content for {selected_task['id']}")

    new_task = input();

    selected_task['task'] = new_task;
    
    print(f"Updated task {selected_task['id']} to {new_task}")
    view_tasks();

    print("\n")

def options_menu():
    print("Welcome to the Todo List Manager!")
    print("---------------------------------")
    print("1. Add a new task")
    print("2. View task(s)")
    print("3. Update task(s)")
    print("4. Delete task(s)")
    print("---------------------------------")
    print("Add any other character to exit...\n")

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
            update_task();
        elif choice == "4":
            print("Deleting task(s)...")
    else:
        print("Exiting...")
        should_continue = False
    