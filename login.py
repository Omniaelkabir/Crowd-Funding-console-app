import re
import hashlib


def login():
    email = input("Enter email: ")
    password = input("Enter password: ")     
    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("login.txt", "r") as f:
        users=f.readlines()
        first_name,last_name,mobilephone,stored_email, stored_password = f.read().split("\n")
        if email == stored_email and auth_hash == stored_password:
            print("Logged in Successfully!")
        else:
            print("Login failed! \n")

    f.close() 

login()  