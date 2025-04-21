import base64
import os.path
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
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

    def save_secret(self, username, secret):
        vault_path = "../vault"
        file_path = os.path.join(vault_path, f"{username}.acrl")

        key, salt = self.derive_key(secret)
        secret_bytes = self.encrypt_secret(secret, key).encode('utf-8')

        file_content = bytearray()
        file_content.extend(salt)
        file_content.extend(struct.pack("H", len(secret_bytes)))
        file_content.extend(secret_bytes)

        encrypted_file_content = base64.b64encode(file_content)

        with open(file_path, "ab") as file:
            file.write(encrypted_file_content)

    def derive_key(self, secret):
        salt = os.urandom(32)

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=32,
            salt = salt,
            iterations= 100_000,
            backend= default_backend()
        )

        key = kdf.derive(secret.encode('utf-8'))
        return key, salt

    def encrypt_secret(self, secret, key):
        if isinstance(secret, str):
            secret = secret.encode('utf-8')

        iv = os.urandom(16)

        cipher = Cipher(algorithm=algorithms.AES(key), mode = modes.GCM(iv))
        encryptor = cipher.encryptor()
        cipher_text = encryptor.update(secret) + encryptor.finalize()
        tag = encryptor.tag
        encrypted_data = iv + cipher_text + tag
        return base64.b64encode(encrypted_data).decode('utf-8')
