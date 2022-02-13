import os
def new_user():
    conf="N"
    while conf !="Y":
        username = input("input username : ")
        print("are you sure to use this ",username," as username ? ", "Y/N")
        conf = input().upper()
    os.system("sudo adduser " + username)
new_user()