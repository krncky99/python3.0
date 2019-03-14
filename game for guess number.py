#--------------------------------------Guess number----------------------------
#IN this game you have five chances to guess a number
#computer create random number using randint module and store in c variable
#you win ,if your number is equal to computer number within the 5 chances else computer wins  
from random import randint
from time import sleep

while input("Press any key to start "):
    c = randint(1,100)          #create random number
    choice = 5
    while choice >0:
        p = int(input("Enter a number ---> "))
        if p==c:
            sleep(1)
            print("!!!You Win!!!")
            break
        elif p>c:
            sleep(1)
            print("Think Smaller")
        else:
            sleep(1)
            print("Think Bigger")
        choice-=1
    else:
        sleep(1)
        print("!!!Computer wins!!!")
        print("Computer's Choice ",c)
