'''
Determine the age of a person, in number of days
'''

from datetime import date


def diffBetweenDatesInDays(date1, date2):
    '''
    in:
        date1 - date object
        date2 - date object
    out:
        integer - the numbers of days between those 2 dates
    '''
    return abs(date2 - date1).days


def readDate():
    '''
    in:
        read a string date in format DD-MM-YYYY and checks
    out:
        it returns the given date in an object of type: date
    '''
    while True:
        # we read an date input
        auxString = input("Please enter your birthdate in format DD-MM-YYYY: ")
        # we read an date input and we check if it is the desired format
        if len(auxString) == 10:
            # we split the auxiliary string and convert the list of strings to a list of integers
            try:
                day, month, year = map(int, auxString.split('-'))
                # we try to create a date object and check if it is a valid date
                auxDate = date(year, month, day)
                if auxDate > date.today():
                    print("Something is wrong... You are not even born yet... Please try again")
                    continue
                return auxDate
            except ValueError:
                print("Oops! That was not a valid date. Try again...")
                continue
        else:
            print("Ooops... the day entered is not in the correct format ")
            continue


def run():
    birthDate = readDate()
    print("You are " + str(diffBetweenDatesInDays(birthDate, date.today())) + " days old")


run()
