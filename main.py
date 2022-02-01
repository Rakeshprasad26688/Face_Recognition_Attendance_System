from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import tkinter
import os
from student import Student


from train import Train
from face_recognition import Face_recognition
from attendance import Attendance   



class Face_recognition_system:
    def __init__(self,root):
        self.root =root
        self.root.geometry("1530x790+0+0")
        self.root.title("face recognition system")

        
        # first image

        img = Image.open(r"D:\wallpaper\1324663.jpg")
        img = img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        label_1 = Label(self.root,image=self.photoimg)
        label_1.place(x=0,y=0,width=500,height=130)


        # second image

        img2 = Image.open(r"D:\wallpaper\digital-art-men-city-futuristic-night-hd-wallpaper-preview.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        label_2 = Label(self.root,image=self.photoimg2)
        label_2.place(x=500, y=0, width=500, height=130)

        # third image

        img3 = Image.open(r"D:\ty_project\college_images\Harebrained-Schemes4.jpg")
        img3= img3.resize((500, 130), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        label_2 = Label(self.root, image=self.photoimg3)
        label_2.place(x=1000, y=0, width=550, height=130)

        # background image
    
        img4= Image.open(r"D:\ty_project\college_images\wp5894291.jpg")
        img4= img4.resize((1530,710), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_image = Label(self.root, image=self.photoimg4)
        bg_image.place(x=0, y=130, width=1530, height=710)

        title_label=Label(bg_image,text="FACE RECOGNITION ATTENDACE SYSTEM SOFTWARE",font=("times new roman",35,"bold",),bg="white",fg="red")
        title_label.place(x=0,y=0,width=1530,height=45)


        #student button

        img5 = Image.open(r"D:\ty_project\college_images\student.png")
        img5 = img5.resize((220,220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_image,image=self.photoimg5,command=self.student_details, cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1 = Button(bg_image,text="Student Details",command=self.student_details, cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        #detect face
        
        img6 = Image.open(r"D:\ty_project\college_images\face.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b2 = Button(bg_image, image=self.photoimg6,cursor="hand2",command=self.face_data)
        b2.place(x=650, y=100, width=220, height=220)

        b1_2 = Button(bg_image, text="Face Detect", cursor="hand2",command=self.face_data, font=("times new roman", 15, "bold"), bg="darkblue", fg="white")
        b1_2.place(x=650, y=300, width=220, height=40)

        #Attendace face button

        img7 = Image.open(r"D:\ty_project\college_images\a1.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b2 = Button(bg_image, image=self.photoimg7,cursor="hand2",command=self.attendance_data)
        b2.place(x=1100, y=100, width=220, height=220)

        b1_2 = Button(bg_image, text="Attendance", cursor="hand2",command=self.attendance_data,font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b1_2.place(x=1100, y=300, width=220, height=40)

        #help desk

        #img8 = Image.open(r"D:\ty_project\college_images\help desk.jpg")
        #img8 = img8.resize((220, 220), Image.ANTIALIAS)
        #self.photoimg8 = ImageTk.PhotoImage(img8)

        #b2 = Button(bg_image, image=self.photoimg8,cursor="hand2")
        #b2.place(x=1100, y=100, width=220, height=220)

        #b1_2 = Button(bg_image, text="Help Desk", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        #b1_2.place(x=1100, y=300, width=220, height=40)

        #Train Data

        img9 = Image.open(r"D:\ty_project\college_images\train data.png")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b2 = Button(bg_image, image=self.photoimg9,cursor="hand2",command=self.train_data)
        b2.place(x=200, y=380, width=220, height=220)

        b1_2 = Button(bg_image, text="Train Data", cursor="hand2",command=self.train_data, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b1_2.place(x=200, y=580, width=220, height=40)

        #photo face button

        img10 = Image.open(r"D:\ty_project\college_images\photo.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b2 = Button(bg_image, image=self.photoimg10,cursor="hand2",command=self.open_img)
        b2.place(x=650, y=380, width=220, height=220)

        b1_2 = Button(bg_image, text="Photo", cursor="hand2",command=self.open_img, font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        b1_2.place(x=650, y=580, width=220, height=40)

        # Developer face button

        #img11 = Image.open(r"D:\ty_project\college_images\developer.jpg")
        #img11 = img11.resize((220, 220), Image.ANTIALIAS)
        #self.photoimg11 = ImageTk.PhotoImage(img11)

        #b2 = Button(bg_image, image=self.photoimg11)
        #b2.place(x=800, y=380, width=220, height=220)

        #b1_2 = Button(bg_image, text="Developer", cursor="hand2", font=("times new roman", 15, "bold"), bg="darkblue",fg="white")
        #b1_2.place(x=800, y=580, width=220, height=40)

        #  exit face button

        img12 = Image.open(r"D:\ty_project\college_images\exit.png")
        img12 = img12.resize((220, 220), Image.ANTIALIAS)
        self.photoimg12 = ImageTk.PhotoImage(img12)

        b2 = Button(bg_image, image=self.photoimg12,cursor="hand2",command=self.iexit)
        b2.place(x=1100, y=380, width=220, height=220)

        b1_2 = Button(bg_image, text="Exit", cursor="hand2",command=self.iexit, font=("times new roman", 15, "bold"), bg="darkblue",fg="white",)
        b1_2.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")    

    def iexit(self):
        self.iexit=tkinter.messagebox.askyesno("Face Recognition","Are You Sure",parent=self.root)
        if self.iexit >0:
           self.root.destroy()
        else:
            return



        #==============Function buttons=========================



    def student_details(self):
            self.new_window=Toplevel(self.root)
            self.app=Student(self.new_window)


    def train_data( self ):
        self.new_window = Toplevel( self.root )
        self.app = Train( self.new_window )

    def face_data( self ):
        self.new_window = Toplevel( self.root )
        self.app = Face_recognition( self.new_window )

    def attendance_data(self):
            self.new_window = Toplevel(self.root )
            self.app = Attendance(self.new_window )








if __name__ == "__main__":
    root=Tk()
    obj=Face_recognition_system(root)
    root.mainloop()