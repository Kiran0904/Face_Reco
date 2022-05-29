from tkinter import*
from tkinter import ttk
from PIL import Image ,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2



class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1750x900")
        self.root.title("face Recogniton System")
        
        
        # =========variables============
        
        self.var_Dep=StringVar() 
        self.var_course=StringVar()
        self.var_Year=StringVar()
        self.var_sem=StringVar() 
        self.var_Student_id=StringVar()
        self.var_Name=StringVar()
        self.var_Roll=StringVar()
        self.var_Gender=StringVar()
        self.var_Email=StringVar()
        self.var_phone=StringVar()
        
        
        
        # first imag
        img= Image.open( r"college_images\student3.jpg")
        img =img.resize((500,130),Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
    
        f_lbl= Label (self.root , image = self.photoimg )
        f_lbl.place ( x = 0 , y = 0 , width =500 , height =130 )
        
        
        #second image
        img1= Image.open (r"college_images\student1.jpg")
        img1 = img1.resize ( ( 500 , 130 ) , Image.ANTIALIAS )
        self.photoimg1 =ImageTk.PhotoImage ( img1 )
     
        f_lbl = Label ( self.root , image = self.photoimg1 )
        f_lbl.place ( x = 500, y = 0 , width = 550 , height = 130 )

        # third imag
        img2=Image.open ( r"college_images\student2.jpg")
        img2 = img2.resize ( ( 500,130 ) , Image.ANTIALIAS )
        self.photoimg2 = ImageTk.PhotoImage ( img2 )
        
        f_lbl = Label ( self.root , image = self.photoimg2 )
        f_lbl.place ( x = 1000, y = 0 , width =550 , height =130 )  
       
        
        #bg image
        img3=Image.open(r"college_images\image19.jpg")
        img3=img3.resize((1700,900),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        bg_img=Label(self.root,image =self.photoimg3) 
        bg_img.place(x=0,y=130, width = 1700,height=900)  
        
        title_lbl=Label(bg_img,text ="STUDENT DETAILS ",font=("times new roman",35,"bold"),bg='white',fg='purple')
        title_lbl.place(x=0,y=0,width=1700,height=45)
       
        main_frame=Frame( bg_img ,bd=2,bg='white')
        main_frame.place(x= 5 ,y = 55,width=1700, height=600)
        
        
        #left frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",30,'bold'))
        Left_frame.place(x=10,y=10,width=750 ,height=580)       
       
        
        img_left=Image.open( r"college_images\student4.jpg")
        img_left=img_left.resize(( 750,130 ),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)
        
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place(x =5,y =0 ,width=750,height =130)
        
        # Current course
        Current_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Course Details",font=("times new roman",30,'bold'))
        Current_frame.place(x=5,y=135,width=750 ,height=150) 
       
        #Department
        dep_label = Label (Current_frame,text="Department",font=("times new roman",12,"bold"),bg='white')
        dep_label.grid ( row=0 , column=0 )
        
        dep_combo=ttk.Combobox(Current_frame,textvariable=self.var_Dep,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"]=("Select Department","Computer Science","IT","Civil","Mechnical", "Electrical")
        dep_combo.current(0)
        dep_combo.grid ( row=0 , column=1,padx= 2,pady= 10)
        
        
        # Course 
        course_label=Label(Current_frame,text ="Course",font=( " times new roman ", 13 ," bold" ),bg ='white')
        course_label.grid(row=0,column=2,padx=10,sticky=W) 
        
        course_combo=ttk.Combobox(Current_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),state="readonly",width='20')
        course_combo["values"]=("Select Course","DS","SE","EE","BE","OOPS")
        course_combo.current(0) 
        course_combo.grid(row=0,column=3,padx= 2,pady=10,sticky=W)
        
        
        # Year 
        year_label =Label(Current_frame , text ="Year",font=("times new roman " , 13 , " bold " ) ,bg ='white')
        year_label.grid (row = 1 , column = 0 , padx = 10 , sticky = W )
        
        year_combo =ttk.Combobox ( Current_frame,textvariable=self.var_Year , font= (" times new roman " , 13 , " bold " ) , state = " readonly " , width="20" )
        year_combo["values"] =("Select Year ","2021-22","2022-23 ","2023-24 ","2024-25 ")
        year_combo.current ( 0 )
        year_combo.grid ( row = 1 , column = 1 , padx = 2 , pady = 10 , sticky = W )
       
       
        #Semester 
        semester_label = Label( Current_frame , text = "Semester" , font = ( " times new roman " , 13 , " bold " ) , bg = "white")
        semester_label.grid ( row = 1 , column = 2 , padx = 10 , sticky = W ) 
        
        semester_combo=ttk.Combobox ( Current_frame,textvariable=self.var_sem , font = ( " times new roman " , 13 , " bold " ) , state = "readonly")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2","Semester-3","Semester-4") 
        semester_combo.current ( 0 ) 
        semester_combo.grid ( row = 1 , column = 3 , padx = 2 , pady = 10 , sticky = W )
       
       
        # Class Student Information
        Student_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Student Information",font=("times new roman",30,'bold'))
        Student_frame.place(x=5,y=270,width=750 ,height=300) 
        
        
        #Student ID
        ID_label = Label( Student_frame , text = " STUDENT ID " , font = ( " times new roman " , 13 , " bold " ) , bg = "white")
        ID_label.grid ( row = 0 , column =0, padx = 10 , sticky = W ) 
        
        StudentID_entry=ttk.Entry(Student_frame,textvariable=self.var_Student_id,width=20,font=("times new roman",13,"bold"))
        StudentID_entry.grid(row=0,column=1,padx=10,sticky=W)
        
        
        #Student Name
        Name_label = Label( Student_frame , text = " Student Name" , font = ( " times new roman " , 13 , " bold " ),bg ="white")
        Name_label.grid ( row = 0 , column =2, padx = 10 ,pady=5 ,sticky = W ) 
        
        StudentName_entry=ttk.Entry(Student_frame,textvariable=self.var_Name,width=20,font=("times new roman",13,"bold"))
        StudentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        
        #Student Email
        Email_label = Label( Student_frame , text = "Email ID" , font = ( " times new roman " , 13 , " bold " ),bg ="white")
        Email_label.grid ( row = 1 , column =0, padx = 10 ,pady=5 ,sticky = W ) 
        
        StudentEmail_entry=ttk.Entry(Student_frame,textvariable=self.var_Email,width=20,font=("times new roman",13,"bold"))
        StudentEmail_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
       
        #Student Roll number
        Roll_label = Label( Student_frame , text = "Roll No." , font = ( " times new roman " , 13 , " bold " ),bg ="white")
        Roll_label.grid ( row = 1 , column =2, padx = 10 ,pady=5 ,sticky = W ) 
        
        StudentRoll_entry=ttk.Entry(Student_frame,textvariable=self.var_Roll,width=20,font=("times new roman",13,"bold"))
        StudentRoll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
       
       
        #Student Gender
        Gender_label = Label( Student_frame , text = " Gender " , font = ( " times new roman " , 13 , " bold " ) , bg = "white")
        Gender_label.grid ( row = 2 , column = 0 , padx = 10 , sticky = W ) 
        
        Gender_combo=ttk.Combobox ( Student_frame ,textvariable=self.var_Gender, font = ( " times new roman " , 13 , " bold " ) , state = "readonly")
        Gender_combo["values"]=("Select Gender","Female","Male") 
        Gender_combo.current ( 0 ) 
        Gender_combo.grid ( row = 2 , column = 1, padx = 2 , pady = 10 , sticky = W )
        
        
        #Student Phone  number
        Phone_label = Label( Student_frame , text = "Phone No." , font = ( " times new roman " , 13 , " bold " ),bg ="white")
        Phone_label.grid ( row = 2 , column =2, padx = 10 ,pady=5 ,sticky = W ) 
        
        StudentPhone_entry=ttk.Entry(Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        StudentPhone_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        # radio Buttons
        self.var_radio1=StringVar()
        radionbtn1 = ttk.Radiobutton(Student_frame,variable=self.var_radio1 , text = " Take Photo Sample " ,value = " Yes " ) 
        radionbtn1.grid ( row =4, column = 0 ) 
        
        
        radionbtn2 = ttk . Radiobutton (Student_frame,variable=self.var_radio1 , text = " No Photo Sample " , value = "No " )
        radionbtn2.grid ( row=4 , column = 1 )
        
        
        #bbuttons frame 
        btn_frame = Frame (Student_frame , bd = 2 , relief = RIDGE ,bg='white') 
        btn_frame.place ( x = 0 , y = 140, width = 710 , height = 35 )
        
        save_btn=Button(btn_frame , text = "Save",command=self.add_data,width =13,font=("times new roman",13,"bold"),bg ='blue',fg='white')
        save_btn.grid ( row = 0 , column = 0 ,padx=3) 
        
        update_btn=Button(btn_frame , text = " Update",command=self.update_data,width = 13,font =(" times new roman " , 13 , " bold " ) ,bg ='blue',fg='white' )
        update_btn.grid ( row = 0 , column = 1,padx=3 ) 
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=13,font =("times new roman",13,"bold"),bg ='blue',fg='white')  
        delete_btn.grid(row =0,column=2,padx=3)
    
        reset_btn=Button(btn_frame , text = " Reset",command=self.reset_data,width = 13,font =(" times new roman " , 13 , " bold " ) ,bg ='blue',fg='white' )
        reset_btn.grid ( row = 0 , column = 3,padx=3 ) 
        
         
         
        btn_frame1 = Frame (Student_frame , bd = 2 , relief = RIDGE ,bg='white') 
        btn_frame1.place ( x = 0 , y = 180, width = 710 , height = 35) 
        
        
        take_photo_btn=Button(btn_frame1,command=self.generate_dataset ,text="Take Photo Sample",width=15,font=("times new roman",13,"bold"))
        take_photo_btn.grid ( row =1, column = 1,padx=6)
        
        update_photo_btn=Button(btn_frame1 ,text="Update Photo Sample",command=self.generate_dataset,width=15,font=("times new roman",13,"bold"))
        update_photo_btn.grid ( row = 1, column = 2 ,padx=6)
        
    
        #Right frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Informations",font=("times new roman",30,'bold'))
        Right_frame.place(x=775,y=10,width=720 ,height=580)       
       
        img_right =Image.open(r"college_images\image19.jpg")
        img_right =img_right.resize((720,130 ),Image.ANTIALIAS) 
        self.photoimg_right=ImageTk.PhotoImage(img_right) 
        
        f_lbl=Label(Right_frame,image=self.photoimg_right) 
        f_lbl.place(x =5,y=0,width=720,height=130)
        
         
        # ======= Search System ==== 
        Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",20))
        Search_frame.place (x=5,y=135,width=710,height=80)
        
        #Search Bar
        Search_label=Label(Search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="purple")
        Search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W) 
        
        
        Search_combo=ttk.Combobox(Search_frame,font=("times new roman",15,"bold"),state="readonly",width=15)
        Search_combo["values"]=("Select","Roll no.","Phone no") 
        Search_combo.current(0) 
        Search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        Search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
        Search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
       
        search_btn=Button(Search_frame,text="Search",width=12,font=("times new roman",10,"bold"),bg ='blue',fg='white')
        search_btn.grid(row =0,column=3,padx=3)
        
        show_btn=Button(Search_frame,text="Show All",width =12,font=("times new roman",10,"bold"),bg ='blue',fg='white')
        show_btn.grid(row=0,column=4,padx=3)
    
       
        # === ===== table frame == 
        table_frame= Frame (Right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=220,width=710,height=300)
        
        
        scroll_x=ttk.Scrollbar( table_frame ,orient=HORIZONTAL) 
        scroll_y=ttk.Scrollbar( table_frame,orient=VERTICAL )
        
        
        self.student_table=ttk.Treeview(table_frame,column=(" Dep " , " course " , " Year " , " sem " , " Student_id " , " Name " , " Roll " , " Email " , " Gender " , " phone "," PhotoSample "),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X) 
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config ( command = self.student_table.xview ) 
        scroll_y.config ( command = self.student_table.yview )
        
        self.student_table.heading ( " Dep " , text = " Department " ) 
        self.student_table.heading ( " course " , text = " Course " ) 
        self.student_table.heading ( " Year " , text = " Year " ) 
        self.student_table.heading ( " sem " , text = " Semester " ) 
        self.student_table.heading ( " Student_id " , text = " StudentId " )  
        self.student_table.heading ( " Name " , text = " Name " ) 
        self.student_table.heading ( " Email " , text = " Email " ) 
        self.student_table.heading ( " Roll " , text = " Roll " )
        self.student_table.heading ( " Gender " , text = " Gender" ) 
        self.student_table.heading ( " phone " , text = " Phone " )
        self.student_table.heading ( " PhotoSample " , text = " PhotoSampleStatus " )
        
        self.student_table["show"]="headings" 
        
        
        self.student_table.column ( " Dep " , width = 100 ) 
        self.student_table.column ( " course " , width = 100 ) 
        self.student_table.column ( " Year " , width = 100 ) 
        self.student_table.column ( " sem " , width = 100 ) 
        self.student_table.column ( " Student_id " , width = 100 ) 
        self.student_table.column ( " Name " , width = 100 ) 
        self.student_table.column ( " Roll " , width = 100 ) 
        self.student_table.column ( " Gender " , width = 100 )  
        self.student_table.column ( " Email " , width = 100 ) 
        self.student_table.column ( " phone " , width = 100 ) 
        self.student_table.column ( " PhotoSample " , width = 150 )
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #=========function declaration===============
    
    def add_data(self):
        if self.var_Dep.get()=="Select Department"or self.var_course.get()=="" or self.var_Name.get()=="" :
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
                try:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Aastha@123",database='student_details')  
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    
                                                                                    self.var_Dep.get(),
                                                                                    self.var_course.get(),
                                                                                    self.var_Year.get(),
                                                                                    self.var_sem.get(),
                                                                                    self.var_Student_id.get(),
                                                                                    self.var_Name.get(),
                                                                                    self.var_Roll.get(),
                                                                                    self.var_Gender.get(),
                                                                                    self.var_Email.get(),
                                                                                    self.var_phone.get(),
                                                                                    self.var_radio1.get()
                                                                
                                                            
                                                                                    
                                                                            ))
                    
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","Student details are added successfully",parent=self.root)
                except Exception as es:
                    messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    
    
    # ============== fetch data ================ 
    
    def fetch_data(self): 
        conn=mysql.connector.connect(host="localhost", username="root",password="Aastha@123", database='student_details')
        my_cursor=conn.cursor() 
        my_cursor.execute(" select* from details ") 
        data=my_cursor.fetchall()
         
        if len(data)!=0: 
            self.student_table.delete(*self.student_table.get_children())
            for i in data: 
                self.student_table.insert ("",END,values=i)
            conn.commit ()
        conn.close()  
        
        
    #===============GET CURSOR =========
    def get_cursor(self,event=""):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]
       
       
       self.var_Dep.set(data[0]),
       self.var_course.set(data[1]),
       self.var_Year.set(data[2]),
       self.var_sem.set(data[3]),
       self.var_Student_id.set(data[4]),
       self.var_Name.set(data[5]),
       self.var_Roll.set(data[6]),
       self.var_Gender.set(data[7]),
       self.var_Email.set(data[8]),
       self.var_phone.set(data[9]),
       self.var_radio1.set(data[10])
    
       
     
    #UPDATE
    def update_data(self):
        if self.var_Dep.get()=="Select Department"or self.var_course.get()=="" or self.var_Name.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                Update=messagebox.askyesno("Update","Do you want to update this student details",parent=self.root)
                if Update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Aastha@123",database='student_details')  
                    my_cursor=conn.cursor()
                    my_cursor.execute("update details set Dep=%s, course=%s, Year=%s, sem=%s, Name=%s, Roll=%s, Gender=%s, Email=%s, phone=%s, PhotoSample=%s where Student_id=%s",(
                                    
                                                                                                                                            self.var_Dep.get(),
                                                                                                                                            self.var_course.get(),
                                                                                                                                            self.var_Year.get(),
                                                                                                                                            self.var_sem.get(),
                                                                                                                                            self.var_Name.get(),
                                                                                                                                            self.var_Roll.get(),
                                                                                                                                            self.var_Gender.get(),
                                                                                                                                            self.var_Email.get(),
                                                                                                                                            self.var_phone.get(),
                                                                                                                                            self.var_radio1.get(),
                                                                                                                                            self.var_Student_id.get()
                                                                                                                                                                    
                                    
                                                                                                                                ))  
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)    
                conn.commit()  
                self.fetch_data()  
                conn.close()
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   
                
                
    #delete         
    def delete_data(self):
        if self.val_Student_id.get()=="": 
            messagebox.showerror("Error","Student id must be required",parent=self.root) 
        else: 
            try : 
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student",parent=self.root) 
                if delete>0: 
                    conn = mysql.connector.connect(host="localhost",username="root",password="Aastha@123",database='student_details') 
                    my_cursor=conn.cursor() 
                    sql="delete from details where Student_id=%s" 
                    val=(self.val_Student_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return    
                conn.commit()  
                self.fetch_data()  
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)   
          
       
    #reset
    def reset_data(self):
       self.var_Dep.set("Select Department")
       self.var_course.set("Select Course")
       self.var_Year.set("Select Year")
       self.var_sem.set("Select Semester")
       self.var_Student_id.set("")
       self.var_Name.set("")
       self.var_Roll.set("")
       self.var_Gender.set("")
       self.var_Email.set("")
       self.var_phone.set("")
       self.var_radio1.set("")
        
    
    
    # Generate data set or Take photo Samples
     
    def generate_dataset(self):
        if self.var_Dep.get()=="Select Department"or self.var_course.get()=="" or self.var_Name.get()=="":
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Aastha@123",database='student_details')  
                my_cursor=conn.cursor()
                my_cursor.execute(" select* from details ")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update details set Dep=%s, course=%s, Year=%s, sem=%s, Name=%s, Roll=%s, Gender=%s, Email=%s, phone=%s, PhotoSample=%s where Student_id=%s",(
                                    
                                                                                                                                            self.var_Dep.get(),
                                                                                                                                            self.var_course.get(),
                                                                                                                                            self.var_Year.get(),
                                                                                                                                            self.var_sem.get(),
                                                                                                                                            self.var_Name.get(),
                                                                                                                                            self.var_Roll.get(),
                                                                                                                                            self.var_Gender.get(),
                                                                                                                                            self.var_Email.get(),
                                                                                                                                            self.var_phone.get(),
                                                                                                                                            self.var_radio1.get(),
                                                                                                                                            self.var_Student_id.get()==id+1
                                    
                            
                                    
                                                                                                                                ))      
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()    
                
                #===load predefined data on face frontals from opencv=====
                
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #Minimum Neighbor=5
                    
                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                 
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret , my_frame=cap.read()   
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                    face=cv2.resize(face_cropped(my_frame),(450,450)) 
                    face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                    file_name_path="data/user." +str(id)+"."+str(img_id)+".jpg"
                    cv2.imwrite(file_name_path)
                    cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                    cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows() 
                
                messagebox.showinfo("Result","Generating data sets completed!!!") 
                
            except EXCEPTION as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)          
       
 
    
    
if __name__ == "__main__":
    root =Tk()
    obj = Student(root)
    root.mainloop()
    