file=open("omar.txt","a")
for num in range(1, 251):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
           else:
                file.write(str(num))
                print(num)
file.close()

       
  