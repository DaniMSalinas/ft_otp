"""Programa para generar un TOTP en python para el bootcamp de 42ciber"""
import sys
from src import key_functions
from src import totp_functions

def main():
    """ main function bro"""
    if sys.argv[1] == "-g":
        if len(sys.argv) == 3:
            print(key_functions.validate_hexadecimal_key(sys.argv[2]))
        else:
            print ("Error using -g command")
    elif sys.argv[1] == "-k":
        if len(sys.argv) == 3:
            print(totp_functions.totp(sys.argv[2]))
        else:
            print ("Hay que pasar golden ticket")
    else:
        print("Invalid command")

if __name__ == "__main__":
    main()
