from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

# Initialize main window
hmp = customtkinter.CTk()
hmp.geometry("1400x800")
hmp.resizable(True, True)
hmp.title("BookHive")
hmp.iconbitmap("cart.ico")
customtkinter.set_appearance_mode("light")  
hmp.configure(fg_color="yellow")  

# ------------ DATABASE SETUP ------------
con = sqlite3.connect('books.db')
cur = con.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS books (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 image TEXT
            )''')
con.commit()

# ------------ BACKGROUND IMAGE ------------
bg_img = Image.open("appbg.png")  
bg_img = ImageTk.PhotoImage(bg_img)

bg_label = customtkinter.CTkLabel(hmp, image=bg_img)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)  # Ensure the background is placed properly

# Prevent garbage collection
hmp.bg_img_ref = bg_img

# -------------- PREORDER BUTTON -------------
def perordr_optn():
    messagebox.showinfo("Invalid", "feature not available yet")

# -------------- CART FUNCTIONALITY -------------
cart_items = []  # This will store books added to the cart

def view_cart():
    """ View the books added to the cart """
    cart_window = Toplevel(hmp)
    cart_window.geometry("400x400")
    cart_window.title("Your Cart")

    if not cart_items:
        empty_label = customtkinter.CTkLabel(cart_window, text="Your cart is empty.", font=("Arial", 16))
        empty_label.pack(pady=20)
    else:
        for book_name in cart_items:
            book_label = customtkinter.CTkLabel(cart_window, text=book_name, font=("Arial", 14))
            book_label.pack(pady=5)
        
    # Add a button to close the cart window
    close_btn = customtkinter.CTkButton(cart_window, text="Close", command=cart_window.destroy, fg_color="red", text_color="white", width=150, height=40)
    close_btn.pack(pady=20)

# ------------ DASHBOARD BUTTONS ------------
info_button = customtkinter.CTkButton(hmp, text='User', fg_color="transparent", text_color="black", width=80, height=30)
info_button.place(x=30, y=10)

name = customtkinter.CTkLabel(hmp, text="*Username")
name.place(x=100, y=10)

contact_btn = customtkinter.CTkButton(hmp, text="Contact", fg_color="transparent", text_color="black", width=80, height=30)
contact_btn.place(x=1300, y=10)

about_btn = customtkinter.CTkButton(hmp, text="About", fg_color="transparent", text_color="black", width=80, height=30)
about_btn.place(x=1200, y=10)

preordr_btn = customtkinter.CTkButton(hmp, text="Pre Order", fg_color="transparent", text_color="black", command=perordr_optn, width=80, height=30)
preordr_btn.place(x=1100, y=10)

cart_btn = customtkinter.CTkButton(hmp, text="Cart", fg_color="transparent", text_color="black", width=80, height=30, command=view_cart)
cart_btn.place(x=1000, y=10)

Home_btn = customtkinter.CTkButton(hmp, text="Home", fg_color="transparent", text_color="black", width=80, height=30)
Home_btn.place(x=900, y=10)

# ------------ SEARCH BOX BACKGROUND ------------
srchbox_img_raw = Image.open("Bookimg.png")  
srchbox_img_resized = srchbox_img_raw.resize((1400, 450))  
srchbox_img = ImageTk.PhotoImage(srchbox_img_resized)

srchbox_background = customtkinter.CTkLabel(hmp, image=srchbox_img)
srchbox_background.place(x=200, y=100)

# Prevent garbage collection
hmp.srchbox_img_ref = srchbox_img

# ------------ SEARCH BOX ------------
Srchbox = customtkinter.CTkEntry(hmp, placeholder_text="Search", width=300, height=30)
Srchbox.place(x=550, y=400)  

# ------------ RECOMMENDATIONS & NEW ARRIVALS ------------
New_arrival = customtkinter.CTkButton(hmp, text="Recommendation", text_color="black", fg_color="transparent", width=150)
New_arrival.place(x=100, y=500)

offer_button = customtkinter.CTkButton(hmp, text="New Arrivals", text_color="black", fg_color="transparent", width=150)
offer_button.place(x=100, y=550)

# ------------ FUNCTION TO OPEN BOOK DETAILS WINDOW ------------
def open_book_window(book_name, book_image):
    """ Open a new window displaying the book details """
    book_window = Toplevel(hmp)
    book_window.geometry("400x500")
    book_window.title(book_name)

    try:
        img = Image.open(book_image)
        img = img.resize((200, 250))  
        book_img = ImageTk.PhotoImage(img)
    except Exception as e:
        print("Error loading image:", e)
        book_img = None

    if book_img:
        img_label = customtkinter.CTkLabel(book_window, image=book_img)
        img_label.image = book_img  
        img_label.pack(pady=10)

    book_label = customtkinter.CTkLabel(book_window, text=book_name, font=("Arial", 18))
    book_label.pack()

    def add_to_cart():
        """ Add the book to the cart """
        cart_items.append(book_name)
        messagebox.showinfo("Added", f"{book_name} has been added to your cart.")
        
    add_to_cart_btn = customtkinter.CTkButton(book_window, text="Add to Cart", fg_color="green", text_color="white", width=150, height=40, command=add_to_cart)
    add_to_cart_btn.pack(pady=10)

    back_btn = customtkinter.CTkButton(book_window, text="Back", command=book_window.destroy, fg_color="red", text_color="white", width=150, height=40)
    back_btn.pack(pady=10)

# ------------ BOOK BUTTONS (DYNAMIC LOADING) ------------
cur.execute("DELETE FROM books")  # Clear existing records
cur.execute("INSERT INTO books (name, image) VALUES ('Book 1', 'book1.png'), ('Book 2', 'book2.png'), ('Book 3', 'book3.png'), ('Book 4', 'book4.png')")
con.commit()

cur.execute("SELECT * FROM books")
books = cur.fetchall()

x_position = 800
for book in books:
    book_id, book_name, book_image = book
    btn = customtkinter.CTkButton(hmp, text=book_name, text_color="black", width=100, height=100, 
                                  command=lambda b=book: open_book_window(b[1], b[2]))
    btn.place(x=x_position, y=500)
    x_position += 150

# Run the main loop
hmp.mainloop()
