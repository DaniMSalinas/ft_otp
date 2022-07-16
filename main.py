"""Programa para generar un TOTP en python para el bootcamp de 42ciber"""

import sys
import key_functions

def main():
    """ main function bro"""
    if sys.argv[1] == "-g":
        if sys.argv[2]:
            key_functions.validate_hexadecimal_key(sys.argv[2])
        else:
            print ("Hay que introducir una clave")
    elif sys.argv[1] == "-k":
        print ("hola -k")

if __name__ == "__main__":
    main()
