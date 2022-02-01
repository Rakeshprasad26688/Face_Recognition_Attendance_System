from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x820+0+0")
        self.root.title("face recognition system")

        #=====variable =======
        self.var_attend_id=StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep= StringVar()
        self.var_attend_time= StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance= StringVar()

        # first image

        img = Image.open( r"D:\ty_project\college_images\developer.jpg" )
        img = img.resize( (800, 200), Image.ANTIALIAS )
        self.photoimg = ImageTk.PhotoImage( img )

        label_1 = Label( self.root, image=self.photoimg )
        label_1.place( x=0, y=0, width=800, height=200 )

        # second image
        img2 = Image.open( r"D:\ty_project\college_images\ajgar.jpg" )
        img2 = img2.resize( (800, 200), Image.ANTIALIAS )
        self.photoimg2 = ImageTk.PhotoImage( img2 )

        label_2 = Label( self.root, image=self.photoimg2 )
        label_2.place( x=800, y=0, width=800, height=200 )

        #bg image

        
        img_l = Image.open( r"D:\ty_project\college_images\wp5894291.jpg" )
        img_l = img_l.resize( (1530, 710), Image.ANTIALIAS )
        self.photoimg_l = ImageTk.PhotoImage( img_l )

        bg_image = Label( self.root, image=self.photoimg_l )
        bg_image.place( x=0, y=200, width=1530, height=710 )

        inside_frame = Label(bg_image,text="ATTENDANCE MANAGEMENT SYSTEM",font=("time new roman", 35, "bold") , bd=2,relief=RIDGE, bg="pink" )
        inside_frame.place( x=0, y=0, width=1530, height=45)

        main_frame = Frame(self.root, bd=2, bg="white" )
        main_frame.place( x=10, y=250, width=1500, height=600 )

         #=====left label=======

        Left_frame = LabelFrame( main_frame, bd=2, bg="white", relief=RIDGE, text="STUDENT ATTENDANCE DETAILS",font=("time new roman", 12, "bold") )
        Left_frame.place( x=10, y=10, width=730, height=530 )

        

        img_l = Image.open( r"D:\ty_project\college_images\wp5894291.jpg" )
        img_l = img_l.resize( (720, 130), Image.ANTIALIAS )
        self.photoimg_l = ImageTk.PhotoImage( img_l )

        bg_image = Label( Left_frame, image=self.photoimg_l )
        bg_image.place( x=5, y=0, width=720, height=130 )

        inside_frame = Frame(Left_frame, bd=2,relief=RIDGE, bg="white" )
        inside_frame.place( x=0, y=135, width=720, height=300)

        #===label and entry
        #===attendaceid=====

        attendace_id_label = Label( inside_frame, text="Attendance id:", font=("time new roman", 12, "bold"),bg="white" )
        attendace_id_label.grid( row=0, column=0, padx=10, pady=5, sticky=W )

        attendaceid_entry = ttk.Entry( inside_frame,width=20,textvariable=self.var_attend_id,font=("time new roman", 12, "bold") )#textvariable=self.var_attend_id
        attendaceid_entry.grid( row=0, column=1, padx=10, pady=5, sticky=W )

        #name
        Name_label = Label( inside_frame, text="Name:", font=("time new roman", 12, "bold"),bg="white" )
        Name_label.grid( row=0, column=2, padx=10, pady=5, sticky=W )

        Name_entry = ttk.Entry( inside_frame, width=20,textvariable= self.var_attend_name,font=("time new roman", 12, "bold") )#,textvariable=self.var_attend_name
        Name_entry.grid( row=0, column=3, padx=10, pady=5, sticky=W )

        #roll no


        roll_label = Label( inside_frame, text="Roll:", font=("time new roman", 12, "bold"), bg="white" )
        roll_label.grid( row=1, column=0, padx=10, pady=5, sticky=W )

        roll_entry = ttk.Entry( inside_frame, width=20,textvariable=self.var_attend_roll,font=("time new roman", 12, "bold") )#,textvariable=self.var_attend_roll
        roll_entry.grid( row=1, column=1, padx=10, pady=5, sticky=W )

        #department


        dep_label = Label( inside_frame, text="Department:", font=("time new roman", 12, "bold"), bg="white" )
        dep_label.grid( row=1, column=2, padx=10, pady=5, sticky=W )

        dep_entry = ttk.Entry( inside_frame, width=20,textvariable=self.var_attend_dep, font=("time new roman", 12, "bold") )#textvariable=self.var_attend_dep,
        dep_entry.grid( row=1, column=3, padx=10, pady=5, sticky=W )

        #time

        time_label = Label( inside_frame, text="Time:",font=("time new roman", 12, "bold"), bg="white" )
        time_label.grid( row=2, column=0, padx=10, pady=5, sticky=W )

        time_entry = ttk.Entry( inside_frame, width=20, textvariable=self.var_attend_time,font=("time new roman", 12, "bold") )#textvariable=self.var_attend_time,
        time_entry.grid( row=2, column=1, padx=10, pady=5, sticky=W )

        # date
        date_label = Label( inside_frame, text="Date:", font=("time new roman", 12, "bold"), bg="white" )
        date_label.grid( row=2, column=2, padx=10, pady=5, sticky=W )

        date_entry = ttk.Entry( inside_frame, width=20,textvariable=self.var_attend_date, font=("time new roman", 12, "bold") )#textvariable=self.var_attend_date,
        date_entry.grid( row=2, column=3, padx=10, pady=5, sticky=W )

        #attendace status
        department_status_label = Label( inside_frame, text="Department Staus:", font=("time new roman", 12, "bold"), bg="white" )
        department_status_label.grid( row=3, column=0, padx=10, pady=5, sticky=W )

        department_status_combo = ttk.Combobox( inside_frame,textvariable=self.var_attend_attendance, font=("time new roman", 12, "bold"),state="readonly", width=18 )#textvariable=self.var_attend_attendance,
        department_status_combo["values"] = ("Status", "Present", "Absent")
        department_status_combo.current( 0 )
        department_status_combo.grid( row=3, column=1, padx=10, pady=5, sticky=W )

        # button frame
        btn_frame = Frame(inside_frame, relief=RIDGE )
        btn_frame.place( x=0, y=250, width=740, height=35)
        # import
        import_btn = Button( btn_frame, text="Import csv",command=self.importcsv,width=18, font=("time new roman", 12, "bold"),bg="blue", fg="white" )
        import_btn.grid( row=0, column=0 )
        #===export
        export_btn= Button( btn_frame, text="Export csv",command=self.exportcsv, width=18, font=("time new roman", 12, "bold"), bg="blue",fg="white" )
        export_btn.grid( row=0, column= 1)
        # update
        update_btn = Button( btn_frame, text="Update", width=18,font=("time new roman", 12, "bold"), bg="blue", fg="white" )
        update_btn.grid( row=0, column=2 )

        # reset
        reset_btn = Button( btn_frame, text="Reset",command=self.reset,width=18,font=("time new roman", 12, "bold"), bg="blue", fg="white" )
        reset_btn.grid( row=0, column=3 )

        # =====right label =============

        right_frame = LabelFrame( main_frame, bd=2, bg="white", relief=RIDGE, text="ATTENDANCE DETAILS",font=("time new roman", 12, "bold") )
        right_frame.place( x=775, y=10, width=720, height=530 )

        table_frame = Frame(right_frame,bd=2,relief=RIDGE,bg="white" )
        table_frame.place( x=5, y=5, width=700, height=480)

        #======scroll bar table=======
        scroll_x= ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar( table_frame, orient=VERTICAL )

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading( "roll", text=" Roll")
        self.AttendanceReportTable.heading( "name", text="Name")
        self.AttendanceReportTable.heading( "department", text="Department")
        self.AttendanceReportTable.heading( "time", text="Time")
        self.AttendanceReportTable.heading( "date", text="Date" )
        self.AttendanceReportTable.heading( "attendance", text="Attendance" )
        self.AttendanceReportTable["show"]="headings"

        #to set width
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column( "roll", width=100 )
        self.AttendanceReportTable.column( "name", width=100 )
        self.AttendanceReportTable.column( "department", width=100 )
        self.AttendanceReportTable.column( "time", width=100 )
        self.AttendanceReportTable.column( "date", width=100 )
        self.AttendanceReportTable.column( "attendance", width=100 )


        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

          #=======fetch data =======
    def fetchdata(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("",END,values=i)

            self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)

           

    #====import csv=========
    def importcsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:

              mydata.append(i)
            self.fetchdata(mydata)

    #=====export csv========

    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found to export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename( initialdir=os.getcwd(), title="Open CSV",filetypes=(("CSV File", "*.csv"), ("ALL File", "*.*")), parent=self.root )
            with open(fln,mode="w",newline="") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                  exp_write.writerow(i)
                messagebox.showinfo("Success","Your Data Exported to" + os.path.basename(fln) +"successfully")
        except Exception as es:
            messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

    #======get data =======

    def get_cursor(self,event=""):
      cursor_row=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursor_row)
      rows=content['values']
      self.var_attend_id.set(rows[0])
      self.var_attend_roll.set( rows[1] )
      self.var_attend_name.set( rows[2] )
      self.var_attend_dep.set( rows[3] )
      self.var_attend_time.set( rows[4] )
      self.var_attend_date.set( rows[5] )
      self.var_attend_attendance.set( rows[6] )
        
    
        
    
    ##=====reset data===  

    def reset(self):
      self.var_attend_id.set("")
      self.var_attend_roll.set("")
      self.var_attend_name.set("")
      self.var_attend_dep.set("")
      self.var_attend_time.set("")
      self.var_attend_date.set("")
      self.var_attend_attendance.set("")

            
            
            


        
        


        



if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()