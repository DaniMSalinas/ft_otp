# ft_otp

PYTHON PROGRAM TO GENERATE TIME BASED ONE TIME PASSWORD.

The program is based on the RFC 6238 and RFC 4226:
    - https://datatracker.ietf.org/doc/html/rfc6238
    - https://datatracker.ietf.org/doc/html/rfc4226

The program has two ways of working:
    - using '-g' in order to generate a master_key ft_otp.key
    - using '-k' in order to generate a TIME_BASED One Time Password

-g option:
    if it's used the -g option the program needs an extra argument. This argument is a file that contains an Hexadecimal string with 64 characters. 
    If this file doesn't fullfil these requirements the program isn't going to work. On the other hand, if the file is correct, the program will create a new file called ft_otp.key whit the key provided in the argument. This information will always be ciphered using AES256 cipher algorithm.

-k option:
    if it's used the -k option the program needs an extra argument. This argument is the ft_otp.key file. This key will be used to cipher the password and will generate a 6 digits One Time Password.

The type of ciphered choosen for this project is a symetric ciphering. The algorithm used to implement it is SHA256.
