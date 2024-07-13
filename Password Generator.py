import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    characters = ""
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        messagebox.showwarning("Input Error", "Please select at least one character type")
        return ""
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def on_generate_button_click():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showwarning("Input Error", "Please enter a positive number for length")
            return

        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_symbols = symbols_var.get()

        password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
        if password:
            result_label.config(text=f"{password}")
    except ValueError:
        messagebox.showerror("Input Error", "Invalid input. Please enter a valid number for length.")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("250x350") 

header_label= tk.Label(root, text = "Password Generator", font = ("Brush Script MT", "20"), foreground = "#000000")
header_label.pack(pady=3)

# Create and place the length label and entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Create and place the checkboxes for character types
upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

upper_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=upper_var)
upper_check.pack(pady=2)
lower_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lower_var)
lower_check.pack(pady=2)
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack(pady=2)
symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_check.pack(pady=2)

# Create and place the generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_button_click)
generate_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(root, text="" , background="#ffffff", font = ("Consolas", "14", "bold"))
result_label.pack(pady=10)

# Run the application
root.mainloop()
