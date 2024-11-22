from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import webbrowser
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendence import Attendance


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.is_dark_mode = False  # Track theme state

        # Initialize theme colors
        self.colors = {
            "bg_light": "#f4f4f4",
            "bg_dark": "#1a1a1a",
            "button_light": "#0078d7",
            "button_dark": "#5f6368",
            "text_light": "#000000",
            "text_dark": "#ffffff",
        }

        self.current_theme = {
            "bg": self.colors["bg_light"],
            "button": self.colors["button_light"],
            "text": self.colors["text_light"],
        }

        # Background frame
        self.bg_lbl = Frame(self.root, bg=self.current_theme["bg"])
        self.bg_lbl.place(x=0, y=0, width=1530, height=790)

        # Title label
        self.title_lbl = Label(
            self.bg_lbl,
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            font=("Roboto", 30, "bold"),
            bg=self.current_theme["bg"],
            fg=self.current_theme["text"],
            pady=10,
        )
        self.title_lbl.pack(fill=X, pady=10)

        # Toggle button with icons
        self.light_icon = ImageTk.PhotoImage(Image.open("icons/light-mode.png").resize((30, 30)))
        self.dark_icon = ImageTk.PhotoImage(Image.open("icons/night-mode.png").resize((30, 30)))

        self.toggle_btn = Button(
            self.bg_lbl,
            image=self.light_icon,
            compound=LEFT,
            command=self.toggle_theme,
            font=("Roboto", 12),
            bg=self.current_theme["bg"],  # Match the background to make it appear transparent
            activebackground=self.current_theme["bg"],  # Match active background
            bd=0,
            relief="flat",
            cursor="hand2",
        )

        self.toggle_btn.place(x=1400, y=15, width=50, height=40)

        # Video background
        self.video_source = "college_images/bg_video.mp4"
        self.cap = cv2.VideoCapture(self.video_source)
        if not self.cap.isOpened():
            print("Error: Could not open video.")
        self.video_label = Label(self.bg_lbl)
        self.video_label.place(x=0, y=70, width=1530, height=720)
        self.update_video_background()

        # Buttons Section (optimized by removing the "Help Desk" button)
        self.create_buttons()

    def toggle_theme(self):
        """Switch between dark and light themes."""
        self.is_dark_mode = not self.is_dark_mode
        self.current_theme = {
            "bg": self.colors["bg_dark"] if self.is_dark_mode else self.colors["bg_light"],
            "button": self.colors["button_dark"] if self.is_dark_mode else self.colors["button_light"],
            "text": self.colors["text_dark"] if self.is_dark_mode else self.colors["text_light"],
        }
        self.toggle_btn.config(
            image=self.dark_icon if self.is_dark_mode else self.light_icon,
        )
        self.apply_theme()

    def apply_theme(self):
        """Update theme for all widgets dynamically."""
        self.bg_lbl.config(bg=self.current_theme["bg"])
        self.title_lbl.config(bg=self.current_theme["bg"], fg=self.current_theme["text"])
        self.toggle_btn.config(bg=self.current_theme["button"], fg=self.colors["text_dark"])

        for widget in self.bg_lbl.winfo_children():
            if isinstance(widget, Button) and widget != self.toggle_btn:
                widget.config(
                    bg=self.current_theme["button"],
                    fg=self.colors["text_dark"] if self.is_dark_mode else self.colors["text_light"],
                )
            elif isinstance(widget, Label) and widget != self.video_label and widget != self.title_lbl:
                widget.config(bg=self.current_theme["bg"], fg=self.current_theme["text"])

    def create_buttons(self):
        """Create buttons with images and labels."""
        button_data = [
            ("Student Details", "college_images/gettyimages-1022573162.jpg", self.student_details, 200, 200),
            ("Train Face", "college_images/Train.jpg", self.train_data, 500, 200),
            ("Developer", "college_images/Team-Management-Software-Development.jpg", self.developer_info, 800, 200),
            ("Exit", "college_images/exit.jpg", self.exit_data, 1100, 200),
        ]

        self.buttons = []  # Store buttons to update theme dynamically

        for text, img_path, command, x, y in button_data:
            img = Image.open(img_path).resize((220, 220), Image.BILINEAR)
            photo = ImageTk.PhotoImage(img)
            btn = Button(self.bg_lbl, image=photo, command=command, bg=self.current_theme["button"], bd=0, cursor="hand2")
            btn.image = photo  # Keep reference
            btn.place(x=x, y=y, width=220, height=220)
            self.buttons.append(btn)

            lbl = Button(
                self.bg_lbl,
                text=text,
                command=command,
                font=("Roboto", 12, "bold"),
                bg=self.current_theme["button"],
                fg=self.colors["text_dark"],
                cursor="hand2",
            )
            lbl.place(x=x, y=y + 240, width=220, height=40)
            self.buttons.append(lbl)

    def update_video_background(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (1530, 720))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.root.after(20, self.update_video_background)

    def __del__(self):
        """Ensure that video capture is released properly."""
        if self.cap.isOpened():
            self.cap.release()

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def developer_info(self):
        webbrowser.open("http://adityadevraj699.online")

    def exit_data(self):
        result = messagebox.askyesno("Face Recognition System", "Do you really want to exit?", parent=self.root)
        if result:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
