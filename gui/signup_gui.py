import tkinter as tk
import os
from PIL import Image, ImageTk
from utils import app_header  # Custom header generator

class SignUpScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window setup
        ico = Image.open("../assets/images/logo.png")
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(self, photo)
        self.title("Cryptic Locker - Sign Up")
        self.minsize(900, 600)
        self.configure(bg="#337b87")
        self.state('zoomed')

        # Content Frame
        self.content_frame = tk.Frame(self, bg="#337b87")
        self.content_frame.place(relx=0.5, rely=0.15, anchor="center")

        # Header Image (instead of font label)
        header_img = app_header.generate_header()
        self.tk_header_img = ImageTk.PhotoImage(header_img)
        self.header_label = tk.Label(self.content_frame, image=self.tk_header_img, bg="#337b87")
        self.header_label.pack(pady=(0, 30))


if __name__ == "__main__":
    app = SignUpScreen()
    app.mainloop()
