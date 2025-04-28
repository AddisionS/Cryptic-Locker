import os
import base64
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

vault_path = "../vault"

class Login():
    def __init__(self):
        self.encrypted_password = None
        self.password_salt = None
        self.username = None

    @staticmethod
    def username_check(name):
        return os.path.exists(os.path.join(vault_path, f"{name}.acrl"))

    def parse_data(self, username):
        self.username = username
        file_path = os.path.join(vault_path, f"{username}.acrl")

        with open(file_path, "rb") as file:
            data = base64.b64decode(file.read())

        index = 16
        self.password_salt = data[index:index + 32]
        index += 32

        username_length = struct.unpack("H", data[index:index + 2])[0]
        index += 2 + username_length

        password_length = struct.unpack("H", data[index:index + 2])[0]
        index += 2
        self.encrypted_password = data[index:index + password_length]

    def derive_key(self, password: str, salt: bytes) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=32,
            salt=salt,
            iterations=100_000,
            backend=default_backend()
        )
        return kdf.derive(password.encode('utf-8'))

    def match_password(self, user_password: str) -> bool:
        try:
            key = self.derive_key(user_password, self.password_salt)

            iv = self.encrypted_password[:16]
            tag = self.encrypted_password[-16:]
            ciphertext = self.encrypted_password[16:-16]

            cipher = Cipher(algorithms.AES(key), modes.GCM(iv, tag))
            decryptor = cipher.decryptor()
            decrypted = decryptor.update(ciphertext) + decryptor.finalize()

            return decrypted.decode('utf-8') == user_password
        except Exception:
            return False
