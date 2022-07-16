from cryptography import fernet

def validate_hexadecimal_key(key):
    """Function to validate master key"""
    try:
        bytes.fromhex(key)
    except ValueError:
        print ("You must set an hexadecimal key")
    try:
        count_key_length(key)
    except ValueError:
        print("The key must have at least 64 Hex characters")
     
def count_key_length(key):
    """Function to check if the key has at least 64 hexadecimal characters"""
    if len(key) / 2 >= 64:
        return True
    return ValueError

def save_key():
    """Function used to save the master key on a ciphered .key file"""
    
    return 0
