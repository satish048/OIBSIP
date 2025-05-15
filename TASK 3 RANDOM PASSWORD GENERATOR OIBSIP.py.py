import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            raise ValueError

        character_pool = ""
        if var_upper.get():
            character_pool += string.ascii_uppercase
        if var_lower.get():
            character_pool += string.ascii_lowercase
        if var_digits.get():
            character_pool += string.digits
        if var_symbols.get():
            character_pool += string.punctuation
        if var_exclude_similar.get():
            for c in "O0Il1":
                character_pool = character_pool.replace(c, "")

        if not character_pool:
            messagebox.showerror("No Options Selected", "Please select at least one character type.")
            return

        password = ''.join(random.choice(character_pool) for _ in range(length))
        password_var.set(password)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number (at least 4).")

def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Advanced Password Generator")
root.geometry("400x350")
root.resizable(False, False)

# Length input
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

# Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_symbols = tk.BooleanVar(value=True)
var_exclude_similar = tk.BooleanVar(value=False)

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Include Symbols", variable=var_symbols).pack(anchor="w", padx=20)
tk.Checkbutton(root, text="Exclude Similar Characters (e.g., O/0, I/1, l)", variable=var_exclude_similar).pack(anchor="w", padx=20)

# Generate button
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Result display
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Courier", 14), justify="center", width=30).pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack(pady=5)

root.mainloop()
