import customtkinter as ctk
from utils import orbitron
from gui.signup_gui import SignUpScreen
from gui.login_gui import LoginScreen
import tkinter as tk


class AuthOptions(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()

        self.after(201, lambda: self.iconbitmap("../assets/images/logo.ico"))
        self.state('zoomed')
        self.title("Cryptic Locker")
        self.minsize(900, 800)
        self.configure(fg_color="#171F55")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.content_frame = ctk.CTkFrame(self, fg_color="#171F55", corner_radius=20)
        self.content_frame.place(relx=0.5, rely=0.4, anchor="center")

        self.header_label = ctk.CTkLabel(
            self.content_frame,
            text="Cryptic Locker",
            font=orbitron.orbitron(90),
            text_color="#6C90C3"
        )

        self.header_label.pack(pady=(50, 50))


        self.buttons_frame = ctk.CTkFrame(self.content_frame, fg_color="#171F55")
        self.buttons_frame.pack(pady=(20, 10))

        self.login_button = ctk.CTkButton(
            self.buttons_frame,
            font=orbitron.orbitron(34),
            width=200,
            height=35,
            corner_radius=8,
            fg_color="#1D2763",
            border_color="#6C90C3",
            border_width=2,
            text_color="white",
            text="Login",
            command= self.login
        )
        self.login_button.pack(side="left", padx=10)

        self.sign_up_button = ctk.CTkButton(
            self.buttons_frame,
            font=orbitron.orbitron(34),
            width=200,
            height=35,
            corner_radius=8,
            fg_color="#1D2763",
            border_color="#6C90C3",
            border_width=2,
            text_color="white",
            text="Sign Up",
            command= self.signup
        )
        self.sign_up_button.pack(side="left", padx=10)

        self.import_button = ctk.CTkButton(
            self.content_frame,
            font=orbitron.orbitron(34),
            width=420,
            height=35,
            corner_radius=8,
            fg_color="#1D2763",
            border_color="#6C90C3",
            border_width=2,
            text_color="white",
            text="Import ACRL File",
        )
        self.import_button.pack(pady=(20, 10))

    def signup(self):
        self.withdraw()
        SignUpScreen(parent=self)

    def login(self):
        self.withdraw()
        LoginScreen(parent=self)


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = AuthOptions()
    app.mainloop()