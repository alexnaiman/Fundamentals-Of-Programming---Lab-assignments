l = [0, "-", "+"]


def backIter():
    x = [0]  # candidate solution
    while len(x) > 0:
        choosed = False
        while (not choosed) and l.index(x[-1]) < len(l) - 1:
            x[-1] = l[l.index(x[-1]) + 1]  # increase the last component
            choosed = consistent(x)
        if choosed:
            if solution(x):
                solutionFound(x)
            x.append(0)  # expand candidate solution
        else:
            x.pop()  # go back one component


def consistent(s):
    return len(s) < n


def solution(s):
    summ = list2[0]
    if not len(s) == n - 1:
        return False
    for i in range(n - 1):
        if s[i] == "-":
            summ -= list2[i + 1]
        else:
            summ += list2[i + 1]
    return summ > 0


def solutionFound(s):
    print(s)


n = int(input("Give number"))
list2 = []
for i in range(n):
    list2.append(int(input(str(i) + ":")))

backIter()
print("test")
