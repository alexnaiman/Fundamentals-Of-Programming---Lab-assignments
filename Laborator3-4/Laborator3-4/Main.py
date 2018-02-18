import datetime


def addExpense(listOfExpenses, expense):
    '''
        Functions that adds a new expense to the list of expenses
    in:
        - listOfExpenses: list of lists
        - expense: list - (day,sum,type)
    out: boolean - True if that isn't any other expense with the same category in the current date, False otherwise
    '''
    for e in listOfExpenses:
        if e[0] == expense[0] and e[2] == expense[2]:
            return False
    else:
        listOfExpenses.append(expense)
        return True


def insertExpense(listOfExepenses, expense):
    '''
            Functions that inserts a new expense to the list of expenses, if there is another expense with the given
        type in that day, it is overwritten
        in:
            - listOfExpenses: list of lists
            - expense: list - (day,sum,type)
        out: boolean - always True because there aren't any conflicts
        '''
    auxExpense = -1
    for i in range(len(listOfExepenses)):
        if listOfExepenses[i][0] == expense[0] and listOfExepenses[i][2] == expense[2]:
            auxExpense = i
    if auxExpense != -1:
        listOfExepenses[auxExpense] = expense
    else:
        listOfExepenses.append(expense)
    return True


def removeExpenseByDay(day, listOfExpenses):
    '''
            Functions that remove a expense by day from the list of expenses
        in:
            - listOfExpenses: list of tuples of form (day,sum,type)
            - day: integer
        out: boolean - True if there are expenses to be removed in the given day, False otherwise
    '''
    auxList = listOfExpenses
    listOfExpenses[:] = filter(lambda a: a[0] != day, listOfExpenses)
    if auxList == listOfExpenses:
        return False
    return True


def removeExpenseByStartEndDay(startDay, endDay, listOfExpense):
    '''
            Functions that remove a expense from period of time from the list of expenses
        in:
            - listOfExpenses: list of tuples of form (day, sum, type)
            - startDay: integer - first day from which we start to remove expenses
            - endDay: integer - last day from which we start to remove expenses
        out: boolean - True if there are expenses to be removed in the given period of time, False otherwise
    '''
    auxList = listOfExpense
    listOfExpense[:] = filter(lambda a: startDay > a[0] or a[0] > endDay, listOfExpense)
    if auxList == listOfExpense:
        return False
    return True


def removeExpenseByType(typeOfExepense, listOfExpenses):
    '''
            Functions that remove a expense from period of time from the list of expenses
        in:
            - listOfExpenses: list of tuples of form (day, sum, type)
            - typeOfExpense: string - the type of expense we want to remove
        out: boolean - True if there are expenses to be removed that are the given type, False otherwise
    '''
    auxList = listOfExpenses
    listOfExpenses[:] = filter(lambda a: a[2] != typeOfExepense, listOfExpenses)
    if auxList == listOfExpenses:
        return False
    return True


def listExpenseByType(listOfExpenses, typeOfExpense):
    '''
            Functions that lists the expenses by type
        in:
            - listOfExpenses: list of tuples of form (day, sum, type)
            - typeOfExpense: string - the type of expense by which we want to list the list
        out: list of tuple of form (day, sum, type)
    '''
    return list(filter(lambda a: a[2] in typeOfExpense, listOfExpenses))


def listExpenseByTypeAndCondition(listOfExpense, typeOfExpense, condition, value):
    '''
            Functions that lists the expenses by type and condition
        in:
            - listOfExpenses: list of tuples of form (day, sum, type)
            - typeOfExpense: string - the type of expense by which we want to list the list
            - condition: string - one of (<, =, >)
            - value: integer - value with which we verify the condition
        out: list of list of form (day, sum, type)
    '''
    if condition == '>':
        auxList = listExpenseByType(listOfExpense, typeOfExpense)
        auxList[:] = filter(lambda a: a[1] > value, auxList)
        return auxList
    if condition == '<':
        auxList = listExpenseByType(listOfExpense, typeOfExpense)
        auxList[:] = filter(lambda a: a[1] < value, auxList)
        return auxList
    if condition == '=':
        auxList = listExpenseByType(listOfExpense, typeOfExpense)
        auxList[:] = filter(lambda a: a[1] == value, auxList)
        return auxList


def addExpenseCommand(params, listOfExpenses):
    '''
            A wrapper function that check the params of the 'add' command, converts the strings to integers,
        links the data input to the functions that modifies directly the list
        in:
            - listOfExpenses: list of tuples of form (day, sum, type)
            - params: list - (<sum>, <category>)
    '''
    if len(params) < 2:
        print("Invalid data type")
    else:
        try:
            params[0] = int(params[0])
        except ValueError:

            print("Invalid data type: sum cannot be string")
            return
        now = datetime.datetime.now()
        global HOUSE_EXPENSES_TYPE
        if params[1] not in HOUSE_EXPENSES_TYPE:
            print("Invalid data type: expense type isn't valid")
            return
        else:
            expense = [now.day, params[0], params[1]]
            if not addExpense(listOfExpenses, expense):
                print("Expense was not valid")
            else:
                print("Expense added to the list")


def insertExpenseCommand(params, listOfExpenses):
    '''
           A wrapper function that check the params of the 'insert' command, converts the strings to integers,
        links the data input to the functions that modifies directly the list
        in:
           - listOfExpenses: list of lists of form (day, sum, type)
           - params: list - <day> <sum> <category>
    '''
    if len(params) < 3:
        print("Invalid data type")
    else:
        try:
            params[0] = int(params[0])
        except ValueError:
            print("Invalid data type: sum cannot be string")
            return
        try:
            params[1] = int(params[1])
        except ValueError:
            print("Invalid data type: sum cannot be string")
            return

        if not 0 < params[0] < 31:
            print("Invalid data type: day must be between 1 and 30")
            return

        global HOUSE_EXPENSES_TYPE
        if params[2] not in HOUSE_EXPENSES_TYPE:
            print("Invalid data type: expense type isn't valid")
            return
        else:
            expense = [params[0], params[1], params[2]]
            if not insertExpense(listOfExpenses, expense):
                print("Expense was not valid")
            else:
                print("Expense added to the list")


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
    if not checkParams(params):
        print("Invalid Command")
        return
    if len(params) < 2:
        if params[0] in HOUSE_EXPENSES_TYPE:
            if not removeExpenseByType(params[0], listOfExpenses):
                print("Day expenses were removed")
            else:
                print("The given category haven't had any expenses")
        else:
            try:
                params = int(params[0])
                print(params)
                if not removeExpenseByDay(params, listOfExpenses):
                    print("Day expenses were removed")
                else:
                    print("The given day haven't had any expenses")
            except ValueError:
                print("Invalid command")
    elif len(params) < 4 and params[1] == 'to':
        try:
            startDay = int(params[0])
            endDay = int(params[2])
            if not 0 < startDay < endDay <= 31:
                print("Invalid day type: startDate and endDate must be between 1 and 30")
                return
            if not removeExpenseByStartEndDay(startDay, endDay, listOfExpenses):
                print("Day expenses were removed")
                return
            else:
                print("The days between didn't have any expenses")
        except ValueError:

            print('Invalid day type: starDate and endDate must be integers')
            return

    else:
        print("Invalid command")


def expenseToString(expense):
    '''
        Converts a list of form (day, sum, category) to a formated string
        in:
            expense - list of form (day, sum, category)
        out:
            string
    '''
    return "Day: " + str(expense[0]) + " Sum: " + str(expense[1]) + " Category: " + str(expense[2])


def listToString(list):
    '''
        Converts a list of lists of form (day, sum, category) to a formated string
        in:
            list - list of lists of form (day, sum, category)
        out:
            string
    '''
    string = ""
    if list is None:
        return "No expense here"
    elif len(list) == 0:
        return "No expense here"
    for i in list:
        string += "\n"+expenseToString(i)
    return string


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
        print(listToString(listExpenseByType(listOfExpenses, HOUSE_EXPENSES_TYPE)))
    elif params[0] in HOUSE_EXPENSES_TYPE:
        if len(params) == 1:
            print("All the expenses for the " + str(params[0] + " are:"))
            print(listToString(listExpenseByType(listOfExpenses, params[0])))
        elif len(params) != 3:
            print("Invalid input")
        else:
            try:
                value = int(params[2])
                if params[1] in operands:
                    print(listToString(listExpenseByTypeAndCondition(listOfExpenses, params[0], params[1], value)))
                else:
                    print("Invalid operand type")
            except ValueError:
                print("Invalid input type")
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


def testInit(listOfExpenses):
    '''
        A function that initialize our list with a set of data
    '''
    listOfExpenses.append([1, 20, 'food'])
    listOfExpenses.append([2, 20, 'food'])
    listOfExpenses.append([3, 30, 'food'])
    listOfExpenses.append([9, 30, 'food'])
    listOfExpenses.append([22, 30, 'internet'])
    listOfExpenses.append([2, 30, 'clothing'])
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


def commandToString(cmd,params):
    return "The executed command is: " + str(cmd) + " " + str([str(a) + " " for a in params])



start()

