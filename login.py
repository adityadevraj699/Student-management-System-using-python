from tkinter import *
from tkinter import messagebox
import os
import sys

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300+500+200")
        self.root.title("Login and Logout System")

        self.username = StringVar()
        self.password = StringVar()

        # Create a frame for login form
        self.login_frame = Frame(self.root, bg="#f0f0f0", width=400, height=300)
        self.login_frame.place(x=0, y=0)

        # Title label
        title_lbl = Label(self.login_frame, text="Login", font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        title_lbl.place(x=160, y=30)

        # Username label and entry
        username_lbl = Label(self.login_frame, text="Username:", font=("Arial", 12), bg="#f0f0f0")
        username_lbl.place(x=60, y=80)
        self.username_entry = Entry(self.login_frame, textvariable=self.username, font=("Arial", 12))
        self.username_entry.place(x=160, y=80, width=180)

        # Password label and entry
        password_lbl = Label(self.login_frame, text="Password:", font=("Arial", 12), bg="#f0f0f0")
        password_lbl.place(x=60, y=120)
        self.password_entry = Entry(self.login_frame, textvariable=self.password, font=("Arial", 12), show="*")
        self.password_entry.place(x=160, y=120, width=180)

        # Login button
        login_btn = Button(self.login_frame, text="Login", command=self.login, font=("Arial", 14, "bold"), bg="#4CAF50", fg="white")
        login_btn.place(x=160, y=170, width=100)

    def login(self):
        """Handle login functionality."""
        user = self.username.get()
        pwd = self.password.get()

        # Check username and password for Teacher and Student
        if user == "Adityadevraj699" and pwd == "Aditya@1234":
            messagebox.showinfo("Login Successful", "Welcome, Teacher!")
            self.show_logout_layout("Teacher")
            self.redirect_to_main()  # Redirect to main.py after successful teacher login
        elif user == "devraj699" and pwd == "Aditya@1234":
            messagebox.showinfo("Login Successful", "Welcome, Student!")
            self.show_logout_layout("Student")
            self.redirect_to_student()  # Redirect to student.py after successful student login
        else:
            messagebox.showerror("Login Failed", "Invalid username or password!")

    def show_logout_layout(self, user_type):
        """Show the logout layout after successful login."""
        # Remove login form
        self.login_frame.destroy()

        # Create a new frame for logout layout
        self.logout_frame = Frame(self.root, bg="#f0f0f0", width=400, height=300)
        self.logout_frame.place(x=0, y=0)

        # Welcome message based on user type
        welcome_msg = f"Welcome, {user_type}!"
        welcome_lbl = Label(self.logout_frame, text=welcome_msg, font=("Arial", 20, "bold"), bg="#f0f0f0", fg="#333")
        welcome_lbl.place(x=120, y=80)

        # Logout button
        logout_btn = Button(self.logout_frame, text="Logout", command=self.logout, font=("Arial", 14, "bold"), bg="#f44336", fg="white")
        logout_btn.place(x=160, y=150, width=100)

    def logout(self):
        """Handle logout functionality."""
        # Remove logout layout
        self.logout_frame.destroy()

        # Show login layout again
        self.__init__(self.root)  # Reinitialize the app (show login form)

    def redirect_to_main(self):
        """Redirect to main.py after teacher login."""
        try:
            # Assuming the main.py is in the same directory
            os.system('python main.py')
            self.root.quit()  # Close the current tkinter window
        except Exception as e:
            messagebox.showerror("Error", f"Error while redirecting to main: {str(e)}")

    def redirect_to_student(self):
        """Redirect to student.py after student login."""
        try:
            # Assuming the student.py is in the same directory
            os.system('python student_main.py')
            self.root.quit()  # Close the current tkinter window
        except Exception as e:
            messagebox.showerror("Error", f"Error while redirecting to student: {str(e)}")


if __name__ == "__main__":
    root = Tk()
    app = LoginApp(root)
    root.mainloop()
