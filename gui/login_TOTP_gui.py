import customtkinter as ctk
import tkinter as tk
from utils import orbitron

class LoginTOTPScreen(ctk.CTkToplevel):
    def __init__(self, username):
        super().__init__()
        self.username = username

        self.after(201, lambda: self.iconbitmap("../assets/images/logo.ico"))
        self.state('zoomed')
        self.title("Cryptic Locker - 2FA")
        self.minsize(900, 800)
        self.configure(fg_color="#171F55")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.content_frame = ctk.CTkFrame(
            self, width=500, height=400, fg_color="#1D2763",
            corner_radius=10, border_color="#6C90C3", border_width=2
        )
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.header_label = ctk.CTkLabel(
            self.content_frame,
            text="2FA",
            font=orbitron.orbitron(65),
            text_color="#6C90C3"
        )
        self.header_label.place(relx=0.5, rely=0.2, anchor="center")

        # Number-only validation
        def only_numbers(text):
            return text.isdigit() or text == ""

        vcmd = (self.register(only_numbers), "%P")

        self.otp_entry = ctk.CTkEntry(
            self.content_frame,
            font=orbitron.orbitron(30),
            width=300,
            corner_radius=10,
            fg_color="#1D2763",
            border_color="#6C90C3",
            border_width=2,
            text_color="white",
            placeholder_text="Enter OTP",
            validate="key",
            validatecommand=vcmd
        )
        self.otp_entry.place(relx=0.5, rely=0.45, anchor="center")

        self.text_label = ctk.CTkLabel(
            self.content_frame,
            text="Enter the OTP displayed\non your Authenticator app",
            font=orbitron.orbitron(32),
            text_color="#6C90C3"
        )
        self.text_label.place(relx=0.5, rely=0.7, anchor="center")

        self.action_button = ctk.CTkButton(
            self.content_frame,
            font=orbitron.orbitron(28),
            width=50,
            height=35,
            corner_radius=8,
            fg_color="#1D2763",
            border_color="#6C90C3",
            border_width=2,
            text_color="white",
            text="Verify",
        )
        self.action_button.place(relx=0.5, rely=0.9, anchor="center")

if __name__ == "__main__":
    app = LoginTOTPScreen("addi")
    app.mainloop()
