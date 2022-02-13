#day4-1_quize

import random

def rand_odd(a,b):
    a = random.randrange(a,b,2)
    b = a + 1
    print (b)
rand_odd(0,100)    

print("----------------------")
#day4-2_qize

def compare(nums):
   if nums[0] == nums[len(nums) - 1]:
       return True
   else:
       return False
numbers_x = [10, 20, 30, 40, 10]
print(compare(numbers_x))  
print("----------------------")
#day4-3_quize
row=5
for i in range(row+1):
    for j in range(i):
        print(i,end=' ')
    print("")

       
