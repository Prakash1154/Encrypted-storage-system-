from Crypto import Random
from Crypto.Cipher import AES
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
from tkinter import *
from tkinter import messagebox

 
class Encrypted_Storage:
    def __init__(self, key):
        self.key = key

    #padding to convert the message whole length 
    def padding(self, s):
        return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

    #function to encrypt the data
    def encrypt_message(self, message, key, key_size=256):
        #padding has been done
        message = self.padding(message)
        #intialize Initialisation vector
        iv = Random.new().read(AES.block_size)
        #creating cipher object to encrypt the message
        cipher = AES.new(key, AES.MODE_CBC, iv)
        #Added initialization vector at the begning of the cipher
        return iv + cipher.encrypt(message)

    #Created a function which recieve the file and encrypt the file data
    # And store them into another encrypted file
    def encrypt_file(self, file_name):
        with open(file_name, 'rb') as ptr:
            plaintext = ptr.read()
        enc = self.encrypt_message(plaintext, self.key)
        
        with open(file_name + ".enc", 'wb') as ptr:
            ptr.write(enc)
        os.remove(file_name)

    def decrypt_message(self, ciphertext, key):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b"\0")

    def decrypt_file(self, file_name):
        with open(file_name, 'rb') as ptr:
            ciphertext = ptr.read()
        dec = self.decrypt_message(ciphertext, self.key)
        with open(file_name[:-4], 'wb') as fo:
            fo.write(dec)
        os.remove(file_name)

    def getAllFiles(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        dirs = []
        for dirName, subdirList, fileList in os.walk(dir_path):
            for fname in fileList:
                if (fname != 'newgui.py' and fname != 'data.txt.enc'):
                    dirs.append(dirName + "\\" + fname)
        return dirs

    def encrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.encrypt_file(file_name)

    def decrypt_all_files(self):
        dirs = self.getAllFiles()
        for file_name in dirs:
            self.decrypt_file(file_name)


                    
key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
enc = Encrypted_Storage(key)
clear = lambda: os.system('cls')

#first Time setup password and id for the Secret storage 
def login():    
        #from tkinter import *
        def stop():
            root.destroy()
            exit()

        def verify():
            Uid=entry_1.get()
            pas=entry_2.get()
            file = open("data.txt", "w+")
            s=str(Uid)+str(pas)
            file.write(s)
            file.close()
            enc.encrypt_file("data.txt")
            messagebox.showerror("","Please LOGIN the system to Encryption and Decryption operation")
            
        
        root = Tk()
        root.geometry('500x500')
        root.title("SECRET STROGE SYSTEM")

        label_0 = Label(root, text="---USER SIGNUP---",width=20,font=("bold", 20))
        label_0.place(x=90,y=53)


        label_1 = Label(root, text="User Id:",width=20,font=("bold", 10))
        label_1.place(x=80,y=130)

        entry_1 = Entry(root)
        entry_1.place(x=240,y=130)

        label_2 = Label(root, text="Password:",width=20,font=("bold", 10))
        label_2.place(x=68,y=180)

        entry_2 = Entry(root)
        entry_2.place(x=240,y=180)

        Button(root, text='Submit',width=20,bg='brown',fg='white',command=verify).place(x=190,y=250)

        Button(root, text='EXIT',width=20,bg='brown',fg='white',command=stop).place(x=190,y=300)

        root.mainloop()

        
#GUI designing and checking their validity and also perform all operation.
if os.path.isfile('data.txt.enc'):
    
    def verify2():
        key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
        enc = Encrypted_Storage(key)
        Uid=entry_1.get()
        pas=entry_2.get()
        s=str(Uid)+str(pas)
        enc.decrypt_file("data.txt.enc")
        p = ''
        with open("data.txt", "r") as ptr:
            p = ptr.readlines()
        if p[0] == s:
            enc.encrypt_file("data.txt")
            x=messagebox.showerror("","Yes password and id are matched")
            if x=='ok':
                def stop():
                    root.destroy()
                def enc():
                    key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
                    enc = Encrypted_Storage(key)
                    z=entry_11.get()
                    enc.encrypt_file(z)
                    messagebox.showerror("","Congratulation your file encrypted successfully please check your current directory")
                    
                def dec():
                    key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
                    enc = Encrypted_Storage(key)
                    print(entry_22.get())
                    enc.decrypt_file(entry_22.get())
                    messagebox.showerror("","Congratulation your file decrypted successfully please check your current directory")
                    
                def allenc():
                    key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
                    enc = Encrypted_Storage(key)
                    enc.encrypt_all_files()
                    messagebox.showerror("","Congratulation your all file encrypted successfully please check your current directory")
                def alldec():
                    key = b'[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e'
                    enc = Encrypted_Storage(key)
                    enc.decrypt_all_files()
                    messagebox.showerror("","Congratulation your all file decrypted successfully please check your current directory")
                root = Tk()
                root.geometry('600x600')
                root.title("SECRET STROGE SYSTEM")

                label_0 = Label(root, text="Operational Form",width=20,font=("bold", 20))
                label_0.place(x=90,y=53)


                label_1 = Label(root, text="One file encryption",width=20,font=("bold", 10))
                label_1.place(x=68,y=130)

                entry_11 = Entry(root)
                entry_11.place(x=240,y=130)
                    
                Button(root, text='Submit',width=20,bg='brown',fg='white',command=enc).place(x=400,y=130)

                label_2 = Label(root, text="One file decryption with(.enc): ",width=20,font=("bold", 10))
                label_2.place(x=68,y=180)

                entry_22= Entry(root)
                entry_22.place(x=240,y=180)

                Button(root, text='Submit',width=20,bg='brown',fg='white',command=dec).place(x=400,y=180)

                label_3 = Label(root, text="All file encryption of directory:",width=20,font=("bold", 10))
                label_3.place(x=70,y=230)

                Button(root, text='OK',width=20,bg='brown',fg='white',command=allenc).place(x=240,y=230)

                label_4 = Label(root, text="All file decryption of directory:",width=20,font=("bold", 10))
                label_4.place(x=68,y=280)

                Button(root, text='OK',width=20,bg='brown',fg='white',command=alldec).place(x=240,y=280)


                Button(root, text='EXIT',width=20,bg='brown',fg='white',command=stop).place(x=180,y=380)

                root.mainloop()           
        
        else:
            messagebox.showerror("","Invalied password or id Please Again SIGNUP")
            
            
    def stop():
        root.destroy()
        exit()    
    root = Tk()
    root.geometry('500x500')
    root.title("SECRET STROGE SYSTEM")

    label_0 = Label(root, text="---USER LOGIN---",width=20,font=("bold", 20))
    label_0.place(x=90,y=53)


    label_1 = Label(root, text="User Id:",width=20,font=("bold", 10))
    label_1.place(x=80,y=130)

    entry_1 = Entry(root)
    entry_1.place(x=240,y=130)

    label_2 = Label(root, text="Password:",width=20,font=("bold", 10))
    label_2.place(x=68,y=180)

    entry_2 = Entry(root)
    entry_2.place(x=240,y=180)

    Button(root, text='Submit',width=20,bg='brown',fg='white',command=verify2).place(x=190,y=250)

    Button(root, text='EXIT',width=20,bg='brown',fg='white',command=stop).place(x=190,y=300)

    root.mainloop()
        
else:
   clear()
   login()
            
        

        

