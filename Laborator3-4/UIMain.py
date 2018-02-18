import Service
import copy
import Tests

undoList = []


def addExpenseCommand(params, listOfExpenses):
    '''
            A wrapper function that check the params of the 'add' command, converts the strings to integers,
        links the data input to the functions that modifies directly the list
        in:
            - listOfExpenses: list of tuples of form (day, sum, type)
            - params: list - (<sum>, <category>)
    '''
    global undoList
    auxList = copy.deepcopy(listOfExpenses)
    try:
        if not Service.addExpense(listOfExpenses, params):
            print("Expense was not valid")
        else:
            print("Expense added to the list")
            undoList.append(auxList)
    except Exception as e:
        print(str(e))


def insertExpenseCommand(params, listOfExpenses):
    '''
           A wrapper function that check the params of the 'insert' command, converts the strings to integers,
        links the data input to the functions that modifies directly the list
        in:
           - listOfExpenses: list of lists of form (day, sum, type)
           - params: list - <day> <sum> <category>
    '''
    auxList = copy.deepcopy(listOfExpenses)
    global undoList
    try:
        if not Service.insertExpense(listOfExpenses, params):
            print("Expense was not valid")
        else:
            print("Expense added to the list")
            undoList.append(auxList)
    except Exception as e:
        print(e)


def removeExpenseCommand(params, listOfExpenses):
    '''
           A wrapper function that check the params of the 'remove' command, converts the strings to integers,
        links the data input to the functions that modifies directly the list
        in:
           - listOfExpenses: list of lists of form (day, sum, type)
           - params: list - (<day>)
                          - (<start day>, to, <end day>)
                          - (<category>)
    '''
    global HOUSE_EXPENSES_TYPE
    global undoList
    auxList = copy.deepcopy(listOfExpenses)
    if not checkParams(params):
        print("Invalid Command")
        return
    if len(params) < 2:
        try:
            global HOUSE_EXPENSES_TYPE
            if params[0] in HOUSE_EXPENSES_TYPE:
                if Service.removeExpenseByType(params[0], listOfExpenses):
                    print("Day expenses with given type were removed")
                    undoList.append(auxList)
                    return
                else:
                    print("The given type haven't had any expenses")
            else:
                if Service.removeExpenseByDay(params, listOfExpenses):
                    print("Day expenses with given type were removed")
                    undoList.append(auxList)
                    return
                else:
                    print("The given day haven't had any expenses")
        except Exception as e:
            print(e)
    elif len(params) < 4 and params[1] == 'to':
        try:
            if Service.removeExpenseByStartEndDay(params, listOfExpenses):
                print("The given period of time didn't have any expenses")
            else:
                print("Day expenses were removed")
                undoList.append(auxList)
        except Exception as e:
            print(e)
    else:
        print("Invalid command")


def sortCommand(params, listOfExpenses):
    '''
          A wrapper function that check the params of the 'sort' command, converts the strings to integers,
        links the data input to the functions that modifies directly the list
        in:
           - listOfExpenses: list of lists of form (day, sum, type)
           - params: sort - (<day>)
                          - (<category>)
    '''
    global HOUSE_EXPENSES_TYPE
    if 0 < len(params) < 2:
        if params[0] in HOUSE_EXPENSES_TYPE:
            print(Service.listToString(Service.sortType(params[0], listOfExpenses)))
        else:
            try:
                for l in reversed(Service.sortDay(listOfExpenses)):
                    print(Service.listToString(l))
            except Exception as e:
                print(e)
    else:
        print("Invalid command")


def filterCommand(params, listOfExpenses):
    '''
      A wrapper function that check the params of the 'filter' command, converts the strings to integers,
        links the data input to the functions that modifies directly the list
        in:
           - listOfExpenses: list of lists of form (day, sum, type)
           - params: filter - (<day>)
                          - (<category>)
    '''
    global HOUSE_EXPENSES_TYPE
    global undoList
    operands = ['<', '>', '=']
    auxList = copy.deepcopy(listOfExpenses)
    # if len(params) != 0:

    if len(params) > 0 and params[0] in HOUSE_EXPENSES_TYPE:
        if len(params) == 1:
            if Service.filterExpenseByType(listOfExpenses, params[0]):
                print("All the non-'" + str(params[0]) + "' were removed")
                undoList.append(auxList)
            else:
                print("There wasn't any non-'" + str(params[0]) + "' expense to be filtered")
        elif len(params) != 3:
            print("Invalid input type: number of operands isn't valid")
        else:
            try:
                value = int(params[2])
                if params[1] in operands:
                    if Service.filterExpenseByTypeAndCondition(listOfExpenses, params[0], params[1], value):
                        print("All the non-'" + str(params[0]) + " " + str(params[1]) + " " + str(value) +
                              "' were removed")
                        undoList.append(auxList)

                    else:
                        print("There wasn't any non-'" + str(params[0]) + "' expense to be filtered")
                else:
                    print("Invalid operand type")
            except ValueError:
                print("Invalid input type")
    else:
        print("Invalid input")


def listCommand(params, listOfExpenses):
    '''
           A wrapper function that check the params of the 'list' command, converts the strings to integers,
        links the data input to the functions that modifies directly the list
        in:
           - listOfExpenses: list of lists of form (day, sum, type)
           - params: list - []
                          - (<category>)
                          - (< <category>, [ < | = | > ], <value>>)
    '''
    global HOUSE_EXPENSES_TYPE
    operands = ['<', '>', '=']
    if len(params) == 0:
        print("Entire list of expenses")
        print(Service.listToString(Service.listExpenseByType(listOfExpenses, HOUSE_EXPENSES_TYPE)))
    elif params[0] in HOUSE_EXPENSES_TYPE:
        if len(params) == 1:
            print("All the expenses for the " + str(params[0] + " are:"))
            print(Service.listToString(Service.listExpenseByType(listOfExpenses, params[0])))
        elif len(params) != 3:
            print("Invalid input")
        else:
            try:
                value = int(params[2])
                if params[1] in operands:
                    print(Service.listToString(Service.listExpenseByTypeAndCondition(listOfExpenses, params[0], params[1], value)))
                else:
                    print("Invalid operand type")
            except ValueError:
                print("Invalid input type")
    else:
        print("Invalid input")


def maxCommand(params, listOfExpenses):

    if len(params) == 1 and params[0] == 'day':
        try:

            print("The day with the most expenses is: " + str(Service.maxOfDay(listOfExpenses)[0]) + " with " +
                  str(Service.maxOfDay(listOfExpenses)[1]) + " RON of expenses ")
        except Exception as e:
            print(e)
    else:
        print("Invalid input")


def readCommand():
    cmd = input("Give the command:\n")
    cmd.strip()
    if cmd.find(' ') == -1:
        command = cmd
        params = []
    else:
        command = cmd[0:cmd.find(' ')]
        params = cmd[cmd.find(' '):]
        params = params.split(';')
        auxParams = []
        for param in params:
            auxParams.append(param.split())
        params = auxParams
    return command, params


# tuple that contain all our constant expense types
HOUSE_EXPENSES_TYPE = ('housekeeping', 'food', 'transport', 'clothing', 'internet', 'others')


def sumCommand(params, listOfExpenses):
    global HOUSE_EXPENSES_TYPE
    if len(params) != 1:
        print("Invalid input: number of params isn't valid")
        return
    if params[0] in HOUSE_EXPENSES_TYPE:
        print("Sum of all " + str(params[0]) + " is equal to: " + str(Service.sumOfType(params[0], listOfExpenses)))
    else:
        print("Invalid input: category isn't valid")


def testInit(listOfExpenses):
    '''
        A function that initialize our list with a set of data
    '''
    listOfExpenses.append([1, 20, 'food'])
    listOfExpenses.append([2, 20, 'food'])
    listOfExpenses.append([3, 30, 'food'])
    listOfExpenses.append([9, 30, 'food'])
    listOfExpenses.append([22, 30, 'internet'])
    listOfExpenses.append([2, 40, 'clothing'])
    listOfExpenses.append([1, 20, 'clothing'])
    listOfExpenses.append([12, 20, 'internet'])
    listOfExpenses.append([13, 30, 'food'])
    listOfExpenses.append([29, 30, 'others'])
    listOfExpenses.append([22, 30, 'internet'])
    listOfExpenses.append([2, 30, 'clothing'])


def checkParams(params):
    if len(params) == 0:
        return False
    return True


def helpCommand(menuCommands):
    '''
        This functions print out all the commands with their example
        menuCommands -> dictionary
    '''
    for command in menuCommands:
        print(menuCommands[command][1])


def undoCommand(listOfExpenses):
    '''

    '''
    global undoList

    if len(undoList) == 0:
        print("Nothing to undo here")
        return
    else:
        listOfExpenses[:] = copy.deepcopy(undoList[len(undoList)-1])
        undoList.pop()
        print("Undo done with success")


def start():
    '''
        This is our main function that controlls our program 
    '''
    # a dictionary with all our menu options with key, message to print and function to call}
    menuCommands = {
        'add': (
            addExpenseCommand,
            '1.Add a new expense into the list. \n\t'
            'add <sum> <category>\n\t'
            'e.g.\n\t'
            'add 10 internet – add to the current day an expense of 10 RON for internet.'
        ),
        'insert': (
            insertExpenseCommand,
            '2.Insert a new expense into the list in a given day\n\t'
            'insert <day> <sum> <category>\n\t'
            'e.g\n\t'
            'insert 25 100 food – insert to day 25 an expense of 100 RON for food.'
        ),
        'remove': (
            removeExpenseCommand,
            '3. Modify expenses from the list.\n\t'
            'remove <day>\n\t'
            'remove <start day> to <end day>\n\t'
            'remove <category>\n\t'
            'e.g.\n\t'
            'remove 15 – remove all the expenses for day 15\n\t'
            'remove 2 to 9 – remove all the expenses between day 2 and day 9\n\t'
            'remove food – remove all the expenses for food from the current month.'
        ),
        'list': (
            listCommand,
            '4. Write the expenses having different properties\n\t'
            'list\n\t'
            'list <category>\n\t'
            'list <category> [ < | = | > ] <value>\n\t'
            'e.g\n\t'
            'list – write the entire list of expenses\n\t'
            'list food – write all the expenses for food.\n\t'
            'list food > 5 - writes all expenses for food with an amount of money > 5\n\t'
            'list internet = 44 - writes all expenses for internet with an amount of money = 44\n\t'
        ),
        'help': (
            helpCommand,
            '5. Show help'
        ),
        'sort': (
            sortCommand,
            '6.Write the list sorted by some criterias\n\t'
            'sort <day>\n\t'
            'sort <category>\n\t'
            'e.g.\n\t'
            'sort day – write the total daily expenses in ascending order by amount of money spent.\n\t'
            'sort food – write the daily expenses for category food in ascending order by amount of money\n\t'
            'spent.\n'
        ),
        'sum': (
            sumCommand,
            '7.Write the total expenses for a given category\n\t'
            'sum <category>\n\t'
            'e.g\n\t'
            'sum food – write the total expense for category food\n'
        ),
        'max': (
            maxCommand,
            '8.Write the day with the maximum expenses\n\t'
            'max <day>\n\t'
            'e.g\n\t'
            'max day – write the day with the maximum expenses.\n'
        ),
        'filter': (
            filterCommand,
            '9. Filter the list of expenses.\n\t'
            'filter <category>\n\t'
            'filter <category> [ < | = | > ] <value>\n\t'
            'e.g.\n\t'
            'filter food – keep only expenses in category food.\n\t'
            'filter books < 100 – keep only expenses in category books with amount of money < 100 RON\n'

        ),
        'undo': (
            undoCommand,
            ''
        )
    }
    listOfExpenses = []
    testInit(listOfExpenses)
    while True:
        cmd = readCommand()
        command = cmd[0]
        params = cmd[1]
        if command == 'exit':
            print("Program ends here with success")
            break
        elif command == 'undo':
            undoCommand(listOfExpenses)
        elif command == 'help':
            menuCommands['help'][0](menuCommands)
        elif command in menuCommands:
            if len(params) == 0:
                menuCommands[command][0](params, listOfExpenses)
            else:
                for param in params:
                    menuCommands[command][0](param, listOfExpenses)
        else:
            print("Invalid command")


def commandToString(cmd, params):
    return "The executed command is: " + str(cmd) + " " + str([str(a) + " " for a in params])


#Tests.runTests()
start()

