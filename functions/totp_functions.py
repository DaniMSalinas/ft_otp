"""Module to generate Time based one time password"""
import base64
import hmac
import struct
import time
from functions.encryption_functions import decrypt

def hotp(key, counter, digits=6, digest='sha1'):
    """Function to generate hotp"""
    key = base64.urlsafe_b64decode(key)
    counter = struct.pack('>Q', counter)
    mac = hmac.new(key, counter, digest)
    mac = mac.digest()
    offset = mac[-1] & 0x0f
    binary = struct.unpack('>L', mac[offset:offset+4])[0] & 0x7fffffff
    return str(binary)[-digits:].zfill(digits)

def totp(key, time_step=30, digits=6, digest='sha1'):
    """Function to generate totp"""
    with open('token', 'rb') as keyfile:
        token = keyfile.read().decode("utf-8")
    key = decrypt(key, base64.urlsafe_b64encode(bytes.fromhex(token)))
    return hotp(key, int(time.time() / time_step), digits, digest)
