import customtkinter as ctk
import tkinter as tk
from utils import orbitron
from backend.login import Login
from gui.login_TOTP_gui import LoginTOTPScreen

class LoginScreen(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.after(201, lambda: self.iconbitmap("../assets/images/logo.ico"))
        self.state('zoomed')
        self.title("Cryptic Locker - Login")
        self.minsize(900, 800)
        self.configure(fg_color="#171F55")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.content_frame = ctk.CTkFrame(self, fg_color="#171F55", corner_radius=20)
        self.content_frame.place(relx=0.5, rely=0.4, anchor="center")
        self.bind("<Escape>", self.go_back)
        self.bind('<Return>', self.submit)


        self.back_button = ctk.CTkButton(
            self,
            text="←",
            font=orbitron.orbitron(30),
            width=50,
            height=40,
            fg_color="#171F55",
            hover_color="#1D2763",
            text_color="#6C90C3",
            corner_radius=20,
            command=self.go_back,
            border_width=0
        )
        self.back_button.place(x=20, y=20)

        self.header_label = ctk.CTkLabel(
            self.content_frame,
            text="Cryptic Locker",
            font=orbitron.orbitron(90),
            text_color="#6C90C3"
        )
        self.header_label.pack(pady=(50, 50))

        self.username_label = ctk.CTkLabel(
            self.content_frame, text="Username:", font=orbitron.orbitron(32), text_color="#6C90C3"
        )
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

        self.password_label = ctk.CTkLabel(
            self.content_frame, text="Password:", font=orbitron.orbitron(32), text_color="#6C90C3"
        )
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
            command=self.submit
        )
        self.login_button.pack(pady=(20, 10))

    def submit(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        login = Login()

        if not username:
            self.content_frame.focus_set()
            self.username_entry.delete(0, ctk.END)
            self.username_entry.configure(border_color="red", placeholder_text_color="red", placeholder_text="Username cannot be empty")
            return

        if not password:
            self.content_frame.focus_set()
            self.password_entry.delete(0, ctk.END)
            self.password_entry.configure(border_color="red", placeholder_text_color="red", placeholder_text="Password cannot be empty")
            return

        if not login.username_check(username):
            self.content_frame.focus_set()
            self.username_entry.delete(0, ctk.END)
            self.username_entry.configure(border_color="red", placeholder_text_color="red", placeholder_text="No such user exists")
            return

        login.parse_data(username=username)
        if not login.match_password(user_password=password):
            self.content_frame.focus_set()
            self.password_entry.delete(0, ctk.END)
            self.password_entry.configure(border_color="red", placeholder_text_color="red", placeholder_text="Invalid Password")
            return
        else:
            self.unbind("<Return>")
            self.unbind("<Escape>")
            LoginTOTPScreen(username=username)
            self.after(1,self.destroy)


    def go_back(self,event=None):
        self.parent.deiconify()
        self.parent.state('zoomed')
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    app = LoginScreen(parent=root)
    app.mainloop()
