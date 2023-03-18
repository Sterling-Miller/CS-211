""" LAB 08 - 02/28/23
Sign-up Interface - Sterling Miller
"""
import re


def validate_email(email: str) -> bool:
    rexgex = re.fullmatch("^[A-Za-z][A-Za-z0-9]+@[a-z]+\.(com|edu)", email)
    return bool(rexgex)


def validate_password(password: str) -> bool:
    rexgex = re.findall("(?=.*\d)(?=.*\W).{10,}", password)
    return bool(rexgex)


def main():
    email = input("Provide an email address: ")
    while not validate_email(email):
        email = input("Invalid email, provide a different one: ")
    password = input("Input your password: ")
    while not validate_password(password):
        password = input("Invalid password, provide a different one: ")
    print("Sign up successful")


if __name__ == '__main__':
    main()
