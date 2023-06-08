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

print('Pick a positive number')
initialNumber = abs(int(input()))

collatz(initialNumber)
