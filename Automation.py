import cv2
import dropbox
import time
import random

start_time = time.time()


  

 
def upload_file(img_name):
    access_token = 'ALVjoFNK01IAAAAAAAAAAUAmgLjzwruP2PyxFdwQwOow4StLjYG2-RwksP36PJu0'
    file =img_name
    file_from = file
    file_to="/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
     while(True):
         if ((time.time() - start_time) >= 5):
             name  = take_snapshot()
             upload_file(name)      

main()          