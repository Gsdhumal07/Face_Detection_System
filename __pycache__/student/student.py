from tkinter import *
from tkinter import ttk
from typing import Sized
from PIL import Image , ImageTk
from tkinter import messagebox


class Student:
    def __init__(self,root):


         self.root=root
         self.root.geometry("1366x768+0+0")
         self.root.title("Face_Recognition_system")

         #=====================variables==========
         self.var_dep=StringVar()
         self.var_course=StringVar()
         self.var_year=StringVar()
         self.var_semister=StringVar()
         self.var_std_id=StringVar()
         self.var_std_name=StringVar()
         self.var_div=StringVar()
         self.var_roll_no=StringVar()
         self.var_gender=StringVar()
         self.var_dob=StringVar()
         self.var_email=StringVar()
         self.var_phone=StringVar()
         self.var_adddres=StringVar()
         self.var_teacher=StringVar()














#img01
         img=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img01.jpg")
         img=img.resize((500,130),Image.ANTIALIAS)
         self.photoimg=ImageTk.PhotoImage(img)

         f_lbl=Label(self.root,image= self.photoimg)
         f_lbl.place(x=0,y=0,width=500,height=130)

#img02
      
         img1=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img02.jpg")
         img1=img1.resize((500,130),Image.ANTIALIAS)
         self.photoimg1=ImageTk.PhotoImage(img1)

         f_lbl=Label(self.root,image= self.photoimg1)
         f_lbl.place(x=500,y=0,width=500,height=130)

#img03         
         img2=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img03.jpg")
         img2=img2.resize((500,130),Image.ANTIALIAS)
         self.photoimg2=ImageTk.PhotoImage(img2)

         f_lbl=Label(self.root,image= self.photoimg2)
         f_lbl.place(x=1000,y=0,width=500,height=130)

#Background Images
         img3=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\background.jpg")
         img3=img3.resize((1366,768),Image.ANTIALIAS)
         self.photoimg3=ImageTk.PhotoImage(img3)

         bg_lbl=Label(self.root,image= self.photoimg3)
         bg_lbl.place(x=0,y=130,width=1366,height=710)

         title_lbl=Label(bg_lbl,text="STUDENTS MANAGMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
         title_lbl.place(x=0,y=0,width=1366,height=45)


         main_frame=Frame(bg_lbl,bd=2)
         main_frame.place(x=5,y=50,width=1335,height=750)

         #left label frame
         #students details
         Left_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Students details",font=("times new roman", 12 ,"bold"))
         Left_frame.place(x=10,y=10,width=640,height=500)

         img_left=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img03.jpg")
         img_left=img_left.resize((625,130),Image.ANTIALIAS)
         self.photoimg_left=ImageTk.PhotoImage(img_left)

         f_lbl=Label(Left_frame,image= self.photoimg_left)
         f_lbl.place(x=5,y=0,width=630,height=130)

        #current course
         current_course_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="current course information",font=("times new roman", 12 ,"bold"))
         current_course_frame.place(x=5,y=130,width=640,height=150)
         #Department
         dep_label=Label(current_course_frame,text="Department",font=("times new roman", 12 ,"bold"),bg="white")
         dep_label.grid(row=0,column=0,padx=10,sticky=W)

         dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman", 12 ,"bold"),state="randomly",width=15)
         dep_combo["values"] =("Select Depart.","computer","IT","Civil","EnTC")
         dep_combo.current(0)
         dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         #course
         course_label=Label(current_course_frame,text="Course",font=("times new roman", 12 ,"bold"),bg="white")
         course_label.grid(row=0,column=2,padx=10,sticky=W)

         course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman", 12 ,"bold"),state="randomly",width=15)
         course_combo["values"] =("Select Course.","FE","SE","TE","BE")
         course_combo.current(0)
         course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

         #year

         year_label=Label(current_course_frame,textvariable=self.var_year,text="Year",font=("times new roman", 12 ,"bold"),bg="white")
         year_label.grid(row=1,column=0,padx=10)

         year_combo=ttk.Combobox(current_course_frame,font=("times new roman", 12 ,"bold"),state="randomly",width=15)
         year_combo["values"] =("Select Course.","2020-21","2021-22","2022-23","2023-24")
         year_combo.current(0)
         year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

         #Semister

         Semister=Label(current_course_frame,textvariable=self.var_semister,text="Year",font=("times new roman", 12 ,"bold"),bg="white")
         Semister.grid(row=1,column=2,padx=10)

         Semister=ttk.Combobox(current_course_frame,font=("times new roman", 12 ,"bold"),state="randomly",width=15)
         Semister["values"] =("Select Course.","2020-21","2021-22","2022-23","2023-24")
         Semister.current(0)
         Semister.grid(row=1,column=3,padx=2,pady=10,sticky=W)
        
         #class Students information
         
         class_students_frame=LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Class Students information",font=("times new roman", 12 ,"bold"))
         class_students_frame.place(x=5,y=250,width=640,height=225)
         #Student ID
         StudentsID_labels=Label(class_students_frame,text="StudentID:",font=("times new roman", 12 ,"bold"),bg="white")
         StudentsID_labels.grid(row=0,column=0,padx=10,pady=5,sticky=W)

         StudentsID_entry=ttk.Entry(class_students_frame,textvariable=self.var_std_id,font=("times new roman", 12 ,"bold"))
         StudentsID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

         #Student Name
         Studentname_labels=Label(class_students_frame,text="Student Name:",font=("times new roman", 12 ,"bold"),bg="white")
         Studentname_labels.grid(row=0,column=2,padx=10,pady=5,sticky=W)

         Studentname_entry=ttk.Entry(class_students_frame,textvariable=self.var_std_name,font=("times new roman", 12 ,"bold"))
         Studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

         #Student Division
         Student_div_labels=Label(class_students_frame,text="Student Div:",font=("times new roman", 12 ,"bold"),bg="white")
         Student_div_labels.grid(row=1,column=0,padx=10,pady=5,sticky=W)

         Student_div_entry=ttk.Entry(class_students_frame,textvariable=self.var_div,font=("times new roman", 12 ,"bold"))
         Student_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
         
         #Roll No
         Student_Roll_no_labels=Label(class_students_frame,text="Roll No:",font=("times new roman", 12 ,"bold"),bg="white")
         Student_Roll_no_labels.grid(row=1,column=2,padx=10,pady=5,sticky=W)

         Student_Roll_no_entry=ttk.Entry(class_students_frame,textvariable=self.var_roll_no,font=("times new roman", 12 ,"bold"))
         Student_Roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

         #Gender
         Student_gender_labels=Label(class_students_frame,text="Gender:",font=("times new roman", 12 ,"bold"),bg="white")
         Student_gender_labels.grid(row=2,column=0,padx=10,pady=5,sticky=W)

         Student_gender_entry=ttk.Entry(class_students_frame,textvariable=self.var_gender,font=("times new roman", 12 ,"bold"))
         Student_gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

         #Email ID
         Student_emailid_labels=Label(class_students_frame,text="Email ID:",font=("times new roman", 12 ,"bold"),bg="white")
         Student_emailid_labels.grid(row=3,column=0,padx=10,pady=5,sticky=W)

         Student_emailid_entry=ttk.Entry(class_students_frame,textvariable=self.var_std_id,font=("times new roman", 12 ,"bold"))
         Student_emailid_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
         #Phone no
         Student_phone_no_labels=Label(class_students_frame,text="Phone no:",font=("times new roman", 12 ,"bold"),bg="white")
         Student_phone_no_labels.grid(row=3,column=2,padx=10,pady=5,sticky=W)

         Student_phone_no_entry=ttk.Entry(class_students_frame,textvariable=self.var_phone,font=("times new roman", 12 ,"bold"))
         Student_phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         #Address
         Student_address_labels=Label(class_students_frame,text="Address:",font=("times new roman", 12 ,"bold"),bg="white")
         Student_address_labels.grid(row=4,column=0,padx=10,pady=5,sticky=W)

         Student_address_entry=ttk.Entry(class_students_frame,textvariable=self.var_adddres,font=("times new roman", 12 ,"bold"))
         Student_address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

         #Teacher name
         techername_labels=Label(class_students_frame,text="Teacher Name:",font=("times new roman", 12 ,"bold"),bg="white")
         techername_labels.grid(row=4,column=2,padx=10,pady=5,sticky=W)

         techername_entry=ttk.Entry(class_students_frame,textvariable=self.var_teacher,font=("times new roman", 12 ,"bold"))
         techername_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio button
         self.var_radio1=StringVar()
         Radionbtn1=ttk.Radiobutton(class_students_frame,variable=self.var_radio1,text="Take Student Sample",value="yes")
         Radionbtn1.grid(row=5,column=0)
         
         Radionbtn2=ttk.Radiobutton(class_students_frame,variable=self.var_radio1,text="No photo Sample",value="No")
         Radionbtn2.grid(row=5,column=1)






    
        #Right label frame

         Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Students details",font=("times new roman", 12 ,"bold"))
         Right_frame.place(x=660,y=10,width=660,height=500)

         img_right=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img03.jpg")
         img_right=img_right.resize((625,130),Image.ANTIALIAS)
         self.photoimg_right=ImageTk.PhotoImage(img_right)

         f_lbl=Label(Right_frame,image= self.photoimg_right)
         f_lbl.place(x=5,y=0,width=630,height=130)

         #===============Search System=============
         search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search hub System",font=("times new roman", 12 ,"bold"))
         search_frame.place(x=5,y=100,width=640,height=70)

         search_labels=Label(search_frame,text="Search By:",font=("times new roman", 12 ,"bold"),bg="red",fg="white")
         search_labels.grid(row=0,column=0,padx=10,pady=5,sticky=W)

         Search=ttk.Combobox(search_frame,font=("times new roman", 12 ,"bold"),state="randomly",width=15)
         Search["values"] =("Select Course.","Rol no","Phone no")
         Search.current(0)
         Search.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         search_entry=ttk.Entry(search_frame,width=15,font=("times new roman", 12 ,"bold"))
         search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


         search_byn=Button(search_frame,text="Search",width=14,font=("times new roman", 12 ,"bold"),bg="red",fg="white")
         search_byn.grid(row=0,column=3)

         showall_byn=Button(search_frame,text="Showall",width=14,font=("times new roman", 12 ,"bold"),bg="red",fg="white")
         showall_byn.grid(row=0,column=4)
         #========================table frame================
         table_frame=Frame(Right_frame,bd=2,relief=RIDGE)
         table_frame.place(x=5,y=175,width=640,height=300)

         scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
         scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

         self.student_table=ttk.Treeview(table_frame,columns=("dep","course","year","sem","id","name","div","roll no","gender","date of birth","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

         scroll_x.pack(side=BOTTOM,fill=X)
         scroll_y.pack(side=RIGHT,fill=Y)
         scroll_x.config(command=self.student_table.xview)
         scroll_y.config(command=self.student_table.yview)

         self.student_table.heading("dep",text="department")
         self.student_table.heading("course",text="course")
         self.student_table.heading("year",text="year")
         self.student_table.heading("sem",text="semister")
         self.student_table.heading("id",text="id")
         self.student_table.heading("name",text="Name")
         self.student_table.heading("div",text="division")
         self.student_table.heading("roll no",text="roll no")
         self.student_table.heading("gender",text="gender")
         self.student_table.heading("date of birth",text="DOB")
         self.student_table.heading("address",text="address")
         self.student_table.heading("teacher",text="teacher")
         self.student_table.heading("photo",text="photosample")
         self.student_table["show"]="headings"

         self.student_table.column("dep",width=100)
         self.student_table.column("course",width=100)
         self.student_table.column("year",width=100)
         self.student_table.column("sem",width=100)
         self.student_table.column("id",width=100)
         self.student_table.column("roll no",width=100)
         self.student_table.column("gender",width=100)
         self.student_table.column("date of birth",width=100)
         self.student_table.column("address",width=100)
         self.student_table.column("teacher",width=100)
         self.student_table.column("photo",width=100)


         self.student_table.pack(fill=BOTH,expand=1)
    
    #=================functions decleration==============
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            messagebox.showinfo("sucess","Welcome ashish mundhe")    
            
    
    
   


if __name__=="__main__":
    root=Tk()
    obj= Student(root)
    root.mainloop()

    
