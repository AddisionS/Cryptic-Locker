import customtkinter as ctk
from utils import orbitron
import tkinter as tk
import re
from backend.signup import SignUp

USERNAME_PATTERN = r"^[A-Za-z0-9_]{4,20}$"
PASSWORD_PATTERN = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d@$!%?&]{6,}$"

class SignUpScreen(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window setup
        self.iconbitmap("../assets/images/logo.ico")
        self.state('zoomed')
        self.title("Cryptic Locker - Sign Up")
        self.minsize(900, 800)
        self.configure(fg_color="#171F55")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Content Frame
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

        # Username
        self.username_label = ctk.CTkLabel(self.content_frame, text="Username:", font=orbitron.orbitron(32), text_color="#6C90C3")
        self.username_label.pack(pady=(10, 5), anchor='w', padx=(35,0))

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

        # Password
        self.password_label = ctk.CTkLabel(self.content_frame, text="Password:", font=orbitron.orbitron(32), text_color="#6C90C3")
        self.password_label.pack(pady=(10, 5), anchor='w', padx=(35,0))

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
            show="#"
        )
        self.password_entry.pack(pady=(0, 20), anchor='w', padx=(85, 0))

        # Confirm Password
        self.confirm_password_label = ctk.CTkLabel(self.content_frame, text="Confirm Password:", font=orbitron.orbitron(32), text_color="#6C90C3")
        self.confirm_password_label.pack(pady=(10, 5), anchor='w', padx=(35,0))

        self.confirm_password_entry = ctk.CTkEntry(
            self.content_frame,
            font=orbitron.orbitron(30),
            width=575,
            corner_radius=10,
            fg_color="#1D2763",
            border_color="#6C90C3",
            border_width=2,
            text_color="white",
            placeholder_text="Re-enter your password",
            show="#"
        )
        self.confirm_password_entry.pack(pady=(0, 20), anchor='w', padx=(85,0))

        # Sign Up Button
        self.sign_up_button = ctk.CTkButton(
            self.content_frame,
            font=orbitron.orbitron(34),
            width=50,
            height=35,
            corner_radius=8,
            fg_color="#1D2763",
            border_color="#6C90C3",
            border_width=2,
            text_color="white",
            text="Sign Up",
            command=self.submit
        )
        self.sign_up_button.pack(pady=(20, 10))

    def submit(self):
        self.username_entry.configure(border_color="#6C90C3", text_color="white")
        self.password_entry.configure(border_color="#6C90C3", text_color="white")
        self.confirm_password_entry.configure(border_color="#6C90C3", text_color="white")

        error = self.submit_check()

        match error:
            case "long_username":
                self.content_frame.focus_set()
                self.username_entry.delete(0, tk.END)
                self.username_entry.configure(border_color="red", text_color="red", placeholder_text="Username cannot exceed 15 characters")

            case "username_exists":
                self.content_frame.focus_set()
                self.username_entry.delete(0, tk.END)
                self.username_entry.configure(border_color="red", text_color="red", placeholder_text="Username already in use")

            case "username_regex_fail":
                self.content_frame.focus_set()
                self.username_entry.delete(0, tk.END)
                self.username_entry.configure(border_color="red", text_color="red", placeholder_text="A-Z, a-z, 0-9, _ and at least 4 chars")

            case "long_password":
                self.content_frame.focus_set()
                self.password_entry.delete(0, tk.END)
                self.password_entry.configure(border_color="red", text_color="red", placeholder_text="Password cannot exceed 15 characters")

            case "password_regex_fail":
                self.content_frame.focus_set()
                self.password_entry.delete(0, tk.END)
                self.password_entry.configure(border_color="red", text_color="red", placeholder_text="A-Z, a-z, 0-9, @, $, !, %, ?, & and at least 6 chars", show="#")

            case "long_confirm_password":
                self.content_frame.focus_set()
                self.confirm_password_entry.delete(0, tk.END)
                self.confirm_password_entry.configure(border_color="red", text_color="red", placeholder_text="Password cannot exceed 15 characters")

            case "confirm_password_regex_fail":
                self.content_frame.focus_set()
                self.confirm_password_entry.delete(0, tk.END)
                self.confirm_password_entry.configure(border_color="red", text_color="red", placeholder_text="A-Z, a-z, 0-9, @, $, !, %, ?, & and at least 6 chars", show="#")

            case "mismatch_password":
                self.content_frame.focus_set()
                self.password_entry.delete(0, tk.END)
                self.confirm_password_entry.delete(0, tk.END)
                self.password_entry.configure(border_color="red", text_color="red", placeholder_text="Password and Confirm Password doesn't match", show="#")
                self.confirm_password_entry.configure(border_color="red", text_color="red", placeholder_text="Password and Confirm Password doesn't match", show="#")

            case "success":
                SignUp().create_acrl_file(username=self.username_entry.get(), password= self.password_entry.get())

    def submit_check(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        signup = SignUp()

        if not signup.username_check(name=username):
            return  "username_exists"

        if not self.entry_length(self.username_entry):
            return "long_username"

        if password != confirm_password:
            return "mismatch_password"

        if not self.entry_length(self.password_entry):
            return "long_password"

        if not self.entry_length(self.confirm_password_entry):
            return "long_confirm_password"

        if not re.match(USERNAME_PATTERN, username):
            return "username_regex_fail"

        if not re.match(PASSWORD_PATTERN, password):
            return "password_regex_fail"

        if not re.match(PASSWORD_PATTERN, confirm_password):
            return "confirm_password_regex_fail"

        return "success"

    def entry_length(self, field):
        return len(field.get()) <= 15


if __name__ == "__main__":
    app = SignUpScreen()
    app.mainloop()
