# Define the to-do list
todo_list = []

def add_task(task):
    todo_list.append({"task": task, "completed": False})
    print(f"Added task: '{task}'")

def view_tasks():
    if not todo_list:
        print("No tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(todo_list, 1):
            status = "Completed" if task["completed"] else "Pending"
            print(f"{idx}. {task['task']} [{status}]")

def mark_task_completed(task_number):
    if 0 < task_number <= len(todo_list):
        todo_list[task_number - 1]["completed"] = True
        print(f"Marked task {task_number} as completed.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Deleted task: '{removed_task['task']}'")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Mark a task as completed")
        print("4. Delete a task")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            view_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            mark_task_completed(task_number)
        elif choice == "4":
            view_tasks()
            task_number = int(input("Enter the task number to delete: "))
            delete_task(task_number)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
