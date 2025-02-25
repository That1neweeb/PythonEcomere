import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
# Create main window
root = tk.Tk()
root.title("Forgot Password")
root.geometry("900x600")
root.configure(bg="white")
 
def signup():
     pid3 = subprocess.Popen([sys.executable,"register.py"])

# Function to handle password reset action
def reset_password():
    user_input = entry.get()
    if user_input:
        messagebox.showinfo("Reset Password", f"Password reset link sent to: {user_input}")
    else:
        messagebox.showwarning("Input Error", "Please enter your email, phone, or username.")

# Heading
heading = tk.Label(root, text="Oh, no !", font=("Arial", 20, "bold"), fg="black", bg="white")
heading.pack(pady=(40, 0))

subheading = tk.Label(root, text="I forgot", font=("Arial", 20, "bold"), fg="black", bg="white")
subheading.pack()

# Instructions
instruction = tk.Label(root, text="Enter your email, phone, or username\nand we'll send you a link to change your password", 
                       font=("Arial", 10), fg="gray", bg="white", justify="center")
instruction.pack(pady=10)

# Input field
entry = tk.Entry(root, width=40, font=("Arial", 12), bd=2, relief="solid")
entry.pack(pady=10)

# Forgot Password Button
forgot_btn = tk.Button(root, text="Forgot Password", font=("Arial", 12, "bold"), bg="black", fg="white", 
                       width=20, height=2, command=reset_password)
forgot_btn.pack(pady=20)

# Sign Up Option
signup_label = tk.Label(root, text="Don't have an account?", font=("Arial", 10), fg="gray", bg="white")
signup_label.pack()

signup_btn = tk.Button(root, text="Sign Up", font=("Arial", 10, "bold"), fg="black", bg="white", bd=0,command=signup)
signup_btn.pack()

# Run the Tkinter loop
root.mainloop()
