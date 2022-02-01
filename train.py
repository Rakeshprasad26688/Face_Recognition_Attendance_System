from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np



class Train:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        title_label = Label(self.root,text="TRAIN DATA SET",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)

        #========imaged top==========
        img_top= Image.open( r"D:\wallpaper\traning.jpg" )
        img_top = img_top.resize( (1530, 325), Image.ANTIALIAS )
        self.photoimg_top = ImageTk.PhotoImage( img_top )

        label = Label(self.root, image=self.photoimg_top)
        label.place( x=0, y=55, width=1530, height=325 )

        # button
        train= Button(self.root, text="TRAIN DATA",command=self.train_classifier,width=11, font=("time new roman",20, "bold"), bg="red",fg="white" )
        train.place(x=0,y=380,width=1530,height=60)

        img_bottom = Image.open(r"D:\wallpaper\traning1.jpg")
        img_bottom = img_bottom.resize( (1530, 325), Image.ANTIALIAS )
        self.photoimg_bottom = ImageTk.PhotoImage( img_bottom )

        label = Label(self.root, image=self.photoimg_bottom)
        label.place( x=0, y=440, width=1530, height=325 )

    def train_classifier(self):
        data_dir=("data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L') ##gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids) ####to convert into array numpy is used it increase the speed of conversion


        #=====Train the classifer=======

        clf=cv2.face.LBPHFaceRecognizer_create()# for this pip install opencv-contrib-python

        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training Dataset completed!!")

        

       


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
