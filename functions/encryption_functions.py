"""Module used to encrypt and decrypt files"""
from cryptography.fernet import Fernet

def encrypt(text, key):
    """Library to encrypt manually"""
    fernet = Fernet(key)
    return fernet.encrypt(text)

def decrypt(file, key):
    """Library to decrypt manually"""
    fernet = Fernet(key)
    with open(file, 'rb') as keyfile:
        encrypted = keyfile.read()
    decrypted = fernet.decrypt(encrypted)
    return bytes.hex(decrypted)
