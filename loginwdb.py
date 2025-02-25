from tkinter import *
from PIL import Image, ImageTk
import subprocess
import sys
import sqlite3
from tkinter import messagebox

root = Tk()
root.geometry('900x600')
root.iconbitmap("cart.ico")
root.title("BooksHive")

def check_login():
    """Validates user login credentials"""
    username = e1.get()
    password = e2.get()
    
    if not username or not password:
        messagebox.showerror("Invalid Input", "Fields must not be empty")
        return
    
    conn = sqlite3.connect("user.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM records WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    
    if user:
        book()  # If credentials are correct, proceed to the next window
        root.destroy() #to close window after login is successful
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

def book():
    subprocess.Popen([sys.executable, "dashboard prototype.py"])

def show():
    if btn.get():
        e2.config(show="")
    else:
        e2.config(show="*")

def open():
    top = Toplevel()
    top.title('Recover your Password')

def signup():
    pid3 = subprocess.Popen([sys.executable,"register.py"])

def seller():
    messagebox.showinfo('Error','Feature not available')

# Username field
Label(root, text="Username", font=("calibre", 10, 'bold')).place(x=425, y=225)
e1 = Entry(root)
e1.place(x=500, y=225)

btn = IntVar()
Checkbutton(text='Show password', variable=btn, command=show).place(x=630, y=275)

# Password field
Label(root, text="Password", font=("calibre", 10, 'bold')).place(x=425, y=280)
e2 = Entry(root, show='*')
e2.place(x=500, y=280)

# Login button with authentication
Button(root, text="Login", padx=75, bg='#000000', fg='white', font="bold", command=check_login).place(x=435, y=350)

# Additional UI elements
Checkbutton(root, text="Remember Me").place(x=420, y=320)
Button(root, text="Forgot Password?", font=("calibre", 10, 'bold'), borderwidth=0, relief='flat', activebackground='gray', command=open).place(x=600, y=320)

# Logo image
img = Image.open("logo.png")
resized = img.resize((70, 60))
convertedimg = ImageTk.PhotoImage(resized)
Label(root, image=convertedimg, width=50, height=40).place(x=495, y=100)
Label(root, text="Welcome to BooksHive!", font=("calibre", 10, 'bold')).place(x=450, y=165)

# Register and seller buttons
Label(root, text="Don't have an account?").place(x=435, y=425)
Button(root, text="Sign Up", font=("calibre", 10, 'bold'), borderwidth=0, relief='flat', activebackground='gray', command=signup).place(x=575, y=425)
Button(root, text="Become a Seller!", font=("calibre", 10, 'bold'), borderwidth=0, relief='flat', activebackground='gray', command=seller).place(x=475, y=475)

mainloop()
