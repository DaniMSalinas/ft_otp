"""Module used to encrypt and decrypt files"""
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes

def encrypt(message, key):
    """Function to encrypt a plain text using AES256"""
    pad = (AES.block_size - len(message) % AES.block_size)\
                * chr(AES.block_size - len(message) % AES.block_size)
    message = message + bytes(pad, "utf-8")
    initial_vector = get_random_bytes(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, initial_vector)
    return initial_vector + cipher.encrypt(message)

def decrypt(message, key):
    """Function to decrypt a ciphered text using AES128"""
    initial_vector = message[:AES.block_size]
    decipher = AES.new(key, AES.MODE_CBC, initial_vector)
    data = decipher.decrypt(message)
    return data[AES.block_size:-ord(data[len(data) - 1:])]
