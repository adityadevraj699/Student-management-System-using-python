from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox
from time import strftime
from datetime import datetime
import mysql.connector
import os
import csv
import numpy as np
from tkinter import filedialog

mydata = []

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        # ======================variables=========================================
        self.var_atten_id = StringVar()
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_time = StringVar()
        self.var_data = StringVar()
        self.var_attendance_status = StringVar()
        
        img = Image.open("college_images/smart-attendance.jpg")
        img = img.resize((765,200), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=765, height=200)

        img1 = Image.open("college_images/iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((765,200), Image.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=765, y=0, width=765, height=200)
        
        # background img
        img3 = Image.open("college_images/wp2551980.jpg")
        img3 = img3.resize((1530, 710), Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1530, height=710)
        
        title_lbl = Label(bg_img, text="ATTENDANCE SYSTEM", 
                          font=("times new roman", 40, "bold"), bg="Skyblue", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=57, width=1500, height=600)
        
        # Left level frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendence Details", 
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)
        
        img_left = Image.open("college_images/AdobeStock_303989091.jpeg")
        img_left = img_left.resize((745, 130), Image.BILINEAR)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_Frame = Label(Left_frame, image=self.photoimg_left)
        f_lbl_Frame.place(x=5, y=0, width=745, height=130)
        
        left_inside_frame = Frame(Left_frame, bd=0,relief=RIDGE, bg="white")
        left_inside_frame.place(x=10, y=135, width=735, height=300)
        
        #label and combobox
        #attandenceID
        attandenceID_label=Label(left_inside_frame,text="AttandenceID :",font=("times new roman", 13, "bold"),bg="white")
        attandenceID_label.grid(row=0,column=0,padx=10,pady=5)
        
        attandenceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",13,"bold"))
        attandenceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student roll
        rollLabel=Label(left_inside_frame,text="Roll :",font=("times new roman", 13, "bold"),bg="white")
        rollLabel.grid(row=0,column=2,padx=10,pady=5)
        
        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        atten_roll.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #Name
        nameLabel=Label(left_inside_frame,text="Name :",font=("times new roman", 13, "bold"),bg="white")
        nameLabel.grid(row=1,column=0,padx=10,pady=5)
        
        atten_name=ttk.Entry(left_inside_frame,textvariable=self.var_name,width=20,font=("times new roman",13,"bold"))
        atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #Department
        departmentLabel=Label(left_inside_frame,text="Department :",font=("times new roman", 13, "bold"),bg="white")
        departmentLabel.grid(row=1,column=2,padx=10,pady=5)
        
        atten_department=ttk.Entry(left_inside_frame,textvariable=self.var_department,width=20,font=("times new roman",13,"bold"))
        atten_department.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        #time
        timeLabel=Label(left_inside_frame,text="Time :",font=("times new roman", 13, "bold"),bg="white")
        timeLabel.grid(row=2,column=0,padx=10,pady=5)
        
        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_time,width=20,font=("times new roman",13,"bold"))
        atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        
        #Date
        dateLabel=Label(left_inside_frame,text="Date :",font=("times new roman", 13, "bold"),bg="white")
        dateLabel.grid(row=2,column=2,padx=10,pady=5)
        
        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_data,width=20,font=("times new roman",13,"bold"))
        atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        
        #Attandence Status
        status_label=Label(left_inside_frame,text="Attandence Status :",font=("times new roman", 13, "bold"),bg="white")
        status_label.grid(row=3,column=0,padx=10,pady=5)
        status_combo = ttk.Combobox(left_inside_frame,width=18,font=("times new roman",13,"bold"), state="readonly",textvariable=self.var_attendance_status)
        status_combo["values"] = ("Select Status","Present","Absent")
        status_combo.current(0)
        status_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)
        
        
        #button frame
        left_button_frame = Frame(Left_frame, bd=0,relief=RIDGE, bg="white")
        left_button_frame.place(x=15, y=440, width=735, height=50)
        
        import_btn = Button(left_button_frame, command=self.importCsv, text="Import CSV", font=("times new roman", 13, "bold"), bg="green", fg="white", width=17)
        import_btn.grid(row=0, column=0)
        
        exit_btn=Button(left_button_frame,text="exit",font=("times new roman", 13, "bold"),bg="red",fg="white",width=17,command=self.exit_data)
        exit_btn.grid(row=0,column=3)
        
        
        export_btn=Button(left_button_frame,text="Export CSV",font=("times new roman", 13, "bold"),bg="blue",fg="white",width=17,command=self.exportCsv)
        export_btn.grid(row=0,column=1)
        
        reset_btn=Button(left_button_frame,text="Reset",font=("times new roman", 13, "bold"),bg="orange",fg="white",width=17,command=self.reset_data)
        reset_btn.grid(row=0,column=2)
        
        
        # Right level frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attandence Details", 
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=780, y=10, width=705, height=580)
        #table frame
        
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RAISED)
        table_frame.place(x=5,y=5,width=695,height=480)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attandence"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)
        
        self.AttendanceReportTable.heading("id",text="ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attandence",text="Attandence")
        self.AttendanceReportTable["show"]="headings"
        
        
        self.AttendanceReportTable.column("id",width=80)  
        self.AttendanceReportTable.column("roll",width=150)
        self.AttendanceReportTable.column("name",width=150)
        self.AttendanceReportTable.column("department",width=150)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attandence",width=100)
        
        
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease-1>",self.get_cursor)
        
        
        # ======================fetch data =========================================================
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
                
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvreader = csv.reader(myfile, delimiter=",")
            for row in csvreader:
                mydata.append(row)
        self.fetchData(mydata)  
        
    # ================Export Csv =========================================
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found To Export",parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="open Csv", filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")), parent=self.root)  
            with open(fln, mode="w", newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    
                    exp_write.writerow(i) 
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
                
                
                
    # ======================update data=========================================
    def get_cursor(self,event=""):
        cursor_focus = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_focus)
        rows= content["values"]  
        self.var_atten_id.set(rows[0])
        self.var_roll.set(rows[1])
        self.var_name.set(rows[2])
        self.var_department.set(rows[3])
        self.var_time.set(rows[4])
        self.var_data.set(rows[5])
        self.var_attendance_status.set(rows[6]) 
        
        
    # =======================reset data ========================================
    def reset_data(self):
        self.var_atten_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_department.set("")
        self.var_time.set("")
        self.var_data.set("")
        self.var_attendance_status.set("Select Status") 
        
        
    def exit_data(self):
        result = messagebox.askyesno("Face Recognition System", "Do you really want to exit?", parent=self.root)
        if result:
            self.root.destroy()               
                      
                   
        
        

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()         