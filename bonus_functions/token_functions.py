"""Module to generate a password to cipher the master key"""
import base64   
import os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def generate_password_token(password):
    """Function to generate to fernet token with password"""
    salt = os.urandom(16)
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(bytes(password, "ascii")))
    with open('__data__/token', 'wb') as tokenfile:
        tokenfile.write(key)
    return key
    