from tkinter import *
from tkinter import messagebox


def login():
    username=entry1.get()
    password=entry2.get()

    if (username=="" and password==""):
        messagebox.showinfo("","Blank Not Allowed")

    elif (username=="Sifa" and password=="admin"):
        messagebox.showinfo("","Login success")

    else:
        messagebox.showinfo("","incorrect username and password")


root = Tk()
root.title("Happy App Login")
root.geometry("500x500")
root.configure(bg='lightpink')

global entry1
global entry2

Label(root,text="Username").place(x=20,y=20)
Label(root,text="Password").place(x=20,y=80)


entry1=Entry(root,bd=1)
entry1.place(x=140,y=20)

entry2=Entry(root,bd=1)
entry2.place(x=140,y=70)

Button(root,text="Login",command=login,height=3,width=13,bd=6,bg='gray',fg='lightblue').place(x=100,y=120)


root.mainloop()