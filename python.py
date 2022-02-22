#quiz python (string)
print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\t Up above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\t How I wonder what you are")

print ("------------------------------------------")

#quiz python (condition)
numbers = [10,33,40]
print (max(numbers))

print ("------------------------------------------")
#quiz python (function)
def calc(s):
   # s = "The Geek King"
    l,u = 0,0
    for i in s:
        if (i>='a'and i<='z'):
            l=l+1  
            
        if (i>='A'and i<='Z'):
            u=u+1   
          
    print('Lower case characters: ',l)
    print('Upper case characters: ',u)
calc("AHMED AHMED")

print ("------------------------------------------")
#quiz python (function) in another way
def up_low(str):
    upper_count=0
    lower_count=0
    for x in str:
        if x.isupper():
            upper_count+=1
        else:
            lower_count+=1
    print('Lower case characters: ',upper_count)
    print('Upper case characters: ',lower_count)

up_low("MOHAMEDemad")