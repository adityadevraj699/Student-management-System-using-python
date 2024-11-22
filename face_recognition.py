from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import os
import numpy as np

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Title label
        title_lbl = Label(self.root, text="Face Recognition System", 
                          font=("times new roman", 35, "bold"), bg="white", fg="green")
        title_lbl.place(x=0, y=0, width=1530, height=55)
        
        img_top = Image.open("college_images/facial_recognition_system_identification_digital_id_security_scanning_thinkstock_858236252_3x3-100740902-large.jpg")
        img_top = img_top.resize((650,700), Image.BILINEAR)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_Frame = Label(self.root, image=self.photoimg_top)
        f_lbl_Frame.place(x=0, y=55, width=650, height=700)
        
        # Background video
        self.video_source = "college_images/face_recognition.mp4"
        self.cap = cv2.VideoCapture(self.video_source)
        if not self.cap.isOpened():
            print("Error: Could not open video.")
        self.video_label = Label(self.root)
        self.video_label.place(x=650, y=55, width=880, height=700)
        self.update_video_background()
        
        b1_1 = Button(f_lbl_Frame, command=self.face_recognition, text="Face Recognition", cursor="hand2",
                      font=("times new roman", 15, "bold"), bg="darkblue", fg="skyblue")
        b1_1.place(x=230, y=620, width=180, height=40)
    
    def update_video_background(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (880, 700))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        
        # Loop video update
        self.root.after(20, self.update_video_background)
    
    def __del__(self):
        # Release the video capture when the application is closed
        if self.cap.isOpened():
            self.cap.release() 
            
    #======================attendence ===========================================================
    def mark_attendence(self, i, r, n, d):
        with open("Aditya.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            nameList = [line.split(",")[0] for line in myDataList]
        
        # Check if attendance is already marked for this combination
            if i not in nameList:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.write(f"{i},{r},{n},{d},{dtString},{d1},Present\n")
                
                    
                    
                    
                       
            
    # Face detection method
    def face_recognition(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
            
            coord = []
            
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w]) 
                confidence = int(100 * (1 - predict / 300))
                
                conn = mysql.connector.connect(host="localhost", username="root", password="Aditya@1234", database="face_recognition")
                my_cursor = conn.cursor()
                
                my_cursor.execute("SELECT Name FROM student WHERE Student_id=" + str(id))
                n = my_cursor.fetchone()
                n = "+".join(n) if n else "Unknown"
                # print("n : ",n)
                
                my_cursor.execute("SELECT Roll FROM student WHERE Student_id=" + str(id))
                r = my_cursor.fetchone()
                r = "+".join(r) if r else "Unknown"
                # print("r:",r)
                
                my_cursor.execute("SELECT Department FROM student WHERE Student_id=" + str(id))
                d = my_cursor.fetchone()
                d = "+".join(d) if d else "Unknown"
                # print("d :",d)
                # print("Predict:", predict, "Confidence:", confidence)
                my_cursor.execute("SELECT Student_id FROM student WHERE Student_id=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(str(element) for element in i) if i else "Unknown"

                # print("Id :",i)
                self.mark_attendence(i,r,n,d)

                
                if predict >= 75 or confidence >= 75:
                    # cv2.putText(img, f"Student_ID: {i}", (x-70, y - 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                    cv2.putText(img, f"Roll: {r}", (x-70, y - 75), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
                    cv2.putText(img, f"Name: {n}", (x-70, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3) 
                    cv2.putText(img, f"Department: {d}", (x-70, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3) 
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord
                
        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        
        video_cap = cv2.VideoCapture(0)
        
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to Face Recognition", img) 
            
            if cv2.waitKey(1) == 13:
                break
        
        video_cap.release()
        cv2.destroyAllWindows() 

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()   