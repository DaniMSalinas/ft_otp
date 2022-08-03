"""Module to generate a password to cipher the master key"""
from Cryptodome.Hash import SHA256
from Cryptodome.Protocol.KDF import PBKDF2

def generate_password_token(password):
    """Function to generate key with password"""
    salt = bytes.fromhex("5ef8572d3738892f309f1b5d56170c8c")
    token = PBKDF2(password, salt, 32, 10000, hmac_hash_module=SHA256)
    return token[:16]
