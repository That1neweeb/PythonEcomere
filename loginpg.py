from tkinter import*
from PIL import Image, ImageTk
from tkinter import messagebox 
import subprocess
import sys

root=Tk()
root.geometry('900x600')
root.iconbitmap("cart.ico")
root.title("BooksHive")
def book():
    pid1 = subprocess.Popen([sys.executable, "dashboard prototype.py"])
 #passwordentrybox
def show():
    if btn.get():
        e2.config(show="")
    else:
        e2.config(show="*")

#recoverpassword
def open():
    top=Toplevel()
    top.title( 'Recover your Password ')

#registeraccount
def signup():
    top1=Toplevel()
    top1.title('Register your account')

#becomeaseller
def seller():
    messagebox.showinfo('Error','Feature not available')


#username
name =  Label(root,text ="Username",font=("calibre",10,'bold')).place(x=425,y=225)
e1=Entry(root).place(x=500,y=225)

btn=IntVar()
chk=Checkbutton(text='show password',variable=btn,command=show).place(x=630,y=275)

#password
password=Label(root,text="Password",font=("calibre",10,'bold')).place(x=425,y=280)
e2=Entry(root,show='*')
e2.place(x=500,y=280)

#loginbutton
Login=Button(root,text="Login",padx=75,bg='#000000',fg='white',font="bold",command=book).place(x=435,y=350)

# check 
box=Checkbutton(root,text="Remember Me").place(x=420,y=320)
froget=Button(root,text="Forgot Password?",font=("calibre",10,'bold'),borderwidth=0,relief='flat',activebackground='gray',command=open).place(x=600,y=320)


#img
img=Image.open("logo.png")
resized=img.resize((70,60))
convertedimg=ImageTk.PhotoImage(resized)
imglbl=Label(root,image=convertedimg,width=50,height=40) .place(x=495,y=100)
lbl=Label(root,text="Welcome to BooksHive!",font=("calibre",10,'bold')).place(x=450,y=165)


#register
lbl1=Label(root,text="Don't have an account?").place(x=435,y=425)
lbl2=Button(root,text="Sign Up",font=("calibre",10,'bold'),borderwidth=0,relief='flat',activebackground='gray',command=signup).place(x=575,y=425)


lbl3=Button(root,text="Become a Seller!",font=("calibre",10,'bold'),borderwidth=0,relief='flat',activebackground='gray',command=seller).place(x=475,y=475)




mainloop()