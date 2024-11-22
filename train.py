from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        # Theme tracking and colors
        self.is_dark_mode = False  # Track the theme state
        self.colors = {
            "bg_light": "#f9f9f9",
            "bg_dark": "#1e1e1e",
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
        self.bg_frame = Frame(self.root, bg=self.current_theme["bg"])
        self.bg_frame.place(x=0, y=0, width=1530, height=790)

        # Title label
        self.title_lbl = Label(
            self.bg_frame,
            text="TRAIN DATA SET",
            font=("Roboto", 35, "bold"),
            bg=self.current_theme["bg"],
            fg=self.current_theme["text"],
        )
        self.title_lbl.place(x=0, y=0, width=1530, height=50)

        # Toggle button with icons
        self.light_icon = ImageTk.PhotoImage(Image.open("icons/light-mode.png").resize((30, 30)))
        self.dark_icon = ImageTk.PhotoImage(Image.open("icons/night-mode.png").resize((30, 30)))
        self.toggle_btn = Button(
            self.bg_frame,
            image=self.light_icon,
            compound=LEFT,
            command=self.toggle_theme,
            bg=self.current_theme["bg"],
            bd=0,
            relief="flat",
            cursor="hand2",
        )
        self.toggle_btn.place(x=1450, y=10, width=50, height=30)

        # Top image
        img_top = Image.open("college_images/di.jpg").resize((1530, 325), Image.BILINEAR)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl_Frame = Label(self.bg_frame, image=self.photoimg_top, bg=self.current_theme["bg"])
        f_lbl_Frame.place(x=0, y=50, width=1530, height=225)

        # Train button
        self.train_btn = Button(
            self.bg_frame,
            text="TRAIN DATA",
            command=self.train_classifier,
            font=("Roboto", 30, "bold"),
            bg=self.current_theme["button"],
            fg=self.colors["text_dark"],
            cursor="hand2",
        )
        self.train_btn.place(x=0, y=280, width=1530, height=60)

        # Background video
        self.video_source = "college_images/bg_video1.mp4"
        self.cap = cv2.VideoCapture(self.video_source)
        if not self.cap.isOpened():
            print("Error: Could not open video.")
        self.video_label = Label(self.bg_frame, bg=self.current_theme["bg"])
        self.video_label.place(x=0, y=350, width=1530, height=430)
        self.update_video_background()

        # Handle window close
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def toggle_theme(self):
        """Switch between dark and light themes."""
        self.is_dark_mode = not self.is_dark_mode
        self.current_theme = {
            "bg": self.colors["bg_dark"] if self.is_dark_mode else self.colors["bg_light"],
            "button": self.colors["button_dark"] if self.is_dark_mode else self.colors["button_light"],
            "text": self.colors["text_dark"] if self.is_dark_mode else self.colors["text_light"],
        }
        self.apply_theme()
        self.toggle_btn.config(image=self.dark_icon if self.is_dark_mode else self.light_icon)

    def apply_theme(self):
        """Apply theme changes to all widgets."""
        self.bg_frame.config(bg=self.current_theme["bg"])
        self.title_lbl.config(bg=self.current_theme["bg"], fg=self.current_theme["text"])
        self.train_btn.config(bg=self.current_theme["button"], fg=self.colors["text_dark"])
        self.video_label.config(bg=self.current_theme["bg"])

    def train_classifier(self):
        """Train classifier using available images."""
        data_dir = "data"  # Path for the data
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces, ids = [], []

        for image in path:
            img = Image.open(image).convert('L')  # Gray scale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training", imageNp)
            if cv2.waitKey(1) == 13:  # Exit training on Enter key
                break

        if not faces or not ids:
            messagebox.showerror("Error", "No training images found in the directory.", parent=self.root)
            return

        try:
            ids = np.array(ids)
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.train(faces, ids)
            clf.write("classifier.xml")
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Training datasets Successfully!!", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Training failed: {str(e)}", parent=self.root)

    def update_video_background(self):
        """Play video in the background."""
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.resize(frame, (1530, 430))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.video_label.imgtk = imgtk
            self.video_label.configure(image=imgtk)
        else:
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.root.after(20, self.update_video_background)

    def on_closing(self):
        """Handle cleanup on window close."""
        if self.cap.isOpened():
            self.cap.release()
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
