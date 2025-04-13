import os
import base64
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

class SignUp():
    def __init__(self):
        super().__init__()

    @staticmethod
    def username_check( name):
        vault_path = "../vault"
        username_file = f"{name}.acrl"

        if not os.path.exists(vault_path):
            os.makedirs(vault_path)

        return not os.path.exists(os.path.join(vault_path, username_file))

    def derive_key(self, password: str, salt: bytes = None) -> tuple[bytes, bytes]:
        if salt is None:
            salt = os.urandom(32)

        kdf = PBKDF2HMAC(
            algorithm= hashes.SHA512(),
            length= 32,
            salt=salt,
            iterations= 100_000,
            backend= default_backend()
        )

        key = kdf.derive(password.encode('utf-8'))
        return key, salt


    def encrypt_password(self, password: str, key: bytes):
        if isinstance(password, str):
            password = password.encode('utf-8')

        iv = os.urandom(16)

        cipher = Cipher(algorithm= algorithms.AES(key), mode= modes.GCM(iv))
        encryptor = cipher.encryptor()

        cipher_text = encryptor.update(password) + encryptor.finalize()
        tag = encryptor.tag
        encrypted_data = iv + cipher_text + tag
        return base64.b64encode(encrypted_data).decode('utf-8')

    def create_acrl_file(self, username, password):
        vault_path = "../vault"
        if not os.path.exists(vault_path):
            os.makedirs(vault_path)
        magic_header = b'ITSACRLFILEBITCH'
        username_bytes = username.encode('utf-8')

        key, salt = self.derive_key(password= password)
        password_bytes = self.encrypt_password(password= password, key=key).encode('utf-8')

        file_path = os.path.join(vault_path, f"{username}.acrl")

        file_content = bytearray()
        file_content.extend(magic_header)
        file_content.extend(salt)
        file_content.extend(struct.pack("H", len(username_bytes)))
        file_content.extend(username_bytes)
        file_content.extend(struct.pack("H", len(password_bytes)))
        file_content.extend(password_bytes)

        encrypted_file_content = base64.b64encode(file_content)

        with open(file_path, "wb") as file:
            file.write(encrypted_file_content)

