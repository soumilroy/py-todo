"""Todo List Manager: A simple app to add, view, update, and delete tasks. Use JSON or a text file for storage."""


def options_menu():
    print("Welcome to the Todo List Manager!")
    print("---------------------------------")
    print("1. Add a new task")
    print("2. View task(s)")
    print("3. Update task(s)")
    print("4. Delete task(s)")
    print("---------------------------------")
    print("Add any other character to exit...")

available_opts = ["1", "2", "3", "4"]

options_menu()
choice = input("Enter your choice: ")

while choice in available_opts:
    options_menu();
    choice = input("Enter your choice: ")

    if choice in available_opts:    
        if choice == "1":
            print("Adding a new task...")
        elif choice == "2":
            print("Viewing task(s)...")
        elif choice == "3":
            print("Updating task(s)...")
        elif choice == "4":
            print("Deleting task(s)...")
        else:
            print("Exiting...")
            break
    