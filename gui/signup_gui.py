import tkinter as tk
import os
from utils import font_loader
from PIL import Image, ImageTk

class SignUpScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        ico = Image.open("../assets/images/logo.png")
        photo = ImageTk.PhotoImage(ico)
        self.wm_iconphoto(self, photo)
        self.title("Cryptic Locker - Sign Up")
        self.minsize(900, 600)
        self.configure(bg="#337b87")
        self.state('zoomed')

        self.register_custom_font()

        self.content_frame = tk.Frame(self, bg="#337b87")
        self.content_frame.pack(expand=True)

        self.title_label = tk.Label(
            self.content_frame,
            text="CRYPTIC LOCKER",
            font=("Bungee Shade", 60),
            fg="#f1f5f4",
            bg="#337b87"
        )
        self.title_label.pack(pady=30)

    def register_custom_font(self):
        font_path = os.path.abspath(os.path.join("..", "assets", "fonts", "BungeeShade-Regular.ttf"))
        if os.path.exists(font_path):
            added = font_loader.loadfont(font_path)
            if added:
                print(f"Custom font loaded from: {font_path}")
            else:
                print("Failed to load custom font.")
        else:
            print(f"Font file not found at: {font_path}")

if __name__ == "__main__":
    app = SignUpScreen()
    app.mainloop()
