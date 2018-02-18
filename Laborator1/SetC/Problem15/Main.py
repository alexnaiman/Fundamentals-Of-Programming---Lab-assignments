'''
Generate the smallest perfect number larger than a given natural number n. If such a number
does not exist, a message should be displayed. A number is perfect if it is equal to the sum of its
divisors, except itself. E.g. 6 is a perfect number (6=1+2+3)
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


def isPerfect(number):
    '''
         in:
             number - integer
         out:
             boolean -> true if it is a perfect number
     '''
    sum = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            sum += i
            print(sum, i)
    return number == sum


def searchForPerfectNumberSmaller(number):
    '''
        in:
            number - integer
        out:
            integer/none -> the largest perfect number smallest than the given number or None
    '''
    while number >= 0:
        if isPerfect(number):
            return number
        else:
            number -= 1


def run():
    '''
         main function of our program
         it "runs" and "controls" the functions we need
    '''
    n = readNaturalNumber("The number is? \n")
    print("The largest perfect number smallest than the given number is " + str(searchForPerfectNumberSmaller(n))
          if searchForPerfectNumberSmaller(n) else "Soooorry... there aren't ny perfect numbers here")


run()
