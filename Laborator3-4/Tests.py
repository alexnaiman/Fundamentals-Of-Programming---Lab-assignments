import Service


def testGetDaysWithExpenses():
    assert Service.getDaysWithExpenses([[1, 20, 'food'], [2, 20, 'food'], [3, 20, 'food'], [3, 20, 'food']]) == {1, 2,
                                                                                                                 3}
    assert Service.getDaysWithExpenses([[3, 20, 'food'], [5, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]) != {1, 2,
                                                                                                                 3}
    assert Service.getDaysWithExpenses([[5, 20, 'food'], [6, 20, 'food'], [9, 20, 'food'], [10, 20, 'food']]) == {5, 6,
                                                                                                                  9, 10}
    assert Service.getDaysWithExpenses([[1, 20, 'food'], [4, 20, 'food'], [4, 20, 'food'], [1, 20, 'food']]) == {1, 4}
    assert Service.getDaysWithExpenses([[2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food']]) != {1, 2,
                                                                                                                 3}
    print("testGetDaysWithExpenses passed")


def testGetExpensesOfEachDay():
    assert Service.getExpensesOfEachDay([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]) == [
        (1, 60), (3, 20)]
    assert Service.getExpensesOfEachDay([[3, 20, 'food'], [5, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]) != [
        (1, 40), (3, 20)]
    assert Service.getExpensesOfEachDay(
        [[5, 20, 'food'], [6, 20, 'food'], [5, 20, 'food'], [10, 20, 'food'], [10, 20, 'food']]) == [(10, 40), (5, 40),
                                                                                                     (6, 20)]
    assert Service.getExpensesOfEachDay([[1, 20, 'food'], [4, 20, 'food'], [4, 20, 'food'], [1, 20, 'food']]) == [
        (1, 40), (4, 40)]
    assert Service.getExpensesOfEachDay([[2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food']]) == [
        (2, 80)]
    print("testGetExpensesOfEachDay passed")


def testMaxOfDay():
    assert Service.maxOfDay([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]) == (1, 60)
    assert Service.maxOfDay([[3, 20, 'food'], [5, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]) != (3, 20)
    assert Service.maxOfDay(
        [[5, 20, 'food'], [6, 20, 'food'], [5, 20, 'food'], [10, 20, 'food'], [10, 20, 'food']]) == (10, 40)
    assert Service.maxOfDay([[1, 20, 'food'], [4, 20, 'food'], [4, 20, 'food'], [1, 20, 'food']]) == (1, 40)
    assert Service.maxOfDay([[2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food']]) == (2, 80)
    print("testMaxOfDay passed")


def testSumOfType():
    assert Service.sumOfType('food', [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [5, 20, 'food']]) == 80
    assert Service.sumOfType('internet', [[3, 20, 'food'], [5, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]) == 0
    assert Service.sumOfType('internet',
                             [[5, 20, 'food'], [6, 20, 'internet'], [5, 20, 'food'], [10, 20, 'food'],
                              [10, 20, 'food']]) == 20
    assert Service.sumOfType('food', [[1, 20, 'food'], [4, 20, 'food'], [4, 20, 'food'], [1, 20, 'food']]) != 50
    assert Service.sumOfType('clothing', [[2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food']]) != 20
    print("testSumOfType passed")


def testSortDay():
    assert Service.sortDay([[1, 20, 'food'], [1, 20, 'internet'], [3, 20, 'food']]) == [
        [[1, 20, 'food'], [1, 20, 'internet']],
        [[3, 20, 'food']]]
    assert Service.sortDay([[1, 20, 'food'], [1, 20, 'clothing'], [3, 20, 'food']]) != [[[1, 20,
                                                                                          'food'],
                                                                                         [1, 20,
                                                                                          'internet']],
                                                                                        [[3, 20,
                                                                                          'food']]]
    assert Service.sortDay([[2, 20, 'food'], [1, 20, 'internet'], [3, 20, 'food'], [4, 20, 'food']]) == [
        [[4, 20, 'food']], [[3, 20, 'food']], [[2, 20, 'food']], [[1, 20, 'internet']]]
    print("testSortDay passed")


def testSortType():
    assert Service.sortType('food', [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [5, 20, 'food']]) == [
        [1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [5, 20, 'food']]
    assert Service.sortType('internet', [[3, 20, 'food'], [5, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]) == []
    assert Service.sortType('internet', [[5, 20, 'food'], [6, 20, 'internet'], [5, 20, 'food'], [10, 20, 'food'],
                                         [10, 20, 'food']]) != [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'],
                                                                [5, 20, 'food']]
    assert Service.sortType('food', [[1, 20, 'food'], [4, 20, 'food'], [4, 20, 'food'], [1, 20, 'food']]) == [
        [1, 20, 'food'], [4, 20, 'food'], [4, 20, 'food'], [1, 20, 'food']]
    assert Service.sortType('clothing', [[2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food']]) == []
    print("testSumOfType passed")


def testListExpenseByTypeAndCondition():
    assert Service.listExpenseByTypeAndCondition([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                                 'food', '<', 20) == []
    assert Service.listExpenseByTypeAndCondition([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                                 'food', '=', 20) == [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'],
                                                                      [1, 20, 'food']]
    assert Service.listExpenseByTypeAndCondition(
        [[1, 20, 'food'], [1, 30, 'internet'], [3, 20, 'food'], [1, 20, 'food']], 'internet', '>', 20) == [
               [1, 30, 'internet']]
    assert Service.listExpenseByTypeAndCondition([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                                 'food', '>', 10) != []
    assert Service.listExpenseByTypeAndCondition([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                                 'food', '>', 0) == [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'],
                                                                     [1, 20, 'food']]
    assert Service.listExpenseByTypeAndCondition([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                                 'food', '<', 20) != [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'],
                                                                      [1, 20, 'food']]
    print("testListExpenseByTypeAndCondition passed")



def testFilterExpenseByType():
    assert not Service.filterExpenseByType([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                       'food')
    assert not Service.filterExpenseByType([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                       'food')
    assert  Service.filterExpenseByType(
        [[1, 20, 'food'], [1, 30, 'internet'], [3, 20, 'food'], [1, 20, 'food']], 'internet')
    assert not Service.filterExpenseByType([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                       'food')
    assert not Service.filterExpenseByType([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                       'food')
    assert not Service.filterExpenseByType([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                       'food')
    print("testFilterExpenseByType passed")


def testListExpenseByDay():
    assert Service.listExpenseByDay([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food']], 1) != [[1, 20, 'food'],
                                                                                                [1, 20, 'internet']]

    assert Service.listExpenseByDay([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']], 2) != [
        [3, 20, 'food']]
    assert Service.listExpenseByDay(
        [[1, 20, 'food'], [1, 30, 'internet'], [3, 20, 'food'], [1, 20, 'food']], 3) == [[3, 20, 'food']]
    assert Service.listExpenseByDay([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                    3) != []
    assert Service.listExpenseByDay([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                    4) == []
    assert Service.listExpenseByDay([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'clothing']],
                                    3) != [[1, 20, 'food'], [1, 20, 'internet']]
    print("testListExpenseByDay passed")


def testListExpenseByType():
    assert Service.listExpenseByType([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                     'food') == [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]

    assert Service.listExpenseByType([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                     'food') == [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]
    assert Service.listExpenseByType(
        [[1, 20, 'food'], [1, 30, 'internet'], [3, 20, 'food'], [1, 20, 'food']], 'internet') == [[1, 30, 'internet']]
    assert Service.listExpenseByType([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                     'food') != [[1, 30, 'internet']]
    assert Service.listExpenseByType([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                     'food') == [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]

    assert Service.listExpenseByType([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                     'food') == [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]
    print("testListExpenseByType passed")


def testRemoveExpenseByType():
    assert Service.removeExpenseByType('food', [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']])

    assert Service.removeExpenseByType('food', [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']])
    assert Service.removeExpenseByType('food',
                                       [[1, 20, 'food'], [1, 30, 'internet'], [3, 20, 'food'], [1, 20, 'food']])
    assert Service.removeExpenseByType('internet',
                                       [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']]) != [
               [1, 30, 'internet']]
    assert not Service.removeExpenseByType('clothing', [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']])
    assert not Service.removeExpenseByType('housekeeping', [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],)

    print("testRemoveExpenseByType passed")


def testInsertExpense():
    assert Service.insertExpense([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                 ([1, 20, 'internet']))

    assert Service.insertExpense([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                     [3, 30, 'internet'])
    assert Service.insertExpense([[1, 20, 'food'], [1, 30, 'internet'], [3, 20, 'food'], [1, 20, 'food']],
                                     [3, 30, 'food'])
    assert Service.insertExpense([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                 [3, 30, 'internet'])
    assert Service.insertExpense([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                 [3, 30, 'internet'])

    assert Service.insertExpense([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                 [3, 30, 'internet'])
    print("testInsertExpense passed")


def testAddExpense():
    assert Service.addExpense([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                 ([20, 'internet']))

    assert Service.addExpense([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                 [30, 'internet'])
    assert Service.addExpense([[1, 20, 'food'], [1, 30, 'internet'], [3, 20, 'food'], [1, 20, 'food']],
                                 [30, 'food'])
    assert Service.addExpense([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                 [30, 'internet'])
    assert Service.addExpense([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                 [30, 'internet'])

    assert Service.addExpense([[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']],
                                 [30, 'internet'])
    print("testAddExpense passed")


def testRemoveExpenseByDay():
    assert not Service.removeExpenseByDay([2], [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [5, 20, 'food']])
    assert not Service.removeExpenseByDay([4], [[3, 20, 'food'], [5, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']])
    assert Service.removeExpenseByDay([6], [[5, 20, 'food'], [6, 20, 'internet'], [5, 20, 'food'], [10, 20, 'food'],
                                         [10, 20, 'food']]) != [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'],
                                                                [5, 20, 'food']]
    assert not Service.removeExpenseByDay([2], [[1, 20, 'food'], [4, 20, 'food'], [4, 20, 'food'], [1, 20, 'food']]) == [
        [1, 20, 'food'], [4, 20, 'food'], [4, 20, 'food'], [1, 20, 'food']]
    assert not Service.removeExpenseByDay([2], [[2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food']]) == []
    print("testRemoveExpenseByDay passed")


def testRemoveExpenseByStartEndDay():
    assert not Service.removeExpenseByDay(['4', 'to', '5'], [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'], [5, 20, 'food']])
    assert Service.removeExpenseByDay(['1', 'to', '5'], [[3, 20, 'food'], [5, 20, 'food'], [3, 20, 'food'], [1, 20, 'food']])
    assert Service.removeExpenseByDay(['2', 'to', '5'], [[5, 20, 'food'], [6, 20, 'internet'], [5, 20, 'food'], [10, 20, 'food'],
                                            [10, 20, 'food']]) != [[1, 20, 'food'], [1, 20, 'food'], [3, 20, 'food'],
                                                                   [5, 20, 'food']]
    assert not Service.removeExpenseByDay(['3', 'to', '8'],
                                          [[1, 20, 'food'], [4, 20, 'food'], [4, 20, 'food'], [1, 20, 'food']]) == [
                   [1, 20, 'food'], [4, 20, 'food'], [4, 20, 'food'], [1, 20, 'food']]
    assert not Service.removeExpenseByDay(['1', 'to', '9'],
                                          [[2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food'], [2, 20, 'food']]) == []
    print("testRemoveExpenseByStartEndDay passed")


def testCreateExpense():
    assert Service.createExpense(['30', '20', 'internet'])
    assert Service.createExpense(['30', '40', 'food'])
    assert Service.createExpense(['10', '20', 'clothing'])
    assert Service.createExpense(['10', '20', 'internet'])
    assert Service.createExpense(['30', '4000', 'housekeeping'])
    print("testCreateExpense passed")


def testCreateExpenseToday():
    assert Service.createExpenseToday([20, 'internet']) == [30, 20, 'internet']
    assert Service.createExpenseToday([40, 'food']) == [40, 'food']
    assert Service.createExpenseToday([20, 'clothing']) == [20, 'clothing']
    assert Service.createExpenseToday([10, 'internet']) == [10, 'internet']
    assert Service.createExpenseToday([4000, 'housekeeping']) == [4000, 'housekeeping']
    print("testCreateExpenseToday passed")


def runTests():
    testGetDaysWithExpenses()
    testGetExpensesOfEachDay()
    testMaxOfDay()
    testSumOfType()
    testSortDay()
    testSortType()
    testListExpenseByTypeAndCondition()
    testFilterExpenseByType()
    testListExpenseByDay()
    testListExpenseByType()
    testRemoveExpenseByType()
    testInsertExpense()
    testAddExpense()
    testRemoveExpenseByDay()
    testRemoveExpenseByStartEndDay()
    testCreateExpense()