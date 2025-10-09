# Function to display the main menu
def display_menu():
    """Prints the main menu options to the console."""
    print("\n" + "="*30)
    print("      📝 TO-DO LIST APP 📝      ")
    print("="*30)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")
    print("-" * 30)

# Function to view all tasks
def view_tasks(todo_list):
    """Displays all tasks in the list, showing their index and status."""
    if not todo_list:
        print("\n🎉 Your to-do list is empty! 🎉")
        return

    print("\n📋 Current To-Do List 📋")
    print("-" * 30)
    # Enumerate helps get the index (i) and the item (task_dict)
    for i, task_dict in enumerate(todo_list):
        # Determine the status display based on the 'completed' key
        status = "✅" if task_dict['completed'] else "⏳"
        # Print format: [Index]. [Status] Task Description
        print(f"{i + 1}. {status} {task_dict['task']}")
    print("-" * 30)

# Function to add a new task
def add_task(todo_list):
    """Prompts the user for a task and adds it to the list."""
    task_name = input("Enter the new task: ").strip()
    if task_name:
        # Each task is a dictionary with the task description and a completion status
        new_task = {'task': task_name, 'completed': False}
        todo_list.append(new_task)
        print(f"\nTask '{task_name}' added successfully!")
    else:
        print("\nTask cannot be empty. Please try again.")

# Function to mark a task as complete
def mark_complete(todo_list):
    """Prompts the user for a task index and marks it as complete."""
    view_tasks(todo_list)
    if not todo_list:
        return

    try:
        # Get the task number from the user (1-based index)
        task_num = int(input("Enter the number of the task to mark as COMPLETE: "))
        # Convert to 0-based index
        task_index = task_num - 1

        if 0 <= task_index < len(todo_list):
            # Update the 'completed' status
            if todo_list[task_index]['completed']:
                print(f"\nTask '{todo_list[task_index]['task']}' is already complete. ✅")
            else:
                todo_list[task_index]['completed'] = True
                print(f"\nTask '{todo_list[task_index]['task']}' marked as complete! 🎉")
        else:
            print("\nInvalid task number. Please enter a number from the list.")

    except ValueError:
        print("\nInvalid input. Please enter a number.")

# Function to delete a task
def delete_task(todo_list):
    """Prompts the user for a task index and deletes it from the list."""
    view_tasks(todo_list)
    if not todo_list:
        return

    try:
        # Get the task number from the user (1-based index)
        task_num = int(input("Enter the number of the task to DELETE: "))
        # Convert to 0-based index
        task_index = task_num - 1

        if 0 <= task_index < len(todo_list):
            # Remove the task and store its name for the confirmation message
            deleted_task = todo_list.pop(task_index)['task']
            print(f"\nTask '{deleted_task}' deleted successfully! 🗑️")
        else:
            print("\nInvalid task number. Please enter a number from the list.")

    except ValueError:
        print("\nInvalid input. Please enter a number.")


# Main application loop
def main():
    """The entry point of the application, running the main loop."""
    # Initialize the list to store the tasks
    todo_list = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task(todo_list)
        elif choice == '2':
            view_tasks(todo_list)
        elif choice == '3':
            mark_complete(todo_list)
        elif choice == '4':
            delete_task(todo_list)
        elif choice == '5':
            print("\n👋 Exiting To-Do List Application. Have a productive day! 👋")
            break  # Exit the while loop
        else:
            print("\n⚠️ Invalid choice. Please select a number between 1 and 5.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()