# Generate the first prime number larger than a given natural number n.


import math


def isPrime(number):
    '''
    in: number - integer
    out: True if number is prime
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


def readNaturalNotNullNumber():
    '''
    in: read a number and checks if it is an integer
    out: it returns the writen number
    '''
    while True:
        try:
            auxNumber = int(input("Enter a natural number: "))
            if auxNumber < 0:
                print("The number is not bigger than 0")
                continue
            return auxNumber
        except ValueError:
            print("Oops! That was no valid number. Try again...")
            continue


def searchForNumber(myNumber):
    '''
    in: myNumber integer
    out: returns the first prime number large than myNumber
    '''

    auxNumber = myNumber + 1
    while not isPrime(auxNumber):
        auxNumber += 1
    return auxNumber


number = readNaturalNotNullNumber()
print(searchForNumber(number))
