# todo_app.py
import os

TODO_FILE = "todo_list.txt"

def load_tasks():
    """Load tasks from the file, or return an empty list if file doesn't exist."""
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return [line.strip() for line in file]

def save_tasks(tasks):
    """Save the list of tasks to the file."""
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            file.write(task + "\n")

def add_task(task):
    """Add a new task to the list."""
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{task}' added.")

def view_tasks():
    """Display all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(task_number):
    """Delete a task by its number in the list."""
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' deleted.")
    else:
        print("Invalid task number.")

def main():
    """Main function to run the to-do list app."""
    while True:
        print("\nOptions: ")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            task = input("Enter the task: ").strip()
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter the task number to delete: ").strip())
                delete_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
