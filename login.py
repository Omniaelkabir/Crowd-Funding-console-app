import hashlib
import re
def Login():
    email = input("Enter email: ")
    password = input("Enter password: ")  
    auth = password.encode()
    auth_hash = hashlib.md5(auth).hexdigest()
    with open("login.txt", "r") as f:
        users=f.readlines()
        for u in users :
            userinfo = u.strip("\n")
            # print(login)
            userinfo=userinfo.split(":")
            # print(userinfo)
            # print(re.search(email,u))
            if userinfo[3] == email and userinfo[4] == auth_hash:
                print("Logged in Successfully!")
            else:
                continue

                
           


    f.close()  
