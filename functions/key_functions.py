"""Library to validate and save hexadecimal keys"""
from base64 import urlsafe_b64encode
from functions.encryption_functions import encrypt

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
    encrypted = encrypt(bytes.fromhex(key), hex2base64(key))
    with open('ft_otp.key', 'wb') as keyfile:
        keyfile.write(encrypted)
    with open('token', 'w', encoding="ascii") as tokenfile:
        tokenfile.write(key)

def hex2base64(key):
    """Function to change hexadecimal base to safe Base64 bytearray"""
    return urlsafe_b64encode(bytes.fromhex(key))