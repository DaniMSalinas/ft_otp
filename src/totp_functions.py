"""Module to generate Time based one time password"""
import hmac
import time
from src.encryption_functions import decrypt
from src.key_functions import ask_password
from src.token_functions import generate_password_token

def hotp(key, counter, digits=6, digest='sha1'):
    """Function to generate hotp"""
    counter = counter.to_bytes(8, byteorder='big') #counter = struct.pack('>Q', counter)
    mac = hmac.new(key, counter, digest)
    mac = mac.digest() #datatracker.ietf.org/doc/html/rfc4226#section-5
    offset = mac[-1] & 0x0f #se buscan the lower 4 bits
    binary = int.from_bytes(mac[offset:offset+4], 'big',signed=False) #binary = struct.unpack('>L', mac[offset:offset+4])[0] & 0x7fffffff
    return str(binary)[-digits:]

def totp(key_path, time_step=60, digits=6, digest='sha1'):
    """Function to generate totp"""
    password = bytes(ask_password(), "utf-8")
    password_key = generate_password_token(password)
    with open('data/' + key_path, 'rb') as keyfile:
        message = keyfile.read()
    key = decrypt(message, password_key)
    print(int(time.time())/time_step)
    if key:
        return hotp(key, int(time.time() / time_step), digits, digest)
    return "Incorrect password"
