'''
For a given natural number n find the minimal natural number m formed with the same digits.
E.g. n=3658, m=3568
'''


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
            return auxNumber
        except ValueError:
            print("Ooops... something went wrong... please try again!")
            continue

def getDigits(naturalNumber):
    auxList = []
    copy = naturalNumber
    while copy:
        auxList.append(copy%10)
        copy//=10
    return auxList


def makeNumberFromDigits(list):
    return reduce(lambda x,y: x*10+y,list)


def makeMinimalNumberFromDigits(list):
    list.sort()
    return makeNumberFromDigits(list)


def run():
    n = readNaturalNumber("The given number is?\n")
    print("The minimal number is: " + str(makeMinimalNumberFromDigits(getDigits((n)))))

run()