from tkinter import * 
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox



class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face_recgonition_system")


        # variables 

        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()



        


        # first image 
        img=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img02.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)  
        f_lbl.place(x=0,y=0,width=500,height=130)

        # second image 
        img1=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img05.jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)  
        f_lbl.place(x=500,y=0,width=500,height=130)

        # third image 
        img2=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img03.jpg")
        img2=img2.resize((600,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)  
        f_lbl.place(x=1000,y=0,width=550,height=130)


        # bg image
        img3=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img03.jpg")
        img3=img3.resize((500,130),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)  
        bg_img.place(x=0,y=130,width=1336,height=710)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red") 
        title_lbl.place(x=0,y=0,width=1366,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=50,width=1300,height=600)


        # left label frame 
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=650,height=500)

        img_left=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img02.jpg")
        img_left=img_left.resize((650,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_frame,image=self.photoimg2)  
        f_lbl.place(x=5,y=0,width=640,height=130)

        # current course information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=640,height=140)


        # department 
        dep_label=Label(current_course_frame,text="department",font=("times new roman",12,"bold"),bg="white")    
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),width=17,state="readonly")
        dep_combo["values"]=("slect department","IT","computer","civil","mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # course
        course_label=Label(current_course_frame,text="course",font=("times new roman",12,"bold"),bg="white")    
        course_label.grid(row=0,column=2,padx=10,sticky=W)


        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("slect course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W) 


        # year
        year_label=Label(current_course_frame,text="year",font=("times new roman",12,"bold"),bg="white")    
        year_label.grid(row=1,column=0,padx=10,sticky=W)


        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_combo["values"]=("slect year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


         # semester
        semester_label=Label(current_course_frame,text="semester",font=("times new roman",12,"bold"),bg="white")    
        semester_label.grid(row=1,column=2,padx=10,sticky=W)


        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly",width=20)
        semester_combo["values"]=("slect semester","semester-1","semester-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # class student information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=640,height=400)

        # student id
        studentID_label=Label(class_student_frame,text="studentId:",font=("times new roman",12,"bold"),bg="white")    
        studentID_label.grid(row=0,column=0,padx=10,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name

        studentname_label=Label(class_student_frame,text="student name :",font=("times new roman",12,"bold"),bg="white")    
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division

        class_div_label=Label(class_student_frame,text="class division",font=("times new roman",12,"bold"),bg="white")    
        class_div_label.grid(row=1,column=0,padx=10,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,textvariable=self.var_div,width=20,font=("times new roman",12,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # roll no

        roll_no_label=Label(class_student_frame,text="roll no",font=("times new roman",12,"bold"),bg="white")    
        roll_no_label.grid(row=1,column=2,padx=10,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # gender

        gender_label=Label(class_student_frame,text="gender",font=("times new roman",12,"bold"),bg="white")    
        gender_label.grid(row=2,column=0,padx=10,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",12,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # dob no

        dob_label=Label(class_student_frame,text="gender",font=("times new roman",12,"bold"),bg="white")    
        dob_label.grid(row=2,column=2,padx=10,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # email

        email_label=Label(class_student_frame,text="email",font=("times new roman",12,"bold"),bg="white")    
        email_label.grid(row=3,column=0,padx=10,sticky=W)

        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # phone no

        phone_label=Label(class_student_frame,text="phone",font=("times new roman",12,"bold"),bg="white")    
        phone_label.grid(row=3,column=2,padx=10,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # address

        address_label=Label(class_student_frame,text="address",font=("times new roman",12,"bold"),bg="white")    
        address_label.grid(row=4,column=0,padx=10,sticky=W)

        address_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # teacher name 

        teacher_label=Label(class_student_frame,text="teacher name ",font=("times new roman",12,"bold"),bg="white")    
        teacher_label.grid(row=4,column=2,padx=10,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # radio buttons
        
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio1,text="take photo sample",value="yes")
        radionbtn1.grid(row=6,column=0)
        
        self.var_radio2=StringVar()
        radionbtn2=ttk.Radiobutton(class_student_frame,textvariable=self.var_radio2,text="no photo sample",value="no")
        radionbtn2.grid(row=6,column=1)



        
       








        





 


        


        

        



        # right label frame 
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="student details 2",font=("times new roman",12,"bold"))
        Right_frame.place(x=670,y=10,width=620,height=500)


        # button frame 
        btn_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=0,width=615,height=70)

        save_btn=Button(btn_frame,text="save",command=self.add_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="update",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="delete",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="reset",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,text="take photo sample",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        update_photo_btn=Button(btn_frame,text="update photo sample",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=1,column=1)



        # search system 


        search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="saerch system",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=70,width=600,height=400)



        search_label=Label(search_frame,text="search by:",font=("times new roman",12,"bold"),bg="red",fg="white")    
        search_label.grid(row=0,column=0,padx=10,sticky=W)


        search_combo=ttk.Combobox(search_frame,font=("times new roman",12,"bold"),state="readonly",width=15)
        search_combo["values"]=("select","roll_no","phone_no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=4,font=("times new roman",12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)





        search_btn=Button(search_frame,text="search",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3)

        showall_btn=Button(search_frame,text="show all ",width=14,font=("times new roman",13,"bold"),bg="blue",fg="white")
        showall_btn.grid(row=0,column=4)

        # table frame 
        table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=140,width=590,height=320)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","roll","div","roll","gender","job","email","gender","dob","email","gender","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Sem")
        self.student_table.heading("id",text="Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("div",text="Div")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("job",text="Job")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="Dob")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("gender",text="gender")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")   
        self.student_table.heading("photo",text="Photo")
        self.student_table["show"]="headings"

        

        self.student_table.pack(fill=BOTH,expand=1)

    # function declare 

    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            messagebox.showinfo("sucess","Welcome ashish mundhe")    
            
    


     

   
        
        
if __name__ == "__main__":
    root=Tk()
    obj=student(root)
    root.mainloop()