"""Library to validate and save hexadecimal keys"""

from src.token_functions import generate_password_token
from src.encryption_functions import encrypt

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
    password_key = generate_password_token(password)
    encrypted = encrypt(bytes.fromhex(key), password_key)
    with open('data/ft_otp.key', 'wb') as keyfile:
        keyfile.write(encrypted)
        keyfile.close()

def set_password():
    """Function to set a password for the master key"""
    return str(input("Set a password for the master key: "))

def ask_password():
    """Function to ask the password for the master key"""
    return str(input("Write the password of the master key: "))
