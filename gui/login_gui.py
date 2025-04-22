import customtkinter as ctk
from utils import orbitron
import tkinter as tk

class LoginScreen(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.after(201, lambda: self.iconbitmap("../assets/images/logo.ico"))
        self.state('zoomed')
        self.title("Cryptic Locker - Login")
        self.minsize(900, 800)
        self.configure(fg_color="#171F55")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.content_frame = ctk.CTkFrame(self, fg_color="#171F55", corner_radius=20)
        self.content_frame.place(relx=0.5, rely=0.4, anchor="center")

        # Header Label
        self.header_label = ctk.CTkLabel(
            self.content_frame,
            text="Cryptic Locker",
            font=orbitron.orbitron(90),
            text_color="#6C90C3"
        )
        self.header_label.pack(pady=(50, 50))

        self.username_label = ctk.CTkLabel(self.content_frame, text="Username:", font=orbitron.orbitron(32), text_color="#6C90C3")
        self.username_label.pack(pady=(10, 5), anchor='w', padx=(35, 0))

        self.username_entry = ctk.CTkEntry(
            self.content_frame,
            font=orbitron.orbitron(30),
            width=575,
            corner_radius=10,
            fg_color="#1D2763",
            border_color="#6C90C3",
            border_width=2,
            text_color="white",
            placeholder_text="Enter your username"
        )
        self.username_entry.pack(pady=(0, 20), anchor='w', padx=(85, 0))

        self.password_label = ctk.CTkLabel(self.content_frame, text="Password:", font=orbitron.orbitron(32),
                                           text_color="#6C90C3")
        self.password_label.pack(pady=(10, 5), anchor='w', padx=(35, 0))

        self.password_entry = ctk.CTkEntry(
            self.content_frame,
            font=orbitron.orbitron(30),
            width=575,
            corner_radius=10,
            fg_color="#1D2763",
            border_color="#6C90C3",
            border_width=2,
            text_color="white",
            placeholder_text="Enter your password",
            show="*"
        )
        self.password_entry.pack(pady=(0, 20), anchor='w', padx=(85, 0))

        self.login_button = ctk.CTkButton(
            self.content_frame,
            font=orbitron.orbitron(34),
            width=50,
            height=35,
            corner_radius=8,
            fg_color="#1D2763",
            border_color="#6C90C3",
            border_width=2,
            text_color="white",
            text="Login",

        )
        self.login_button.pack(pady=(20, 10))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = LoginScreen()
    app.mainloop()