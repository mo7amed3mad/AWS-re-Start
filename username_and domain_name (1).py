mail = input("input your email : ")
username = mail.split('@')[0]
print( "user name : " + username)

domain = mail[mail.index('@') + 1 : ]
print("domain name : " + str(domain)) 