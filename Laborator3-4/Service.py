from Model import *
import copy


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


def removeExpenseByStartEndDay(params, listOfExpense):
    '''
            Functions that remove a expense from period of time from the list of expenses
        in:
            - listOfExpenses: list of tuples of form (day, sum, type)
            - startDay: integer - first day from which we start to remove expenses
            - endDay: integer - last day from which we start to remove expenses
        out: boolean - True if there are expenses to be removed in the given period of time, False otherwise
    '''
    try:
        startDay = int(params[0])
        endDay = int(params[2])
    except ValueError:
        raise ValueError("Invalid day type: starDate and endDate must be integers")
    if not 0 < startDay < endDay <= 31:
        raise ValueError("Invalid day type: startDate and endDate must be between 1 and 30")
    auxList = listOfExpense
    listOfExpense[:] = filter(lambda a: startDay > a[0] or a[0] > endDay, listOfExpense)
    if auxList == listOfExpense:
        return False
    return True


def removeExpenseByDay(params, listOfExpenses):
    '''
            Functions that remove a expense by day from the list of expenses
        in:
            - listOfExpenses: list of tuples of form (day,sum,type)
            - day: integer
        out: boolean - True if there are expenses to be removed in the given day, False otherwise
    '''
    try:
        day = int(params[0])
    except ValueError:
        raise ValueError("Invalid input: To remove by day the given day cannot be string")
    auxList = copy.deepcopy(listOfExpenses)
    listOfExpenses[:] = filter(lambda a: a[0] != day, listOfExpenses)
    if auxList == listOfExpenses:
        return False
    return True


def addExpense(listOfExpenses, params):
    '''
        Functions that adds a new expense to the list of expenses
    in:
        - listOfExpenses: list of lists
        - params: list - (day,sum,type)
    out: boolean - True if that isn't any other expense with the same category in the current date, False otherwise
    '''
    expense = createExpenseToday(params)
    if len(params)!=2:
        raise ValueError("Invalid input: number of parameters isn't valid")
    for e in listOfExpenses:
        if e[0] == expense[0] and e[2] == expense[2]:
            return False
    else:
        listOfExpenses.append(expense)
        return True


def insertExpense(listOfExepenses, params):
    '''
            Functions that inserts a new expense to the list of expenses, if there is another expense with the given
        type in that day, it is overwritten
        in:
            - listOfExpenses: list of lists
            - params: list - (day,sum,type)
        out: boolean - always True because there aren't any conflicts
    '''
    expense = createExpense(params)
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
    auxList = []
    auxList[:] = listOfExpenses
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


def listExpenseByDay(listOfExpenses, day):
    '''
            Functions that lists the expenses by type
        in:
            - listOfExpenses: list of tuples of form (day, sum, type)
            - typeOfExpense: string - the type of expense by which we want to list the list
        out: list of tuple of form (day, sum, type)
    '''
    return list(filter(lambda a: a[0] == day, listOfExpenses))


def filterExpenseByType(listOfExpenses, typeOfExpense):
    '''
            Functions that filters the expenses by type
        in:
            - listOfExpenses: list of tuples of form (day, sum, type)
            - typeOfExpense: string - the type of expense by which we want to list the list
        out: true if we can filter the list, false otherwise
    '''
    auxList = copy.deepcopy((list(filter(lambda a: a[2] in typeOfExpense, listOfExpenses))))
    if auxList == listOfExpenses:
        return False
    listOfExpenses[:] = copy.deepcopy(auxList)
    return True


def filterExpenseByTypeAndCondition(listOfExpense, typeOfExpense, condition, value):
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
        if auxList == listOfExpense:
            return False
        listOfExpense[:] = copy.deepcopy(auxList)
        return True
    if condition == '<':
        auxList = listExpenseByType(listOfExpense, typeOfExpense)
        auxList[:] = filter(lambda a: a[1] < value, auxList)
        if auxList == listOfExpense:
            return False
        listOfExpense[:] = copy.deepcopy(auxList)
        return True
    if condition == '=':
        auxList = listExpenseByType(listOfExpense, typeOfExpense)
        auxList[:] = filter(lambda a: a[1] == value, auxList)
        if auxList == listOfExpense:
            return False
        listOfExpense[:] = copy.deepcopy(auxList)
        return True


def listExpenseByTypeAndCondition(listOfExpense, typeOfExpense, condition, value):
    '''
            Functions that lists the expenses by type and condition
        in:
            - listOfExpenses: list of lists of form (day, sum, type)
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


def sortType(typeOfExpense, listOfExpenses):
    '''
        Returns list of expenses from the given type in ascending order
    in:
        - listOfExpenses: list of lists of form (day, sum, type)
        - typeOfExpense: string - the type of expense by which we want to sort the list
    out:
        - listOfExpenses: list of lists of form (day, sum, type)
    '''
    auxList = listExpenseByType(listOfExpenses, typeOfExpense)
    auxList.sort(key=lambda x: x[1])
    return auxList


def sortDay(listOfExpenses):
    '''
            Returns  the total daily expenses in ascending order by amount of money spent.
        in:
           - listOfExpenses: list of lists of form (day, sum, type)
        out:
           - sortedList: list of lists of listsOfExpenses
    '''
    dayWithExpenses = getExpensesOfEachDay(listOfExpenses)
    dayWithExpenses.sort(key=lambda a: a[1])
    dayWithExpenses = list(reversed(dayWithExpenses))
    sortedList = []
    for day in dayWithExpenses:
        auxList = listExpenseByDay(listOfExpenses, day[0])
        sortedList.append(auxList)
    return sortedList


def sumOfType(type, listOfExpenses):
    '''
        Returns the total expenses for a given type
        in:
            - listOfExpenses: list of lists of form (day, sum, type)
        out:
            - summ: integer
    '''
    summ = 0
    for i in listExpenseByType(listOfExpenses, type):
        summ += i[1]
    return summ


def getDaysWithExpenses(listOfExpenses):
    '''
        Returns a set with the days in which we have expenses
        in:
            - listOfExpenses: list of lists of form (day, sum, type)
        out:
            - days: set of integers
    '''
    days = set([])
    for expense in listOfExpenses:
        days.add(expense[0])
    return days


def getExpensesOfEachDay(listOfExpenses):
    '''
        Returns the total daily expenses in a list of form tuples (day, total)
        in:
            - listOfExpenses: list of lists of form (day, sum, type)
        out:
            - dayWithExpense: list of tupples of form (day, total)
    '''
    dayWithExpenses = []
    days = getDaysWithExpenses(listOfExpenses)
    for day in days:
        sum = 0
        for expense in listOfExpenses:
            if expense[0] == day:
                sum += expense[1]
        dayWithExpenses.append((day, sum))
    return dayWithExpenses


def maxOfDay(listOfExpenses):
    '''
        Returns the day with the maximum amount of expenses as a tuple of form (day, total)
        in:
            - listOfExpenses: list of lists of form (day, sum, type)
        out:
            maxDay, maxTotal: integers
    '''
    dayWithExpenses = getExpensesOfEachDay(listOfExpenses)
    maxDay, maxTotal = -1, -1
    for i in dayWithExpenses:
        if i[1] > maxTotal:
            maxDay, maxTotal = i[0], i[1]
    return maxDay, maxTotal
