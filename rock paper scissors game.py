#---------------------- Rock–paper–scissors game----------------------------

from random import choice     
from time import sleep        
l=["r","p","s"]               ## From Random Module WE import Choice which provide Choice from list 
while 1:
    c=choice(l)
    p=input("Enter R for Rock|P for Paper|S for Scissor% ---->  ").strip().lower()
    if p==c:
        sleep(2)              #From time module we import sleep which sleep the result for 2 second
        print("Draw")
        print("Computer choice",c)
    elif p=="p" and c=="r" or p=="s" and c=="p" or p=="r" and c=="s":
        sleep(2)
        print("Player1 Wins")
        print("computer choice",c)
    else:
        sleep(2)
        print("computer Wins")
        print("computer choice",c)
    print()
    print("For continue this game press y else press any key ")
    ch=input("Enter your choice ")
    if ch!="y":
        break
