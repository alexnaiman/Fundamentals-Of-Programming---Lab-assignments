'''
Given the natural number n, determine the prime numbers p1 and p2 such that n = p1 + p2
(check the Goldbach hypothesis)
'''

import math


def checkConditions(conditions, number):
    for condition in conditions:
        if not condition(number):
            return False
    return True


def naturalNumber(number):
    if number < 0:
        print("The number is not bigger than 0")
        return False
    return True


def evenNumber(number):
    if number % 2 != 0:
        print("The number is not even!")
        return False
    return True


def readIntegerWithGivenConditions(conditionsToCheck):
    '''
    in:
        read number and checks if it is a natural number
    out:
        returns the written number
    '''
    while True:
        try:
            auxNumber = int(input("Enter a natural (even) number: "))
            if not checkConditions(conditionsToCheck, auxNumber):
                continue
            return auxNumber
        except ValueError:
            print("Ooops.... tht wast not a valid number. Try again...")
            continue


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


def searchForNumbersGoldbachNumbers(naturalNumber):
    '''
    in:
       naturalNumber -  a natural even number
    out:
        returns the Goldbach numbers for the given number - natural numbers
    '''
    auxList = []
    for i in range(2, naturalNumber // 2 + 1):
        if isPrime(i) and isPrime(naturalNumber - i):
            auxList.append([i, naturalNumber - i])
    return auxList


def run():
    '''
        main function of our program
        it "runs" and "controls" the functions we need
    '''
    print("Goldbach's conjecture: \n Every even integer greater than 2 can be expressed as "
          "the sum of two primes (there are some odd numbers that respect this conjecture too)")
    n = readIntegerWithGivenConditions([naturalNumber, evenNumber])
    listOfGoldBachNumbers = searchForNumbersGoldbachNumbers(n)
    print("The Goldbach numbers are:\n " + str(listOfGoldBachNumbers))


run()
