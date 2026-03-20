from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(secret: str):
    return base64.urlsafe_b64encode(hashlib.sha256(secret.encode()).digest())

class SecureData:
    def __init__(self, secret_key):
        key = generate_key(secret_key)
        self.cipher = Fernet(key)

    def encrypt(self, data: str) -> bytes:
        return self.cipher.encrypt(data.encode())

    def decrypt(self, encrypted_data: bytes) -> str:
        return self.cipher.decrypt(encrypted_data).decode()
