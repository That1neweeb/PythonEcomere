from tkinter import *
from PIL import Image, ImageTk
import sqlite3
from tkinter import messagebox
import customtkinter

# Initialize main windowx   
roots = customtkinter.CTk()
roots.geometry('900x600')
roots.iconbitmap("cart.ico")
roots.title("BooksHive")
customtkinter.set_appearance_mode("light") 

f = ('Times', 14)  # Global font
# Background Image
bg_image = ImageTk.PhotoImage(Image.open("registerpgbgimage.jpg"))
bg_label = customtkinter.CTkLabel(roots,image=bg_image,text="")
bg_label.place(relwidth=1, relheight=1)
# Connect to SQLite database
con = sqlite3.connect('user.db')
cur = con.cursor()

# Create table if it doesn't exist
cur.execute('''CREATE TABLE IF NOT EXISTS record(
             email TEXT,
             firstname TEXT,
             lastname TEXT,
             contact TEXT,
             username TEXT,
             password TEXT
            )
         ''')
con.commit()

# Function to insert records
def insert_record():
    check_counter = 0
    warn = ""

    # Input validation
    if emailorphn.get() == "":
        warn = "Enter your email"
    else:
        check_counter += 1
    if fname.get() == "":
        warn = "Enter your first name"
    else:
        check_counter += 1
    if lname.get() == "":
        warn = "Enter your last name"
    else:
        check_counter += 1
    if contact.get() == "":
        warn = "Enter your contact number"
    else:
        check_counter += 1
    if username.get() == "":
        warn = "Enter your username"
    else:
        check_counter += 1
    if password.get() == "" or confirm.get() == "":
        warn = "Enter your password and confirm it"
    else:
        check_counter += 1

    # Check if passwords match
    if password.get() != confirm.get():
        warn = "Passwords do not match!"
        check_counter -= 1  # Reduce counter since passwords are invalid

    # If all fields are filled correctly
    if check_counter == 6:
        try:
            con = sqlite3.connect('user.db')
            cur = con.cursor()
            cur.execute("INSERT INTO record VALUES (?, ?, ?, ?, ?, ?)", (
                emailorphn.get(),
                fname.get(),
                lname.get(),
                contact.get(),
                username.get(),
                password.get()
            ))
            con.commit()
            con.close()

            messagebox.showinfo('Confirmation', 'Record Saved')

            # Clear entry fields after successful insertion
            emailorphn.delete(0, END)
            fname.delete(0, END)
            lname.delete(0, END)
            contact.delete(0, END)
            username.delete(0, END)
            password.delete(0, END)
            confirm.delete(0, END)

        except Exception as ep:
            messagebox.showerror('Database Error', str(ep))
    else:
        messagebox.showerror('Error', warn)

# Logo
wlc = Label(roots, text="Welcome")
img2 = Image.open("logo.png")
resizedimg = img2.resize((70, 60))
convertedimg = ImageTk.PhotoImage(resizedimg)
imglbl = Label(roots, image=convertedimg, width=50, height=40)

Label1 = customtkinter.CTkLabel(roots,text="Let's Get Started",font=("",24))
Label1.pack(pady=20)
# Entry boxes
emailorphn = customtkinter.CTkEntry(roots,placeholder_text="Enter Your Email")
emailorphn.pack(pady = 10)
fname = customtkinter.CTkEntry(roots,placeholder_text="Enter Your First Name ")
fname.pack(pady = 10)
lname = customtkinter.CTkEntry(roots,placeholder_text="Enter Your Last Name")
lname.pack(pady = 10)
contact = customtkinter.CTkEntry(roots,placeholder_text="Enter Your Phone number")  # Define the missing contact field
contact.pack(pady = 10)
username = customtkinter.CTkEntry(roots,placeholder_text="Enter Username")
username.pack(pady = 10)
password = customtkinter.CTkEntry(roots,placeholder_text="Enter Your Password", show="*")  # Hide password
password.pack(pady = 10)
confirm = customtkinter.CTkEntry(roots,placeholder_text="Confirm Password", show="*")  # Hide confirm password
confirm.pack(pady = 10)

# Button
SignUp = customtkinter.CTkButton(roots, text="Sign Up",font=("bold",16),command=insert_record)
SignUp.pack()

# Run the application
roots.mainloop()