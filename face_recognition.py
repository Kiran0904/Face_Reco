from tkinter import*
from tkinter import ttk
from turtle import color
from PIL import Image ,ImageTk
from tkinter import messagebox
from cv2 import COLOR_BGR2GRAY
from matplotlib.pyplot import clf
import mysql.connector
import cv2
import os
import sys
import numpy as np

    
    
class Face_Recognition: 
    def __init__(self,root):
        self.root=root 
        self.root.geometry("1750x900" )
        self.root.title("Face Recogniton System") 

        title_lbl=Label(self.root,text ="FACE_RECOGNITION",font=("times new roman ",35,"bold"),bg='white',fg='purple')
        title_lbl.place(x = 0,y = 0,width= 1750,height=45)
         
         
        #First image 
        img_top=Image.open(r"college_images\face8.jpg" ) 
        img_top =img_top.resize((750,700),Image.ANTIALIAS)
        self.photoimg_top=ImageTk.PhotoImage(img_top) 
        
        f_lbl=Label(self.root,image=self.photoimg_top)
        f_lbl.place(x =0,y=55,width=750,height=700)

      
        #Second image
        img_bottom=Image.open(r"college_images\image12.webp" ) 
        img_bottom =img_bottom.resize((950,700),Image.ANTIALIAS)
        self.photoimg_bottom=ImageTk.PhotoImage(img_bottom) 
        
        f_lbl=Label(self.root,image=self.photoimg_bottom)
        f_lbl.place(x =750,y=55,width=950,height=700)

        #button
        b1=Button(f_lbl,text="Face Recognition",cursor ="hand2",font=("times new roman ",15,"bold"),bg='darkgreen',fg='white')
        b1.place(x =350,y=650,width=200,height =40 )

    #=======Face Recognition=======
    
    def face_recog(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2,COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)
            
            coord=[]
            
            for(x,y,w,h) in features:
                cv2.rectangle(img(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
                
                conn=mysql.connector.connect(host= "localhost" ,username= "root" ,password= "Aastha@123" ,database= "student_details")  
                my_cursor=conn.cursor()
                
                
                my_cursor.execute("select Name from details where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
                
                
                my_cursor.execute("select Roll from details where Student_id=" +str(id))
                s=my_cursor.fetchone()
                s="+".join(s)
                
                my_cursor.execute("select Dep from details where Student_id=" +str(id))
                t=my_cursor.fetchone()
                t="+".join(t)
                
                
                
                
                
                if confidence>77:
                    cv2.putText(img,f"Roll:{s}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{i}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Dep:{t}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            
            return coord    

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
    
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_capture = cv2.VideoCapture(0)
        
        while True:
            
            ret, frame = video_capture.read()
            
            frame=recognize(frame,clf,faceCascade)
            
            cv2.imshow("Welcome to Face Recognition",frame)
            
            
            if cv2.waitKey(1)==13:
                break
            
        video_capture.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root =Tk()
    obj = Face_Recognition(root)
    root.mainloop()