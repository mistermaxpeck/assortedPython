# My solution to the Collatz Sequence problem from Automate the Boring Stuff by Al Sweigart

import os, sys

def collatz(number):
    while number !=1:
        if number % 2 == 0:
            print(number/2)
            return collatz(number/2)
        elif number % 2 == 1:
            print(3*number+1)
            return collatz(3 * number + 1)
    print('End of program')

def userChoice():
    print('Pick a number.')
    try:
        initialNumber = abs(int(input()))
        if initialNumber == 0:
            sys.exit('Zero doesn\'t exist.')
    except:
        sys.exit('Pick a number, dummy')

    collatz(initialNumber)

userChoice()
