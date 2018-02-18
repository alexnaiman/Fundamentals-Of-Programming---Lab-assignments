import datetime
HOUSE_EXPENSES_TYPE = ('housekeeping', 'food', 'transport', 'clothing', 'internet', 'others')


def expenseToString(expense):
    '''
        Converts a list of form (day, sum, category) to a formated string
        in:
            expense - list of form (day, sum, category)
        out:
            string
    '''
    return "Day: " + str(expense[0]) + " Sum: " + str(expense[1]) + " Category: " + str(expense[2])


def createExpense(params):
    '''
        A constructor for an expense object that also verifies the type of each param and raises errors
        in:
                - params: list - (day,sum,type)
        out:
                - expense: (day,sum,type)
    '''
    if len(params) < 2:
        raise ValueError("Invalid data type")
    else:
        try:
            params[0] = int(params[0])
        except ValueError:
            raise ValueError("Invalid data type: sum cannot be string")
        try:
            params[1] = int(params[1])
        except Exception:
            raise Exception("Invalid data type: sum cannot be string")
        if not 0 < params[0] < 32:
            raise Exception("Invalid data type: day must be between 1 and 30")
        if params[1] < 0:
            raise Exception("Invalid data type: sum cannot be negative")
        try:
            if params[2] not in HOUSE_EXPENSES_TYPE:
                raise Exception("Invalid data type: expense type isn't valid")
        except Exception:
            raise Exception("Invalid data type: expense type cannot be null")
        if params[2] not in HOUSE_EXPENSES_TYPE:
            raise Exception("Invalid data type: expense type isn't valid")

        expense = [params[0], params[1], params[2]]
        return expense


def createExpenseToday(params):
    '''
        A wrap up functions of the createExpense functions that create a new expense with the given params today
        in:
            - params: list - (day,sum,type)
        out: true if we can add the new expense, false otherwise
    '''
    now = datetime.datetime.now()
    auxParams = [now.day]
    for param in params:
        auxParams.append(param)
    return createExpense(auxParams)

