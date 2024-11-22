from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox
import mysql.connector
import os

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        
        #########variables##########
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_Id = StringVar()
        self.var_std_name =StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()
        
        # Load and resize the images
        img = Image.open("college_images/Stanford.jpg")
        img = img.resize((510, 130), Image.BILINEAR)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=510, height=130)

        img1 = Image.open("college_images/iStock-182059956_18390_t12.jpg")
        img1 = img1.resize((510, 130), Image.BILINEAR)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=510, y=0, width=510, height=130)

        img2 = Image.open("college_images/u.jpg")
        img2 = img2.resize((510, 130), Image.BILINEAR)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1020, y=0, width=510, height=130)
        
        img3 = Image.open("college_images/un.jpg")
        img3 = img3.resize((1530, 710), Image.BILINEAR)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)
        
        # Title label
        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT SYSTEM", 
                          font=("times new roman", 35, "bold"), bg="Skyblue", fg="black")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Canvas for the bottom border
        border_canvas = Canvas(bg_img, width=1530, height=2, bg="darkgreen", highlightthickness=0)
        border_canvas.place(x=0, y=45)
        
        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=57, width=1500, height=600)
        
        # Left level frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", 
                                font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y=10, width=760, height=580)
        
        
        
        
        img_left = Image.open("college_images/AdobeStock_303989091.jpeg")
        img_left = img_left.resize((745, 130), Image.BILINEAR)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl_Frame = Label(Left_frame, image=self.photoimg_left)
        f_lbl_Frame.place(x=5, y=0, width=745, height=130)
        
        
        # current course
        Left_frame_current_course = LabelFrame(Left_frame, bd=0, bg="white", relief=RIDGE, text="Current Course Information", 
                                font=("times new roman", 12, "bold"))
        Left_frame_current_course.place(x=5, y=130, width=745, height=115)
        
        
        #Department
        dep_label=Label(Left_frame_current_course,text="Department :",font=("times new roman", 13, "bold"),bg="white")
        dep_label.grid(row=0,column=2,padx=10)
        
        dep_combo = ttk.Combobox(Left_frame_current_course,textvariable=self.var_dep, font=("times new roman", 13, "bold"), width=20, state="readonly")
        dep_combo["values"] = ("Select Department", "Computer Science And Engineering", "IT", "Civil", "AIML", 
                               "Data Science", "Electronic", "Electrical")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=3, padx=10, pady=5, sticky=W)
        
        #course
        course_label=Label(Left_frame_current_course,text="Course :",font=("times new roman", 13, "bold"),bg="white")
        course_label.grid(row=0,column=0,padx=10,pady=10)
        
        course_combo = ttk.Combobox(Left_frame_current_course,textvariable=self.var_course, font=("times new roman", 13, "bold"), width=20, state="readonly")
        course_combo["values"] = ("Select Course","B.tech", "B Pharma", "BBA", "BCA", "B.Com", "B.sc(agr)")
        course_combo.current(0)
        course_combo.grid(row=0, column=1, padx=10, pady=5, sticky=W)
        
        #year
        year_label=Label(Left_frame_current_course,text="Year :",font=("times new roman", 13, "bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,pady=10)
        
        year_combo = ttk.Combobox(Left_frame_current_course,textvariable=self.var_year, font=("times new roman", 13, "bold"), width=20, state="readonly")
        year_combo["values"] = ("Select Year","1st year","2nd year","3rd year","4th year")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx=10, pady=5, sticky=W)
        
        #semester
        semester_label=Label(Left_frame_current_course,text="Semester :",font=("times new roman", 13, "bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10)
        
        semester_combo = ttk.Combobox(Left_frame_current_course,textvariable=self.var_semester, font=("times new roman", 13, "bold"), width=20, state="readonly")
        semester_combo["values"] = ("Select Semester","1st semester","2nd semester")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3, padx=10, pady=5, sticky=W)
        
        
        # Class Student Information
        Left_frame_class_student_information = LabelFrame(Left_frame, bd=0, bg="white", relief=RIDGE, text="Student Information", 
                                font=("times new roman", 12, "bold"))
        Left_frame_class_student_information.place(x=5, y=245, width=745, height=305)
        
        
        #studentID
        studentID_label=Label(Left_frame_class_student_information,text="StudentID :",font=("times new roman", 13, "bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5)
        
        studentID_entry=ttk.Entry(Left_frame_class_student_information,textvariable=self.var_std_Id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)
        
        #student name
        student_name_label=Label(Left_frame_class_student_information,text="Student Name :",font=("times new roman", 13, "bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5)
        
        student_name_entry=ttk.Entry(Left_frame_class_student_information,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        #class division
        class_division_label=Label(Left_frame_class_student_information,text="Class Division :",font=("times new roman", 13, "bold"),bg="white")
        class_division_label.grid(row=1,column=0,padx=10,pady=5)
        
        class_division_entry=ttk.Entry(Left_frame_class_student_information,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
        class_division_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        #roll number
        roll_number_label=Label(Left_frame_class_student_information,text="Roll Number :",font=("times new roman", 13, "bold"),bg="white")
        roll_number_label.grid(row=1,column=2,padx=10,pady=5)
        
        roll_number_entry=ttk.Entry(Left_frame_class_student_information,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_number_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)
        
        
        #gender
        gender_label=Label(Left_frame_class_student_information,text="gender :",font=("times new roman", 13, "bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5)
        
        gender_combo = ttk.Combobox(Left_frame_class_student_information,textvariable=self.var_gender,width=18,font=("times new roman",13,"bold"), state="readonly")
        gender_combo["values"] = ("Select gender","Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=10, pady=5, sticky=W)
        
        # gender_entry=ttk.Entry(Left_frame_class_student_information,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)
        
        #DOB
        dob_label=Label(Left_frame_class_student_information,text="DOB :",font=("times new roman", 13, "bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5)
        
        dob_entry=ttk.Entry(Left_frame_class_student_information,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)
        
        
        #email
        email_label=Label(Left_frame_class_student_information,text="Email :",font=("times new roman", 13, "bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5)
        
        email_entry=ttk.Entry(Left_frame_class_student_information,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)
        
        #phone
        phone_label=Label(Left_frame_class_student_information,text="Phone :",font=("times new roman", 13, "bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5)
        
        phone_entry=ttk.Entry(Left_frame_class_student_information,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)
        
        
         #address
        address_label=Label(Left_frame_class_student_information,text="Address :",font=("times new roman", 13, "bold"),bg="white")
        address_label.grid(row=4,column=0,padx=10,pady=5)
        
        address_entry=ttk.Entry(Left_frame_class_student_information,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)
        
         # Teacher name
        teacher_name_label = Label(Left_frame_class_student_information, text="Teacher Name :", font=("times new roman", 13, "bold"), bg="white")
        teacher_name_label.grid(row=4, column=2, padx=10, pady=5)

        teacher_name_entry = ttk.Entry(Left_frame_class_student_information, textvariable=self.var_teacher, width=20, font=("times new roman", 13, "bold"))
        teacher_name_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)
        
        #radio buttons _take a photo or not
        self.var_radio1 = StringVar()
        radiobtn1=ttk.Radiobutton(Left_frame_class_student_information,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)
        
        radiobtn2=ttk.Radiobutton(Left_frame_class_student_information,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=5,column=1)
        
        
        #button frame 
        btn_frame=Frame(Left_frame_class_student_information,bd=0,relief=RAISED,bg="white")
        btn_frame.place(x=0,y=210,width=743,height=38)
        
        save_btn=Button(btn_frame,text="Save", command=self.add_data,font=("times new roman", 13, "bold"),bg="green",fg="white",width=18)
        save_btn.grid(row=0,column=0)
        
        update_btn=Button(btn_frame,text="Update",command=self.updata_date,font=("times new roman", 13, "bold"),bg="blue",fg="white",width=18)
        update_btn.grid(row=0,column=1)
        
        
        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman", 13, "bold"),bg="lightgreen",fg="white",width=18)
        delete_btn.grid(row=0,column=2)
        
        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman", 13, "bold"),bg="blue",fg="white",width=18)
        reset_btn.grid(row=0,column=3)
        
        
        #second button frame
        btn_frame2=Frame(Left_frame_class_student_information,bd=0,relief=RAISED,bg="white")
        btn_frame2.place(x=0,y=248,width=743,height=38)
        
        
        take_photo_btn=Button(btn_frame2,command=self.generate_dataset,text="Take Photo",font=("times new roman", 13, "bold"),bg="skyblue",fg="white",width=37)
        take_photo_btn.grid(row=0,column=0)
        
        Exit_photo_btn=Button(btn_frame2,text="Exit",font=("times new roman", 13, "bold"),bg="red",fg="white",width=37,command=self.exit_data)
        Exit_photo_btn.grid(row=0,column=1)
        
        
        
        
        
        
        # Right level frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", 
                                font=("times new roman", 12, "bold"))
        Right_frame.place(x=780, y=10, width=705, height=580)
        
        img_right = Image.open("college_images/KPIs-and-Agile-software-development-metrics-for-teams-1.jpg")
        img_right = img_right.resize((745, 130), Image.BILINEAR)
        self.photoimg_right = ImageTk.PhotoImage(img_right)
        f_lbl_Frame1 = Label(Right_frame, image=self.photoimg_right)
        f_lbl_Frame1.place(x=5, y=0, width=690, height=130)
        
        
        # =============Search System==============
        
        search_frame = LabelFrame(Right_frame,bd=0,bg="white",relief=RAISED,text="Search System ",font=("times new roman", 12, "bold"))
        search_frame.place(x=5,y=130,width=690,height=70)
        
        
        phone_label=Label(search_frame,text="Search By :",font=("times new roman", 13, "bold"),bg="red",fg="white")
        phone_label.grid(row=0,column=0,padx=10,pady=5)
        
        searchby_combo = ttk.Combobox(search_frame, font=("times new roman", 13, "bold"), width=15, state="readonly")
        searchby_combo["values"] = ("SelectBy","Roll_number","Phone_number")
        searchby_combo.current(0)
        searchby_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)
        
        search_roll_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_roll_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        
        search_btn=Button(search_frame,text="Search",font=("times new roman", 12, "bold"),bg="red",fg="white",width=12)
        search_btn.grid(row=0,column=3,padx=4)
        
        showall_btn=Button(search_frame,text="Show All",font=("times new roman", 12, "bold"),bg="blue",fg="white",width=12)
        showall_btn.grid(row=0,column=4,padx=4)
        
        #table frame
        
        table_frame = Frame(Right_frame,bd=2,bg="white",relief=RAISED)
        table_frame.place(x=5,y=200,width=690,height=350)
        
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,columns=("department","course","year","semester","id","name","division","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        
        self.student_table.heading("department",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("semester",text="Semester")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("division",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        
        self.student_table.column("department",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("semester",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("division",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=200)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=150)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
        
    
    
    #########function decration ##########3
    
    def add_data(self):
        if self.var_dep.get() == "select Department" or self.var_std_name.get()=="" or self.var_std_Id.get() == "" : 
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
            
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Aditya@1234",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_Id.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)
        
    ############fetch data ###########
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="Aditya@1234",database="face_recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        
        if len(data)!= 0 :
            self.student_table.delete(*self.student_table.get_children())
            for i in data :
                self.student_table.insert("", END,values=i) 
            conn.commit()
        conn.close()
    ################get cursor####################
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_Id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])
    
    #############update Data ###################
    def updata_date(self):
        if self.var_dep.get() == "select Department" or self.var_std_name.get()=="" or self.var_std_Id.get() == "" : 
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
            
        else:
            try:
                update = messagebox.askyesno("update","Do you want to update this student detail",parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Aditya@1234",database="face_recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Department=%s,course=%s,Year=%s,Semester=%s,name=%s,Devision=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_Id.get(),
                    ))
                else :
                    if not update:
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","Student Detail Update Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root) 
    
    
    
    #############delete data####################
    def delete_data(self):
        if self.var_std_Id.get()=="":
            messagebox.showerror("Error","Student id must be required !",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do you want to delete this Student Data !",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="Aditya@1234",database="face_recognition")
                    my_cursor = conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_std_Id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete :
                        return 
                conn.commit()
                self.fetch_data()
                conn.close()
                self.reset_data()
                messagebox.showinfo("Delete","Successfully Deleted A student data ",parent=self.root)           
            
            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root) 
                
        
    #################reset data############
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_year.set("Select Year"),
        self.var_course.set("Select Course"),
        self.var_semester.set("Select Semester"),
        self.var_std_name.set(""),
        self.var_div.set(""),
        self.var_roll.set(""),
        self.var_dob.set(""),
        self.var_gender.set("Select gender"),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set(""),
        self.var_std_Id.set(""),
    
    
    ################## Generate data set or take photo sample ###################
    def generate_dataset(self):
        if self.var_dep.get() == "select Department" or self.var_std_name.get()=="" or self.var_std_Id.get() == "" : 
            messagebox.showerror("Error", "All Fields are required",parent=self.root)
            
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="Aditya@1234",database="face_recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                myresult = my_cursor.fetchall()
                id=0 
                for x in myresult:
                    id+=1 
                my_cursor.execute("update student set Department=%s,course=%s,name=%s,Year=%s,Semester=%s,Devision=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_Id.get()==id+1
                    )) 
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                
                ################# Load predifiend data on face frontals from opencv #################
                
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #img convert into gray scale 
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    #scalling factor = 1.3
                    #minimum Neighbour =5
                    
                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped
                cap = cv2.VideoCapture(0)   # web camera ka 0 and other camera ka 1 and path dena hoga 
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)
                    
                    if cv2.waitKey(1)==13 or int(img_id)==100 :
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed Successfully !!")
            except Exception as es:
                messagebox.showerror("Error",f"Due TO:{str(es)}",parent=self.root)  
    
    
    def exit_data(self):
        result = messagebox.askyesno("Face Recognition System", "Do you really want to exit?", parent=self.root)
        if result:
            self.root.destroy() 
        else:
            return messagebox.showinfo("Continue", "Welcome back to Student Management System Software", parent=self.root)                            
                                        
        

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
