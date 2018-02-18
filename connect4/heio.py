def functieCuRaise(x):
    if x == 1:
        raise ValueError
    elif x == 2:
        raise TypeError
    elif x == 3:
        raise IOError
    return True


def testFunctieCuRaise():
    try:
        functieCuRaise(1)
        assert False
    except ValueError:
        print("test passed")  # a aruncat eroare de tipul ValueError deci e oki
        assert True

    try:
        functieCuRaise(2)
        assert False
    except TypeError:
        print("test passed")

        assert True

    try:
        functieCuRaise(3)
        assert False
    except IOError:
        print("test passed")
        assert True


testFunctieCuRaise()
