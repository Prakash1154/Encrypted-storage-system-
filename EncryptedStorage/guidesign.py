from tkinter import *
def stop():
        root.destroy()
root = Tk()
root.geometry('600x600')
root.title("SECRET STROGE SYSTEM")

label_0 = Label(root, text="Operational Form",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="One file encryption",width=20,font=("bold", 10))
label_1.place(x=68,y=130)

entry_1 = Entry(root)
entry_1.place(x=240,y=130)

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=400,y=130)

label_2 = Label(root, text="One file decryption: ",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root)
entry_2.place(x=240,y=180)

Button(root, text='Submit',width=20,bg='brown',fg='white').place(x=400,y=180)

label_3 = Label(root, text="All file encryption of directory:",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Button(root, text='OK',width=20,bg='brown',fg='white').place(x=240,y=230)

label_4 = Label(root, text="All file decryption of directory:",width=20,font=("bold", 10))
label_4.place(x=68,y=280)

Button(root, text='OK',width=20,bg='brown',fg='white').place(x=240,y=280)


Button(root, text='EXIT',width=20,bg='brown',fg='white',command=stop).place(x=180,y=380)

root.mainloop()


















entry_3.place(x=240,y=280)
