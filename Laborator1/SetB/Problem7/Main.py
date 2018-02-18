'''
Determine a calendar data (as year, month, day) starting from two integer numbers
representing the year and the day number inside that year
'''

from calendar import isleap


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


def isLeapYear(year):
    if isleap(year):
        return False
    return True



def checkDays(days):
    if days >= 365:
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
            auxNumber = int(input("The year is? "))
            if not checkConditions(conditionsToCheck, auxNumber):
                continue
            return auxNumber
        except ValueError:
            print("Ooops.... tht wast not a valid number. Try again...")
            continue


