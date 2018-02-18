from Model import *


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