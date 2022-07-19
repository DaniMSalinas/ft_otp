"""Library with the bonus functions of the projects"""

def set_password():
    """Function to set a password for the master key"""
    password = str(input("Set a password for the master key: "))
    with open('__data__/.pw', 'w', encoding="ascii") as password_file:
        password_file.write(password)
    return password

def ask_password():
    """Function to ask the password for the master key"""
    password = str(input("Write the password of the master key: "))
    with open('__data__/.pw', 'r', encoding="ascii") as password_file:
        original_password = password_file.read()
    if original_password != password:
        raise ValueError
