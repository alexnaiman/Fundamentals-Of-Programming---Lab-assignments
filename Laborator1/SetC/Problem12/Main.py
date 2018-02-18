'''
The numbers n1 and n2 have the property P if their writings in basis 10 have the same digits
(e.g. 2113 and 323121). Determine whether two given natural numbers have the property P
'''


def readNaturalNumber(message):
    '''
    in:
        message - string -> the message shown before reading the number
    out:
        it returns a natural number read from the keyboard
    '''

    print("Any float will be converted!")
    while True:
        try:
            auxNumber = int(input(message))
            if auxNumber < 0:
                print("The number should be positive!")
                continue
            return auxNumber
        except ValueError:
            print("Ooops... something went wrong... please try again!")
            continue


def getNumbersDigits(number):
    '''
    in:
        number - integer -> the number of which we want to get its set of digits
    out:
        auxSetOfDigits - set of integers -> the set of digits of the given number
    '''

    auxSetOfDigits = set([])
    while number != 0:
        auxSetOfDigits.add(number % 10)
        number = number // 10
    return auxSetOfDigits


def checkForPProperty(firstSetOfDigits, secondSetOfDigits):
    '''
    in:
        firstSetOfDigits, secondSetOfDigits - sets of integers which contains the digits of the numbers
    out:
         boolean -> true if the given numbers have the P property
    '''

    differenceSet = set.symmetric_difference(firstSetOfDigits, secondSetOfDigits)
    if len(differenceSet) != 0:
        return False
    return True


def run():
    '''
        main function of our program
        it "runs" and "controls" the functions we need
    '''
    firstNumber = readNaturalNumber("The first number is? \n")
    secondNumber = readNaturalNumber("the second number is? \n")
    firstNumberDigits = getNumbersDigits(firstNumber)
    secondNumberDigits = getNumbersDigits(secondNumber)
    print("Have the given numbers the P property? \n")
    print("Yes, the given numbers have the P property" if checkForPProperty(firstNumberDigits, secondNumberDigits) else
          "No, the given numbers doesn't have the P property")


run()
