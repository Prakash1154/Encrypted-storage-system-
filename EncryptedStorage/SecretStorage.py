import os
import os.path
from os.path import isfile,join
from os import listdir
from Crypto import Random
from Crypto.Cipher import AES
import time

class Encryptor:
    def __init__(self,key):
        self.key=key

    #padding to convert the message whole length into multiple of block size
    def padding(self,s):
        return s+b"\0"*(AES.block_size-len(s)% AES.block_size)

    #function to encrypt the data
    def Encrypt(self,message,key,key_size=256): 
        #padding has been done
        pad_message=self.padding(message)
        #intialize Initialisation vector
        IV=Random.new().read(AES.block_size)
        #creating cipher object to encrypt the message
        cipher=AES.new(key,AES.MODE_CBC,IV)
        #Added initialization vector at the begning of the cipher
        return IV+cipher.Encrypt(message)
    
    #Created a function which recieve the file and encrypt the file data
    # And store them into another encrypted file
    def Encrypt_File(self,file_name):
        with open(file_name, 'rb') as ptr:
            PlainText=ptr.read()
            Encrypted_Data=self.Encrypt(PlainText,self.key)
            #store data in another file and delete the oroginal file
            with open(file_name+ ".enc",'wb')as ptr:
                ptr.write(Encrypted_Data)
            os.remove(file_name)

    #function for decrypt the cipher text
    def Decrypt(self,cipherText,key):
        IV=cipherText[:AES.block_size]
        #creating cipher object to encrypt the message
        cipher=AES.new(key,AES.MODE_CBC,IV)
        PlianText=cipher.Decrypt(cipherText[AES.block_size:])
        return PlainText.rstrip(b'\0')


    def Decrypt_File(self,file_name):
        with open(file_name, 'rb') as ptr:
            cipherText=ptr.read()
            Decrypted_Data=self.Decrypt(cipherText,self.key)
            #store data in another file and delete the decrypted oroginal file
            with open(file_name[:-4],'wb')as ptr:
                ptr.write(Decrypted_Data)
            os.remove(file_name)

    #give all the files of the folder excluding python and text file
    def getAllfiles(self):
        dir_path=os.path.dirname(os.path.realpath(__file__))
        dirs=[]
        for dirName,subdirList,fileList in os.walk(dir_path):
            for fname in fileList:
                if(fname!='SecretStorage.py' and fname!='data.txt.enc'):
                    dirs.append(dirName+"\\"+fanme)

        return dirs
    
    def encrypt_all_file(self):
        dirs=self.getAllFiles()
        for file_name in dirs:
            self.Encrypt_File(file_name)


    def decrypt_all_file(self):
        dirs=self.getAllFiles()
        for file_name in dirs:
            self.Decrypt_File(file_name)

key=b'[Ex\xc8\xd5\xbfi{\xa2$\x05(\xd5\x18\xbf\xc0\x85\)\x10nc)j\xdf(\x69'
enc=Encryptor(key)
clear=lambda:os.system('cls')

if os.path.isfile('data.txt.enc'):
    while True:
        password=input("Enter password:  ")
        enc.Decrypt_File("data.txt.enc")
        p=''
        with open('data.txt','r') as ptr:
            p=ptr.readlines()
        if p[0]==password:
            enc.Encrypt_File('data.txt')
            break
        
    while True:
        clear()
        choice=int(input(
            """
                1.encrypt a particular file \n
                2.decrypt a particular file \n
                3.encrypt all file in directory \n
                4.decrypt all file in directory \n
                5.exit
            """))
        clear()
        if choice==1:
            enc.Encrypt_File(input('Enter the name of the file'))
        elif choice==2:
            enc.Decrypt_File(input('Enter the name of the decrypted file'))
        elif choice==3:
            enc.encrypt_all_file()
        elif choice==4:
            enc.decrypt_all_file()
        elif choice==5:
             exit()
        else:
            print('Please enter the valied choice!  ')
            
else:
    while True:
        clear()
        password=str(input('Set a password to enter into the sytem next time:  '))
        repassword=str(input('confirm the password:  '))
        if password==repassword:
            break
        else:
            print('password mismathed! ')
            break
        f=open("data.txt","w+")
        f.write(password)
        f.close()
        enc.Encrypt_File("data.txt")
        print('please restart the program to and enter the password which has given before ')
        time.sleep(15)



    










            
    
