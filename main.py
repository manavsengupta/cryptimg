#Importing Stuff
from Crypto.Cipher import AES
import io
import pil.Image
from tkinter import *
import os

#Private Stuff
key = b'Key of length 16' #Todo Enter a Key(Like a password only) Here of Length 16 (Both Key and ivb required keep both safely and securely)
iv = b'ivb of length 16' #Todo Enter a ivb (Like a password only) Here of Length 16 (Both Key and ivb required keep both safely and securely)


cwd_original_1=os.getcwd()

cwd_original=os.path.join(cwd_original_1,"Encrypted")
cwd_original_decrypt=os.path.join(cwd_original_1,"Decrypted")
#Encrypting Image
def encrypt_image():
    try:
        os.mkdir(os.path.join(cwd_original_1,"Encrypted"))
    except:
        pass
    global key,iv,entry_for_folder,root
    file_path=str(entry_for_folder.get())
    if(file_path=="" or file_path[0]==" "):
        file_path=os.getcwd()
    files=[]
    # r=root, d=directories, f = files
    for r, d, f in os.walk(file_path):
        for file in f:
            file_str=file.lower()
            if((".jpg" in file_str or ".png" in file_str) and ('.enc' not in file_str)):
                direc = os.path.split(r)
                cwd=os.path.join(cwd_original,direc[-1])
                try:
                    os.mkdir(cwd)
                except:
                    pass #Chill
                input_file = open((os.path.join(r,file)),"rb")
                input_data = input_file.read()
                input_file.close()
                cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
                enc_data = cfb_cipher.encrypt(input_data)
                enc_file = open(os.path.join(cwd,file)+".enc", "wb")
                enc_file.write(enc_data)
                enc_file.close()
    root.destroy()
    root = Tk()
    root.title("Encryption Successfully Done")
    root.geometry("400x200")
    label = Label(text="Encryption Successfully Done", height=50, width=50, font=(None, 15))
    label.pack(anchor=CENTER, pady=50)
    root.mainloop()
#Decrypting Image
def decrypt_image():
    try:
        os.mkdir(os.path.join(cwd_original_1, "Decrypted"))
    except:
        pass
    global key,iv,entry_for_folder,root
    file_path = str(entry_for_folder.get())
    if (file_path == "" or file_path[0] == " "):
        file_path = os.getcwd()
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(file_path):
        for file in f:
            file_str=file.lower()
            if '.enc' in file_str:
                direc = os.path.split(r)
                cwd = os.path.join(cwd_original_decrypt, direc[-1])
                try:
                    os.mkdir(cwd)
                except:
                    pass #Chill
                enc_file2 = open(os.path.join(r,file),"rb")
                enc_data2 = enc_file2.read()
                enc_file2.close()

                cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
                plain_data = (cfb_decipher.decrypt(enc_data2))

                imageStream = io.BytesIO(plain_data)
                imageFile = pil.Image.open(imageStream)
                file_str=file.lower()
                if(".jpg" in file_str):
                    imageFile.save(((os.path.join(cwd,file))[:-8])+".JPG")
                elif(".png" in file_str):
                    imageFile.save(((os.path.join(cwd, file))[:-8]) + ".png")

    root.destroy()
    root = Tk()
    root.title("Decryption Successfully Done")
    root.geometry("400x200")
    label = Label(text="Decryption Successfully Done",height=50, width=50,font=(None, 15))
    label.pack(anchor=CENTER,pady=50)
    root.mainloop()



#Tkinter Stuff

root=Tk()

root.title("Simple AES Encryption and Decryption of JPG Images")

folder_directory_label=Label(text="Enter the Folder Directory")
folder_directory_label.pack()

entry_for_folder=Entry(root)
entry_for_folder.pack()


encrypt=Button(text="Encrypt All",command=encrypt_image)
encrypt.pack()
label=Label(text="Leave Blank for Current Working Directory")
label.pack()
decrypt=Button(text="Decrypt All",command=decrypt_image)
decrypt.pack()



root.mainloop()

# All good
