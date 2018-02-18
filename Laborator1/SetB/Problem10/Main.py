'''
Consider a given natural number n. Determine the product p of all the proper factors of n
'''

import math
from functools import reduce


def readNaturalNumber(message):
    '''
    in:
        message - string -> the message shown before reading the number
    out:
        it returns a natural number read from the keyboard
    '''

    while True:
        try:
            auxNumber = int(input(message))
            if auxNumber < 0:
                print("The number should be positive!")
                continue
            if isPrime(auxNumber):
                print("The number is prime!")
                continue
            return auxNumber
        except ValueError:
            print("Ooops... something went wrong... please try again!")
            continue


def getProperFactors(naturalNumber):
    auxList = []
    for i in range(2, naturalNumber // 2 + 1):
        if naturalNumber % i == 0:
            auxList.append(i)
    return auxList


def isPrime(number):
    '''
    in:
        number - integer
    out:
        boolean if number is prime or not
    '''
    if number == 1:
        return False
    elif number == 2:
        return True
    if number % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
    return True


def listToProduct(list):
    return reduce(lambda x, y: x * y, list)


def run():
    '''
        main function of our program
        it "runs" and "controls" the functions we need
    '''
    n = readNaturalNumber("The number is?\n")

    print("The product of the number's factors is: " + str(listToProduct(getProperFactors(n))))


run()
