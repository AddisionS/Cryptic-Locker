import os
import base64

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

