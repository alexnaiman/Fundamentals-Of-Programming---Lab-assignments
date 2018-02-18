'''
The palindrome of a number is the number obtained by reversing the order of digits. E.g.
palindrome (237) = 732). For a given natural number n, determine its palindrome
'''


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


def DeterminePalindrome(number):
    '''
        in:
            number - integer
        out:
            auxNumber - integer the palindrome for the number
    '''
    auxNumber = 0
    while number > 0:
        auxNumber = number % 10 + auxNumber * 10
        number //= 10

    return auxNumber


def run():
    '''
        main function of our program
        it "runs" and "controls" the functions we need
    '''
    n = readNaturalNumber("The number is?\n")

    print("The number's palindrome is: " + str(DeterminePalindrome(n)))


run()
