# a wrap up which prints the list for the "strictly increasing numbers" condition
def _strictlyIncreasingNumbers(listOfNumber):
    print("Property 1: strictly increasing numbers")
    firstPosition, secondPosition = checkCondition(listOfNumber, strictlyIncreasingCondition, True)
    _printListFromGivenPosition(listOfNumber, firstPosition, secondPosition+1)


# a wrap up which prints the list for the "alternate sign" condition
def _alternateSignNumbers(listOfNumbers):
    print("Property 2: Consecutive numbers have different signs")
    firstPosition, secondPosition = checkCondition(listOfNumbers, alternateSignCondition, True)
    _printListFromGivenPosition(listOfNumbers, firstPosition, secondPosition+1)


def _readList(listOfNumbers):
    '''
        in: reads the list of numbers one by one
    '''
    print("Enter the list of numbers (type 'exit' to exit):")
    while True:
        number = input()
        if number.strip().lower() == 'exit':
            return
        if addNumber(listOfNumbers, number):
            print("Number added to the list")
        else:
            _printError("invalid input")


def _printAllList(list):
    print("The list is")
    _printListFromGivenPosition(list, 0, len(list))
    return


def _printError(message):
    print("Ooops... something went wrong:\n" + message)


def _exit(stop):
    print("The end of the program")
    return not stop


def _printMenu(menuOptionsList):
    print("Menu:")
    for i in range(len(menuOptionsList)):
        print(str(i) + ' ' + str(menuOptionsList[i][0]))
    return


def _printListFromGivenPosition(listOfNumbers, firstPosition, endposition):
    '''
        in: listOfNumbers - list of integers
            firstPosition, endPostion - the position from which we print the items from  the list - integers

    '''
    print(listOfNumbers[firstPosition:endposition])


def strictlyIncreasingCondition(a, b):
    '''
          in: a,b - integers
          out: bool returns true if a is strictly greater than one
    '''
    return a < b


def addNumber(listOfNumbers, numberToAdd):
    '''
    in: listOfNumbers - list of integers
        numberToAdd - the number which we want to append to the list - string
    out: check if the input read is an integer and it appends to the list
        boolean - true if the number is added with success
                - false if it is wasn't read a number
    '''
    try:
        listOfNumbers.append(int(numberToAdd))
        return True
    except ValueError:
        return False


def alternateSignCondition(a, b):
    '''
        in: a,b - integers
        out: bool returns true if the numbers have different signs
    '''
    return (a > 0 > b) or (a < 0 < b)


def checkNumbersInPairs(listOfNumbers, givenCondition):
    '''
        in: listOfNumbers - integers
            givenCondition - the condition we want to check - function
        out: list of integers like (firstPosition, secondPosition) that are the positions from which we will the largest
             with the given condition
    '''
    pos, number, maxNumber, firstPos = -1, -1, -1, -1
    i = -1
    while i < len(listOfNumbers) - 2:
        i += 1
        if givenCondition(listOfNumbers[i], listOfNumbers[i + 1]) and i < len(listOfNumbers) - 1:
            pos = i
            number = 0
            while i < len(listOfNumbers) - 1 and givenCondition(listOfNumbers[i], listOfNumbers[i + 1]):
                number += 1
                i += 1
            # i -= 1
            if number > maxNumber:
                maxNumber = number
                firstPos = pos
    return firstPos, firstPos + maxNumber


def checkNumbersOneAtATime(listOfNumbers, givenCondition):
    '''
        in: listOfNumbers - integers
            givenCondition - the condition we want to check - function
        out: list of integers like (firstPosition, secondPosition) that are the positions from which we will the largest
             with the given condition
    '''
    pos, number, maxNumber, firstPos = -1, -1, -1, -1
    i = 0
    while i < len(listOfNumbers) - 1:
        i += 1
        if givenCondition(listOfNumbers[i], listOfNumbers[i + 1]) and i < len(listOfNumbers) - 1:
            pos = i
            number = 0
            while i < len(listOfNumbers) - 1 and givenCondition(listOfNumbers[i], listOfNumbers[i + 1]):
                number += 1
                i += 1
            if number > maxNumber:
                maxNumber = number
                firstPos = pos
    return firstPos, firstPos + maxNumber


def sumOfElements10(listOfNumbers):
    pos, number, maxNumber, firstPos = -1, -1, -1, -1
    for i in range(len(listOfNumbers) - 1):
        auxSum=listOfNumbers[i]
        pos = i
        number = 1
        while auxSum <= 10 and i < len(listOfNumbers):
            auxSum += listOfNumbers[i+1]
            number+=1
            print(auxSum)
            if auxSum == 10:
                if number > maxNumber:
                    maxNumber = number
                    firstPos = pos
                break
            elif auxSum > 10:
                break
            i += 1
    return firstPos, firstPos + maxNumber


def atMost3DistinctValues(listOfNumbers):
    pos, number, maxNumber, firstPos = -1, -1, -1, -1
    auxList=[]
    for i in range(len(listOfNumbers)-1):
        auxList.append(listOfNumbers[i])
        pos = i
        number = 0
        while len(auxList) <= 3 and i<len(listOfNumbers)-1:
            if listOfNumbers[i+1] in auxList:
                number += 1
            elif len(auxList) <= 3:
                number += 1
                auxList.append(listOfNumbers[i+1])
            i+=1
        if number>maxNumber:
            maxNumber = number
            firstPos = pos
        auxList=[]
    return firstPos, firstPos + maxNumber


def checkCondition(listOfNumbers, givenCondition, pairFlag):
    '''
        in: listOfNumbers - integers
            givenCondition - the condition we want to check -function
            pairFlag - boolean which determines if we should check the numbers one at a time or two by two
                    - true -> pair;
                    -false -> one by one
        out: list of integers like (firstPosition, secondPosition) that are the positions from which we will the largest
             with the given condition
    '''
    if pairFlag:
        return checkNumbersInPairs(listOfNumbers, givenCondition)
    return givenCondition(listOfNumbers)


def cleanList(listOfNumbers):
    '''
        in:
            listOfNumbers - list of integers
        out:
            it cleans the list's content
    '''
    del listOfNumbers[:]


def _cleanList(listOfNumbers):
    print("The list was cleaned")
    cleanList(listOfNumbers)


def _atMost3DistinctValues(myList):
    firstPos,lastPos= atMost3DistinctValues(myList)
    print(myList[firstPos:lastPos])


def _sumOfElements10(myList):
    firstPos, lastPos = sumOfElements10(myList)
    print(myList[firstPos:lastPos])


def start():
    # a dictionary with all our menu options with key, message to print and function to call
    menuOptions = {1: ('Read sequence of numbers', _readList),
                   2: ('Print the list of numbers', _printAllList),
                   3: ('Check for the largest sequence with strictly increasing numbers', _strictlyIncreasingNumbers),
                   4: ('Check for the largest sequence whose numbers have different signs', _alternateSignNumbers),
                   5: ('Clean the list', _cleanList),
                   6: ('Check for the largest sequence that contains at most 3 distinct values', _atMost3DistinctValues),
                   7: ('Check for the largest sequence which elements have sum equal to 10', _sumOfElements10),
                   0: ('Exit', _exit)
                   }

    listOfNumbers = []
    stop = False
    while not stop:
        _printMenu(menuOptions)
        try:
            command = int(input("Select one of the menu options:\n"))
            if command == 0:
                 stop = menuOptions[0][1](stop)
            elif command == 6:
                _atMost3DistinctValues(listOfNumbers)
            else:
                menuOptions[command][1](listOfNumbers)
        except (ValueError, KeyError):
            _printError("That command wasn't valid!")
            continue

start()
