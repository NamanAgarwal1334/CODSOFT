import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to add a task to the list
def add_task():
    task = task_field.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_field.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task from the list
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        task_listbox.delete(task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task.")

# Function to update a selected task as done
def update_task_done():
    try:
        task_index = task_listbox.curselection()[0]
        task = task_listbox.get(task_index)
        task_listbox.delete(task_index)
        task_listbox.insert(tk.END, task + " [Done]")
    except:
        messagebox.showwarning("Warning", "You must select a task.")

# function to close the application  
def close():    
    print(task_listbox)  
    root.destroy() 

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x450+750+250")    
root.resizable(0, 0)  
root.configure(bg = "#FAEBD7")

# defining frames using the tk.Frame() widget  
header_frame = tk.Frame(root, bg = "#FAEBD7")  
functions_frame = tk.Frame(root, bg = "#FAEBD7")  
listbox_frame = tk.Frame(root, bg = "#FAEBD7")  

# using the pack() method to place the frames in the application  
header_frame.pack(fill = "both")  
functions_frame.pack(side = "left", expand = True, fill = "both")  
listbox_frame.pack(side = "right", expand = True, fill = "both") 

# defining a label 
header_label = ttk.Label(  
        header_frame,  
        text = "To-Do List",  
        font = ("Brush Script MT", "50"),  
        background = "#FAEBD7",  
        foreground = "#8B4513"  
    )  
header_label.pack(padx = 20, pady = 20) 

# defining another label
task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task:",  
        font = ("Consolas", "14", "bold"),  
        background = "#FAEBD7",  
        foreground = "#000000"  
    ) 
task_label.place(x = 30, y = 40)  

# Create an entry widget for task input
task_field = ttk.Entry(  
        functions_frame,  
        font = ("Consolas", "12"),  
        width = 18,  
        background = "#FFF8DC",  
        foreground = "#000000"  
    )  
task_field.place(x = 30, y = 80) 

# Create buttons for adding, deleting, updating and exiting tasks
add_button = ttk.Button(functions_frame, text="Add Task", width=26, command=add_task)
add_button.place(x = 30, y = 120)  

update_button = ttk.Button(functions_frame, text="Update task", width=26, command=update_task_done)
update_button.place(x = 30, y = 160)

delete_button = ttk.Button(functions_frame, text="Delete Task", width=26, command=delete_task)
delete_button.place(x = 30, y = 200)  

exit_button= ttk.Button(functions_frame, text="Exit", width=26, command=close)
exit_button.place(x = 30, y = 240)

# Create a listbox to display tasks
task_listbox = tk.Listbox(  
        listbox_frame,  
        width = 26 ,  
        height = 16,  
        font = ("Consolas", "11"),  
        selectmode = 'SINGLE',  
        background = "#FFFFFF",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
task_listbox.place(x = 10, y = 10)  

# Start the main event loop
root.mainloop()
