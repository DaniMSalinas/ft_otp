"""Library to validate and save hexadecimal keys"""
from Cryptodome.Hash import SHA256
from Cryptodome.Protocol.KDF import PBKDF2
from src.encryption_functions import encrypt
from base64 import b32decode, b32encode, b32hexdecode

def validate_hexadecimal_key(key):
    """Function to validate master key"""
    try:
        bytes.fromhex(key)
    except ValueError:
        return "You must set an hexadecimal key"
    try:
        count_key_length(key)
    except ValueError:
        return "The key must have at least 64 Hex characters"
    save_key(key)
    return "The key have been succesfully saved in ft_otp.key"

def count_key_length(key):
    """Function to check if the key has at least 64 hexadecimal characters"""
    if len(key) >= 64:
        return True
    raise ValueError

def save_key(key):
    """Function used to save the master key on a ciphered .key file"""
    password = bytes(set_password(), "utf-8")
    key = key.encode("utf-8")
    encrypted = encrypt(b32encode(key), generate_password_token(password))
    with open('data/ft_otp.key', 'wb') as keyfile:
        keyfile.write(encrypted)
        keyfile.close()

def generate_password_token(password):
    """Function to generate key with password"""
    salt = bytes.fromhex("5ef8572d3738892f309f1b5d56170c8c")
    token = PBKDF2(password, salt, 64, 1000, hmac_hash_module=SHA256)
    return token[-16:]

def change_to_base32(key):
    """Function changes the key to base32"""
    key = b32encode(key)
    return b32decode(key)

def set_password():
    """Function to set a password for the master key"""
    return str(input("Set a password for the master key: "))

def ask_password():
    """Function to ask the password for the master key"""
    return str(input("Write the password of the master key: "))
