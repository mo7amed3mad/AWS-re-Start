file = open ("append" , "a")
file.write(" \nthis line is the test")
file.close()

print("-------------------")

def count_words():
    file = open("append","r")
    count = 0
    count2 = 0
    data = file.read()
    words = data.split()
    for word in words:
        if word[-1] == 'e':
            count+=1
        if word == 'the':
             count2+=1
    print("the number of words ends with character \"e\" is : ",count)
    print("the number of word  \"the\" is : ",count2)

    file.close()

count_words()

