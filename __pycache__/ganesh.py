from tkinter import *
from tkinter import ttk
from PIL import Image , ImageTk
#from student import Student


class Face_Recognition_system:
    def __init__(self,root):


         self.root=root
         self.root.geometry("1366x768+0+0")
         self.root.title("Face_Recognition_system")
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

#backgroung img
         
         img3=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\background.jpg")
         img3=img3.resize((1366,768),Image.ANTIALIAS)
         self.photoimg3=ImageTk.PhotoImage(img3)

         bg_lbl=Label(self.root,image= self.photoimg3)
         bg_lbl.place(x=0,y=130,width=1366,height=710)

         title_lbl=Label(bg_lbl,text="FACE RECOGNITION SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
         title_lbl.place(x=0,y=0,width=1366,height=45)

#students button
         img4=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\ABT8233C001DCB7E9E41A8FAC2A654A085D1C6C2639D7174C81C18BD9CAFC360AFD.jpg")
         img4=img4.resize((1366,768),Image.ANTIALIAS)
         self.photoimg4=ImageTk.PhotoImage(img4)

         b1=Button(bg_lbl,image=self.photoimg4,command=self.student_details,cursor="hand2")
         b1.place(x=100,y=80,width=220,height=220)

         b1_1=Button(bg_lbl,text="students details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
         b1_1.place(x=100,y=275,width=220,height=40)

#decet face button
         img5=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img05.jpg")
         img5=img5.resize((1366,768),Image.ANTIALIAS)
         self.photoimg5=ImageTk.PhotoImage(img5)

         b1=Button(bg_lbl,image=self.photoimg5,cursor="hand2")
         b1.place(x=400,y=80,width=220,height=220)

         b1_1=Button(bg_lbl,text="Face Detector",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
         b1_1.place(x=400,y=275,width=220,height=40)

#attendance face button
         img6=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\attendance.png")
         img6=img6.resize((1366,768),Image.ANTIALIAS)
         self.photoimg6=ImageTk.PhotoImage(img6)

         b1=Button(bg_lbl,image=self.photoimg6,cursor="hand2")
         b1.place(x=700,y=80,width=220,height=220)

         b1_1=Button(bg_lbl,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
         b1_1.place(x=700,y=275,width=220,height=40)

#help face button
         img7=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img05.jpg")
         img7=img7.resize((1366,768),Image.ANTIALIAS)
         self.photoimg7=ImageTk.PhotoImage(img7)

         b1=Button(bg_lbl,image=self.photoimg7,cursor="hand2")
         b1.place(x=1000,y=80,width=220,height=220)

         b1_1=Button(bg_lbl,text="HELP",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
         b1_1.place(x=1000,y=275,width=220,height=40)

#Train face button
         img8=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img05.jpg")
         img8=img8.resize((1366,768),Image.ANTIALIAS)
         self.photoimg8=ImageTk.PhotoImage(img8)

         b1=Button(bg_lbl,image=self.photoimg8,cursor="hand2")
         b1.place(x=100,y=325,width=220,height=220)

         b1_1=Button(bg_lbl,text="Train Face",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
         b1_1.place(x=100,y=520,width=220,height=40)

#photos face button

         img9=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img05.jpg")
         img9=img8.resize((1366,768),Image.ANTIALIAS)
         self.photoimg9=ImageTk.PhotoImage(img9)

         b1=Button(bg_lbl,image=self.photoimg9,cursor="hand2")
         b1.place(x=400,y=325,width=220,height=220)

         b1_1=Button(bg_lbl,text="Photos Face ",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
         b1_1.place(x=400,y=520,width=220,height=40)

#Developer face button
         img11=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img05.jpg")
         img11=img11.resize((1366,768),Image.ANTIALIAS)
         self.photoimg11=ImageTk.PhotoImage(img11)

         b1=Button(bg_lbl,image=self.photoimg11,cursor="hand2")
         b1.place(x=700,y=325,width=220,height=220)

         b1_1=Button(bg_lbl,text=" Developer ",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
         b1_1.place(x=700,y=520,width=220,height=40)

#Exit button
         img11=Image.open(r"C:\Users\wn10\Desktop\face_recognisation_system\Camera Roll\img05.jpg")
         img11=img11.resize((1366,768),Image.ANTIALIAS)
         self.photoimg11=ImageTk.PhotoImage(img11)

         b1=Button(bg_lbl,image=self.photoimg11,cursor="hand2")
         b1.place(x=1000,y=325,width=220,height=220)

         b1_1=Button(bg_lbl,text="EXIT ",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
         b1_1.place(x=1000,y=520,width=220,height=40)

    #===========functions buttons============
         


    def student_details(self):
        pass
    
        
        self.new_window=Toplevel(self.root)
        self.aap=Student(self.new_window)




















if __name__=="__main__":
    root=Tk()
    obj= Face_Recognition_system(root)
    root.mainloop()
