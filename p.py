# importing required modules
from zipfile import ZipFile
import os
import cv2
import shutil


# opening the zip file in READ mode
def list_All_Dirs(filename):
    with ZipFile(filename,'r') as zip:
        zip.printdir()
        zip.extractall()
        print("Cropping the Images Done")

    folders = []
    images = []

    # Adding the foldernames from unzippedfile to another 
    for file in os.listdir("tiny_shoppee_train"):
        folders.append(file)
        path = "tiny_shoppee_train" + "/" + file

        # Adding the images from unzippedfile to another folder
        for image in os.listdir(path):
            path1 = path + "/" + image
            images.append(path1)

    # making the folders to new directory
    for i in folders:
        os.makedirs(f'Newfolder/{i}')

    # Resizing the images in the folders
    for j in images:
        img = cv2.imread(j)
        crop = cv2.resize(img,([150,150]))
        k = j.split('/')[1]
        s = j.split('/')[-1]
        if k in j:
            cv2.imwrite(f'Newfolder/{k}/{s}', crop)

    # making the folder to zip file
    shutil.make_archive('Newfolder', 'zip', "/home/ubuntu/Desktop/naresh")

        
list_All_Dirs("tiny_shoppee_train.zip")