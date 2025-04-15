import pyotp
import qrcode
from io import BytesIO

class TOTPHandler:
    def __init__(self):
        super().__init__()

    def generate_secret(self):
        return pyotp.random_base32()

    def get_qr(self, username):
        secret = self.generate_secret()
        issuer = "Cryptic Locker"
        uri = pyotp.totp.TOTP(secret).provisioning_uri(name=username, issuer_name=issuer)

        qr = qrcode.make(uri)
        byte_stream = BytesIO()
        qr.save(byte_stream, format='PNG')

        return byte_stream.getvalue(), secret


    def verify_otp(self, otp, secret):
        totp = pyotp.TOTP(secret)
        return totp.verify(otp, valid_window=1)

    def save_secret(self, secret):
        print(secret)