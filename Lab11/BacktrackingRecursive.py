l = ["+", "-"]


def backRec(x):
    for j in l:
        x.append(j)
        if consistent(x):
            if solution(x):
                solutionFound(x)
            backRec(x)
        x.pop()


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

backRec([])
