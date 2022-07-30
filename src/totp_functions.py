"""Module to generate Time based one time password"""
import hmac
import struct
import time
from src.encryption_functions import decrypt
from src.key_functions import ask_password
from src.token_functions import generate_password_token

def hotp(key, counter, digits=6, digest='sha1'):
    """Function to generate hotp"""
    counter = struct.pack('>Q', counter)
    mac = hmac.new(key, counter, digest)
    mac = mac.digest()
    offset = mac[-1] & 0x0f
    binary = struct.unpack('>L', mac[offset:offset+4])[0] & 0x7fffffff
    return str(binary)[-digits:]

def totp(key_path, time_step=30, digits=6, digest='sha1'):
    """Function to generate totp"""
    password = bytes(ask_password(), "utf-8")
    password_key = generate_password_token(password)
    with open('data/' + key_path, 'rb') as keyfile:
        message = keyfile.read()
    key = decrypt(message, password_key)
    if key:
        return hotp(key, int(time.time() / time_step), digits, digest)
    return "Incorrect password"
