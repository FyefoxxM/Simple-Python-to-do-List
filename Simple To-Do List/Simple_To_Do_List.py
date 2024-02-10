# Define an empty list to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print("Task added successfully!")

# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print("Task removed successfully!")
    else:
        print("Task not found.")

# Function to display all tasks in the list
def display_tasks():
    if tasks:
        print("Your to-do list:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("Your to-do list is empty.")

# Function to take user input for adding a task
def get_task_from_user():
    return input("Enter the task: ")

# Function to take user input for removing a task
def get_task_to_remove():
    return input("Enter the task to remove: ")

# Function to take user input for displaying tasks
def get_display_choice():
    return input("Enter 'A' to add a task, 'R' to remove a task, or 'D' to display tasks: ").upper()

# Main function to manage user input and update tasks accordingly
def main():
    while True:
        choice = get_display_choice()
        if choice == 'A':
            task = get_task_from_user()
            add_task(task)
        elif choice == 'R':
            task = get_task_to_remove()
            remove_task(task)
        elif choice == 'D':
            display_tasks()
        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()


