import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        password_label.config(text="Generated Password: " + password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for password length.")

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Set window size and background color
root.geometry("400x200")
root.configure(bg="#f0f0f0")  # Light gray background color

# Create and pack widgets with some color
length_label = tk.Label(root, text="Enter password length:", bg="#f0f0f0", fg="black",font=200)  # Light gray background and blue text
length_label.pack()

length_entry = tk.Entry(root, bg="white", fg="black",font=200)  # White background and black text
length_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg="red", fg="white",font=200)  # Green button with white text
generate_button.pack()

password_label = tk.Label(root, text="", bg="#f0f0f0", fg="black",font=400)  # Light gray background and red text
password_label.pack()

# Run the main event loop
root.mainloop()
