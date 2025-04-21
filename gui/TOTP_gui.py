import customtkinter as ctk
from utils import orbitron
from backend.TOTP import TOTPHandler
from PIL import Image
from io import BytesIO

class TOTPScreen(ctk.CTkToplevel):
    def __init__(self, username):
        super().__init__()
        self.username = username

        self.after(201,lambda: self.iconbitmap("../assets/images/logo.ico"))
        self.state('zoomed')
        self.title("Cryptic Locker - 2FA")
        self.minsize(900, 800)
        self.configure(fg_color="#171F55")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self.bind("<Return>", self.handle_enter_key)

        # Content Frame
        self.content_frame = ctk.CTkFrame(
            self, width=500, height=600, fg_color="#1D2763",
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

        # Generate QR
        self.qr_img_bytes, self.secret = TOTPHandler().get_qr(self.username)
        self.qr_img = Image.open(BytesIO(self.qr_img_bytes))
        self.qr_ctk_image = ctk.CTkImage(light_image=self.qr_img, dark_image=self.qr_img, size=(200, 200))

        self.qr_label = ctk.CTkLabel(self.content_frame, image=self.qr_ctk_image, text="")
        self.qr_label.place(relx=0.5, rely=0.45, anchor="center")
        self.qr_label.image = self.qr_ctk_image

        self.text_label = ctk.CTkLabel(
            self.content_frame,
            text="Scan this using your\nAuthenticator app",
            font=orbitron.orbitron(32),
            text_color="#6C90C3"
        )
        self.text_label.place(relx=0.5, rely=0.77, anchor="center")

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
            text="Proceed",
            command=self.proceed
        )
        self.action_button.place(relx=0.5, rely=0.9, anchor="center")

    def handle_enter_key(self, event=None):
        if self.action_button.cget("text") == "Proceed":
            self.proceed()
        elif self.action_button.cget("text") == "Verify":
            self.verify_otp()

    def proceed(self):
        self.content_frame.configure(height=400)
        self.qr_label.destroy()

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
        )
        self.otp_entry.place(relx=0.5, rely=0.45, anchor="center")

        self.text_label.configure(text="Enter the OTP displayed\non your Authenticator app")
        self.text_label.place(relx=0.5, rely=0.65, anchor="center")

        self.action_button.configure(text="Verify", command=self.verify_otp)

    def verify_otp(self):
        otp = self.otp_entry.get().strip()
        if TOTPHandler().verify_otp(otp, self.secret):
            TOTPHandler().save_secret(username=self.username, secret=self.secret)
            self.after(1, self.otp_entry.destroy)
            self.after(1, self.action_button.destroy)
            self.content_frame.configure(height=300)
            self.text_label.configure(text="Successfully Verified")
            self.text_label.place(relx=0.5, rely = 0.6)

        else:
            self.content_frame.focus_set()
            self.otp_entry.delete(0, ctk.END)
            self.otp_entry.configure(
                border_color="red",
                placeholder_text_color="red",
                placeholder_text="Invalid OTP",
            )


if __name__ == "__main__":
    app = TOTPScreen("addi")
    app.mainloop()