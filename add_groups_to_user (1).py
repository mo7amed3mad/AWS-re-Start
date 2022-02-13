import subprocess
import os

#add user if does not exsit

def add_user():
    confirm = "NO"
    while confirm !="YES":
        user=input("entre the username : ")
        out_u = subprocess.Popen(["grep",user,"/etc/passwd"],stdout=subprocess.PIPE).communicate()[0]
        out_g = subprocess.Popen(["grep",user,"/etc/group"],stdout=subprocess.PIPE).communicate()[0]
        username = str(out_u)
        groupname = str(out_g)
        if user in username:
            print("user already exist plz entre new user")
            confirm = "No"
            
        elif user in groupname:
            subprocess.run(["sudo","useradd","-g",user,user])
            confirm="YES"
            return user
            
        else:
             subprocess.run(["sudo","useradd",user])
             confirm="YES"
             return user
             
#add group if does not exist    
   
def add_group():
    confirm = "NO"
    while confirm !="YES":
        group=input("entre the groupname : ")
        out = subprocess.Popen(["grep",group,"/etc/group"],stdout=subprocess.PIPE).communicate()[0]
        groupname = str(out)
        if group in groupname:
            print("group already exist plz entre new user")
            confirm = "No"
        else:
             subprocess.run(["sudo","groupadd",group])
             confirm="YES"
             return group
#add useres to group             
             
def add_user_to_group():
    user=add_user()
    confirm = "y"
    while confirm !="n":
        group=add_group()
        subprocess.run(["sudo","usermod","-a","-G",group,user])
        print("would you like to add "+user+" in another gorups Y/N")
        confirm = input()
        
add_user_to_group()