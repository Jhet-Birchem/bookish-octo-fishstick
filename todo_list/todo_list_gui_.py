import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.realpath(__file__))

# Define the file path in the same directory as the script
TODO_FILE = os.path.join(script_dir, "todo_list.json")

# Load tasks from the file
def load_tasks():
    try:
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to the file
def save_tasks():
    with open(TODO_FILE, "w") as file:
        json.dump(todo_list, file, indent=4)

# Define the to-do list and load existing tasks
todo_list = load_tasks()

def refresh_listbox():
    listbox.delete(0, tk.END)
    for idx, task in enumerate(todo_list, 1):
        status = "Completed" if task["completed"] else "Pending"
        listbox.insert(tk.END, f"{idx}. {task['task']} [{status}]")

def add_task():
    task = simpledialog.askstring("Add Task", "Enter the task:")
    if task:
        todo_list.append({"task": task, "completed": False})
        save_tasks()
        refresh_listbox()

def toggle_task_status():
    selected = listbox.curselection()
    if selected:
        task_number = selected[0]
        todo_list[task_number]["completed"] = not todo_list[task_number]["completed"]
        save_tasks()
        refresh_listbox()
    else:
        messagebox.showwarning("No Selection", "Please select a task to toggle its status.")

def delete_task():
    selected = listbox.curselection()
    if selected:
        task_number = selected[0]
        task = todo_list.pop(task_number)
        save_tasks()
        refresh_listbox()
        messagebox.showinfo("Task Deleted", f"Deleted task: '{task['task']}'")
    else:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create the listbox to display tasks
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Create buttons for actions
btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

toggle_btn = tk.Button(btn_frame, text="Toggle Complete", command=toggle_task_status)
toggle_btn.grid(row=0, column=1, padx=5)

delete_btn = tk.Button(btn_frame, text="Delete Task", command=delete_task)
delete_btn.grid(row=0, column=2, padx=5)

# Populate the listbox with existing tasks
refresh_listbox()

# Run the main event loop
root.mainloop()
