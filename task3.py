import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    password_length = int(length_entry.get())
    if password_length < 8:
        messagebox.showwarning("Warning", "Password length should be at least 8 characters.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(password_length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    password = password_entry.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Success", "Password copied to clipboard!")

# Create the main application window
root = tk.Tk()
root.title("Password Generator by Mithlesh")
root.geometry('500x300')
root.resizable(0, 0)
root.config(bg="Green")

# Create widgets
length_label = tk.Label(root, text="Password Length:", font=('Book Antiqua', 10, 'bold'))
length_label.pack(pady=20)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, font=('Book Antiqua', 10, 'bold'))
generate_button.pack(pady=20)

password_entry = tk.Entry(root, show="")
password_entry.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=('Book Antiqua', 10, 'bold'))
copy_button.pack(pady=10)

root.mainloop()