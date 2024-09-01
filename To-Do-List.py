import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete!")

def mark_done():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"✓ {task}")
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to mark as done!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create the entry widget for adding tasks
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Create the button to add tasks
add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

# Create the listbox to display tasks
task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

# Create the buttons to delete tasks, mark tasks as done, and clear all tasks
delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=5)

mark_done_button = tk.Button(root, text="Mark Done", command=mark_done)
mark_done_button.pack(pady=5)

clear_tasks_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks)
clear_tasks_button.pack(pady=5)

# Start the main event loop
root.mainloop()
