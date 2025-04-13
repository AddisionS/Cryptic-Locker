import customtkinter as ctk
from utils import orbitron
from backend.TOTP import TOTPHandler
from PIL import Image
from io import BytesIO

class TOTPScreen(ctk.CTk):
    def __init__(self, username):
        super().__init__()
        self.username = username

        self.iconbitmap("../assets/images/logo.ico")
        self.state('zoomed')
        self.title("Cryptic Locker - 2FA")
        self.minsize(900, 800)
        self.configure(fg_color="#171F55")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        # Content Frame
        self.content_frame = ctk.CTkFrame(self, width=500, height=600, fg_color="#1D2763",corner_radius=10, border_color="#6C90C3", border_width=2)
        self.content_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.header_label = ctk.CTkLabel(
            self.content_frame,
            text="2FA",
            font=orbitron.orbitron(65),
            text_color="#6C90C3"
        )
        self.header_label.place(relx=0.5, rely=0.2, anchor="center")

        qr_img_bytes, secret = TOTPHandler().get_qr(self.username)
        qr_img = Image.open(BytesIO(qr_img_bytes))

        self.qr_ctk_image = ctk.CTkImage(light_image=qr_img, dark_image=qr_img, size=(200, 200))

        self.qr_label = ctk.CTkLabel(self.content_frame, image=self.qr_ctk_image, text="")
        self.qr_label.place(relx=0.5, rely=0.45, anchor="center")

        self.text_label = ctk.CTkLabel(self.content_frame, text = "Scan this using your\nAuthenticator app", font = orbitron.orbitron(32), text_color="#6C90C3")
        self.text_label.place(relx = 0.5, rely = 0.77, anchor = "center")
        self.proceed_button = ctk.CTkButton(
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
        )
        self.proceed_button.place(relx = 0.5, rely = 0.9, anchor = "center")



if __name__ == "__main__":
    app = TOTPScreen("addi")
    app.mainloop()
