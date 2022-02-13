import random
score = 0
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        score+=1
        print(" That is correct your score is: {}".format(score))
        if score == 5:
            break
        
    else:
        if score > 0:
            score-=1
        else:
            score=0;
        print(" That is false your score is: {}".format(score))
        
        
