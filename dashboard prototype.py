from tkinter import *
import customtkinter
from PIL import ImageTk, Image

# Initialize main window
hmp = customtkinter.CTk()
hmp.geometry("1400x800")
hmp.resizable(True,True)
hmp.title("BookHive")
hmp.iconbitmap("cart.ico")
customtkinter.set_appearance_mode("light")  # set the background to white
hmp.configure(fg_color="yellow")  


# Background image
bg_img = ImageTk.PhotoImage(Image.open("appbg.png"))
bg_label = customtkinter.CTkLabel(hmp, image=bg_img, text="")  # CustomTkinter doesn't support plain image labels
bg_label.place(relwidth=1, relheight=1)

#-------------DASHBOARD
# -------- Username Display --------
info_button = customtkinter.CTkButton(hmp, text='User', fg_color="transparent",text_color="black", width=80, height=30)
info_button.place(x=30, y=10)

name = customtkinter.CTkLabel(hmp, text="*Username")
name.place(x=100, y=10)

# -------- Navigation Buttons --------
contact_btn = customtkinter.CTkButton(hmp, text="Contact", fg_color="transparent",text_color="black", width=80, height=30)
contact_btn.place(x=1300, y=10)

about_btn = customtkinter.CTkButton(hmp, text="About", fg_color="transparent",text_color="black", width=80, height=30)
about_btn.place(x=1200, y=10)

preordr_btn = customtkinter.CTkButton(hmp, text="Pre Order", fg_color="transparent",text_color="black", width=80, height=30)
preordr_btn.place(x=1100, y=10)

cart_btn = customtkinter.CTkButton(hmp, text="Cart", fg_color="transparent",text_color="black", width=80, height=30)
cart_btn.place(x=1000, y=10)

Home_btn = customtkinter.CTkButton(hmp, text="Home", fg_color="transparent",text_color="black", width=80, height=30)
Home_btn.place(x=900, y=10)

# -------- Search Box Background --------
srchbox_img_raw = Image.open("Bookimg.png")
srchbox_img_resized = srchbox_img_raw.resize((1400, 450))  # Adjust width and height 
srchbox_img = ImageTk.PhotoImage(srchbox_img_resized)
srchbox_background = customtkinter.CTkLabel(hmp, image=srchbox_img, text="",width=500,height=200)
srchbox_background.place(x=200, y=100)

# -------- Search Box --------
Srchbox = customtkinter.CTkEntry(hmp, placeholder_text="Search", width=300, height=30)
Srchbox.place(x=600, y=400)

# -------- Recommendation & New Arrivals --------
New_arrival = customtkinter.CTkButton(hmp, text="Recommendation",text_color="black", fg_color="transparent", width=150)
New_arrival.place(x=100, y=500)

offer_button = customtkinter.CTkButton(hmp, text="New Arrivals",text_color="black", fg_color="transparent", width=150)
offer_button.place(x=100, y=550)

# -------- Book Items --------
itm_1 = customtkinter.CTkButton(hmp, text="BOOK",text_color="black", width=100, height=100)
itm_1.place(x=800, y=500)

itm_2 = customtkinter.CTkButton(hmp, text="BOOK", text_color="black",width=100, height=100)
itm_2.place(x=950, y=500)

itm_3 = customtkinter.CTkButton(hmp, text="BOOK", text_color="black",width=100, height=100)
itm_3.place(x=1100, y=500)

itm_4 = customtkinter.CTkButton(hmp, text="BOOK", text_color="black",width=100, height=100)
itm_4.place(x=1250, y=500)

# Run the main loop
hmp.mainloop()
