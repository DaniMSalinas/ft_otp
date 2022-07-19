"""Programa para generar un TOTP en python para el bootcamp de 42ciber"""
import sys
from functions import key_functions
from functions import totp_functions

def main():
    """ main function bro"""
    if sys.argv[1] == "-g":
        if sys.argv[2]:
            print(key_functions.validate_hexadecimal_key(sys.argv[2]))
        else:
            print ("Hay que introducir una clave")
    elif sys.argv[1] == "-k":
        if sys.argv[2]:
            print(totp_functions.totp(sys.argv[2]))
        else:
            print ("Hay que pasar golden ticket")

if __name__ == "__main__":
    main()
