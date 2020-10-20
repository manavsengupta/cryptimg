#Importing Stuff
from Crypto.Cipher import AES
import io
import PIL.Image
from tkinter import *
import os

#Private Stuff
key = b'Key of length 16' #Todo Enter a Key(Like a password only) Here of Length 16 (Both Key and ivb required keep both safely and securely)
iv = b'ivb of length 16' #Todo Enter a ivb (Like a password only) Here of Length 16 (Both Key and ivb required keep both safely and securely)




#Encrypting Image
def encrypt_image():
    global key,iv,entry_for_folder
    file_path=str(entry_for_folder.get())
    if(file_path=="" or file_path[0]==" "):
        file_path=os.getcwd()
    files=[]
    # r=root, d=directories, f = files
    for r, d, f in os.walk(file_path):
        for file in f:
            if((('.JPG' in file) or ('.jpg' in file)) and ('.enc' not in file)):
                files.append(os.path.join(r, file))
    for file_name in files:
        input_file = open(file_name,"rb")
        input_data = input_file.read()
        input_file.close()

        cfb_cipher = AES.new(key, AES.MODE_CFB, iv)
        enc_data = cfb_cipher.encrypt(input_data)

        enc_file = open(file_name+".enc", "wb")
        enc_file.write(enc_data)
        enc_file.close()


#Decrypting Image
def decrypt_image():
    global key,iv,entry_for_folder
    file_path = str(entry_for_folder.get())
    if (file_path == "" or file_path[0] == " "):
        file_path = os.getcwd()
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(file_path):
        for file in f:
            if '.enc' in file:
                files.append(os.path.join(r, file))
    for file_name in files:
        enc_file2 = open(file_name,"rb")
        enc_data2 = enc_file2.read()
        enc_file2.close()

        cfb_decipher = AES.new(key, AES.MODE_CFB, iv)
        plain_data = (cfb_decipher.decrypt(enc_data2))

        imageStream = io.BytesIO(plain_data)
        imageFile = PIL.Image.open(imageStream)
        imageFile.save((file_name[:-8])+".jpg")




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

