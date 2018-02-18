def expenseToString(expense):
    '''
        Converts a list of form (day, sum, category) to a formated string
        in:
            expense - list of form (day, sum, category)
        out:
            string
    '''
    return "Day: " + str(expense[0]) + " Sum: " + str(expense[1]) + " Category: " + str(expense[2])

