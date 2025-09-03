# to_do_gui.py
# Run this in VS Code (Python 3.x)

import tkinter as tk
from tkinter import messagebox

tasks = []  # store tasks as dictionaries {title, status}

def add_task():
    title = task_entry.get()
    if title.strip() == "":
        messagebox.showwarning("Input Error", "Task cannot be empty!")
        return
    tasks.append({"title": title, "status": "Pending"})
    task_entry.delete(0, tk.END)
    refresh_tasks()

def refresh_tasks():
    task_listbox.delete(0, tk.END)
    for idx, task in enumerate(tasks, start=1):
        task_listbox.insert(tk.END, f"{idx}. {task['title']} - {task['status']}")

def mark_complete():
    try:
        index = task_listbox.curselection()[0]
        tasks[index]["status"] = "Completed"
        refresh_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task!")

def update_task():
    try:
        index = task_listbox.curselection()[0]
        new_title = task_entry.get()
        if new_title.strip() == "":
            messagebox.showwarning("Input Error", "Task cannot be empty!")
            return
        tasks[index]["title"] = new_title
        task_entry.delete(0, tk.END)
        refresh_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task!")

def delete_task():
    try:
        index = task_listbox.curselection()[0]
        tasks.pop(index)
        refresh_tasks()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task!")

# GUI setup
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.config(bg="#f0f0f0")

# Title
title_label = tk.Label(root, text="✅ To-Do List App", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Task entry
task_entry = tk.Entry(root, font=("Arial", 14))
task_entry.pack(pady=10, padx=20, fill=tk.X)

# Buttons frame
btn_frame = tk.Frame(root, bg="#f0f0f0")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="➕ Add", width=8, command=add_task, bg="#4CAF50", fg="white")
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(btn_frame, text="✏️ Update", width=8, command=update_task, bg="#2196F3", fg="white")
update_btn.grid(row=0, column=1, padx=5)

complete_btn = tk.Button(btn_frame, text="✔️ Done", width=8, command=mark_complete, bg="#FF9800", fg="white")
complete_btn.grid(row=0, column=2, padx=5)

delete_btn = tk.Button(btn_frame, text="🗑️ Delete", width=8, command=delete_task, bg="#F44336", fg="white")
delete_btn.grid(row=0, column=3, padx=5)

# Task list
task_listbox = tk.Listbox(root, font=("Arial", 12), height=15, selectbackground="#a6a6a6")
task_listbox.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)

# Run app
root.mainloop()
