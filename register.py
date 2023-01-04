import re
import hashlib


def check_email(email):
    
   regex = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(regex,email):
      return "Valid Email"
   return "Invalid Email"


def registration():
    first_name= input("Please enter your first Name ")
    last_name= input("Please enter your last Name ")
    mobilephone= input("Please enter your phone number ")  
    try:
        if len(first_name)== 0 or len(last_name) == 0 or len(mobilephone)==0:
            print("sorry Empty Value ")
    except Exception as e:
        print('___error happened___', e)
    email = input("Enter email address: ")
    try:
        if check_email(email) == "Valid Email":
            print("your email is ",email)
        else:
            print("Invalid Email")   
    except:             
        if len(email) == 0 :
            print("Sorry,Empty value")
    password = input("Enter password: ")
    conf_pwd = input("Confirm password: ")     
    if conf_pwd == password:
        enc = conf_pwd.encode()
        pwd_hash = hashlib.md5(enc).hexdigest()   
        userinfo= f"{email}:{pwd_hash}:"   
        with open("login.txt", "a") as f:
            f.write(first_name + ":")
            f.write(last_name + ":")
            f.write(mobilephone + ":")
            f.write(userinfo + "\n")
        f.close()
        print("You have registered successfully!")   
    else:
        print("Password is not same as above! \n")
        registration()
