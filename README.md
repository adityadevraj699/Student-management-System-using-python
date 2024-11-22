# Student Management System and Automatic Attendance Marking  
### Using Python, Haar Cascade for Object Detection, LBPH OpenCV for Face Recognition, and MySQL Database  

## 📋 Project Overview  
This project aims to simplify and automate the attendance process for educational institutions. Using facial recognition technology, the system identifies and marks attendance automatically, ensuring accuracy and reducing manual effort. It also includes a student management system to maintain and manage student data effectively.  

## ✨ Features  
- **Facial Recognition**:  
   - Uses Haar Cascade for face detection.  
   - Leverages LBPH (Local Binary Patterns Histograms) from OpenCV for facial recognition.  

- **Automatic Attendance Marking**:  
   - Captures the image in real-time using a webcam.  
   - Identifies students from a pre-trained dataset and marks attendance in the database.  

- **Student Management System**:  
   - Add, update, and delete student details.  
   - View student profiles and attendance records.  

- **Database Integration**:  
   - MySQL is used to store student details and attendance records.  
   - Secure and efficient database operations.  

## 🛠️ Technologies Used  
- **Programming Language**: Python  
- **Libraries/Modules**:  
  - OpenCV  
  - MySQL Connector for Python  
  - Tkinter (for GUI)  

- **Database**: MySQL  
- **Algorithms**: Haar Cascade, LBPH  

## ⚙️ Installation  

### Prerequisites  
1. Python 3.x installed on your system.  
2. MySQL server installed and configured.  
3. Webcam or camera for face detection and recognition.  

### Steps  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/adityadevraj699/Student-management-System-using-python.git
   ```  
2. Navigate to the project directory:  
   ```bash  
   cd Student-Management-Attendance  
   ```  
3. Install the required Python libraries:  
   ```bash  
   pip install opencv-python numpy mysql-connector-python  
   ```  
4. Set up the database:  
   - Import the provided `student_management.sql` file into your MySQL server.  
   - Update the database connection settings in the code with your MySQL credentials.  

5. Run the project:  
   ```bash  
   python main.py  
   ```  

## 🖥️ How It Works  
1. **Training the Model**:  
   - The system captures images of students and saves them in a dataset folder.  
   - Train the LBPH face recognizer with the dataset to recognize faces.  

2. **Real-Time Detection and Attendance**:  
   - The system uses Haar Cascade to detect faces in a webcam feed.  
   - LBPH recognizer identifies the student based on the trained dataset.  
   - Attendance is automatically marked in the database with the date and time.  

3. **Student Management**:  
   - A graphical user interface (GUI) enables administrators to add, edit, or remove student details.  
   - Attendance records can be viewed for any specific date.  



## 🎯 Future Enhancements  
- Implement email notifications for attendance updates.  
- Enhance recognition accuracy with advanced deep learning models.  
- Add mobile app integration for real-time monitoring.  

## 🤝 Contributions  
Contributions are welcome! If you'd like to contribute, please fork the repository and create a pull request.  

## 📄 License  
This project is licensed under the MIT License. See the `LICENSE` file for details.  

## 📧 Contact  
For any queries or support, please reach out:  
- **Email**: adevraj934@gmail.com
- **GitHub**: [yourusername](https://github.com/adityadevraj699)  

---  

Let me know if you'd like to customize this further!
