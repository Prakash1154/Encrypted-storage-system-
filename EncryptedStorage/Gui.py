from tkinter import *

def stop():
    print(type(entry_1.get()))
    print(entry_1.get())
    root.destroy()
        
root = Tk()
root.geometry('500x500')
root.title("SECRET STROGE SYSTEM")

label_0 = Label(root, text="USER LOGIN ",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="User Id:",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)
print(entry_1.get())
label_2 = Label(root, text="Password:",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)
print(entry_2.get())
Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=190,y=250)

Button(root, text='EXIT',width=20,bg='brown',fg='white',command=stop).place(x=190,y=300)

root.mainloop()

