# Name- Harleen Kaur
# Roll no. - 1025230010


# To-Do List Application

def add_task(todo_list):
    #Function to add a new task to the to-do list.
    task = input("Enter the task you want to add: ").strip()
    if task:
        todo_list.append(task)
        print(f"Success: '{task}' was added to your list.")
    else:
        print("Error: Task description cannot be empty.")

def view_tasks(todo_list):
    #Display current tasks in the list along with their indices.
    if not todo_list:
        print("\nYour to-do list is currently empty!")
        return
    
    print("\n--- CURRENT TO-DO LIST ---")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")
    print("-" * 26)

def delete_task(todo_list):
    #Function to delete a task based on its index.
    if not todo_list:
        print("\nThere are no tasks to delete.")
        return
        
    # Show current tasks so the user knows the numbers
    view_tasks(todo_list)
    
    try:
        choice = int(input("Enter the number of the task you want to delete: "))
        # Check if the index is valid (converting 1-based user input to 0-based list index)
        if 1 <= choice <= len(todo_list):
            removed_task = todo_list.pop(choice - 1)
            print(f"Success: '{removed_task}' has been removed.")
        else:
            print("Error: Invalid task number. Please choose a number from the list.")
    except ValueError:
        print("Error: Please enter a valid number.")

# --- Main Program Execution ---
todo_list = []
print("Welcome to the To-Do List Application!")

while True:
    print("\nChoose an option:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ").strip()
    
    if choice == '1':
        add_task(todo_list)
    elif choice == '2':
        view_tasks(todo_list)
    elif choice == '3':
        delete_task(todo_list)
    elif choice == '4':
        print("\nExiting application. Goodbye!")
        break
    else:
        print("Invalid option! Please enter a number between 1 and 4.")