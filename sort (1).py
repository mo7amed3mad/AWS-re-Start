import json
'''
def sortlist(lis,string):
    f=open("out.txt" , "r+")
    
    if string == "asc":
        lis.sort()
        for i in lis:
            f.write(str(i) + " , ")
        print(lis)
        
    elif string == "desc":
        lis.sort(reverse=True)
        
        for i in lis:
            f.write(str(i) + " , ")
        print(lis)
        
    elif string == "none":
        
        for i in lis:
            f.write(str(i) + " , ")
        print(lis)
    else:
        print ("you entre unvalid value")


x = input("intre the list in format [item 1 , item 2 ,...., item n] : ")
lis=json.loads(x)
string = input (" inter type of sort (asc , desc , none) : ")
sortlist(lis,string)
'''
print("-------------------")

def mid(s):
    if len(s) % 2 != 0:
        print (s[len(s)//2])
    elif len(s) % 2 == 0:
        print ("")
x = input("inter your string : " )
mid(x)

