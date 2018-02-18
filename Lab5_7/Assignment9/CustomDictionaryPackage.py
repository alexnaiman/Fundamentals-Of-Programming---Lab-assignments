def filter(condition, list):
    for i in list:
        if condition(i):
            yield i


def sort(lisT, key=lambda x: x, comparator=lambda x, y: x < y, reverse=True):
    for i in range(len(lisT)):
        for j in range(i, len(lisT)):
            if comparator(key(lisT[i]), key(lisT[j])):
                lisT[i], lisT[j] = lisT[j], lisT[i]
    if reverse:
        lisT = reversed(lisT)


class CustomDict:
    def __init__(self):
        self.data = {}
        self.__i = 0

    def __setitem__(self, key, value):
        self.data[key] = value

    def values(self):
        return self.data.values()

    def keys(self):
        return self.data.keys()

    def __getitem__(self, item):
        return self.data[item]

    def __delitem__(self, key):
        del self.data[key]

    def __iter__(self):
        self.__i = 0
        return iter(self.data)

    def __next__(self):
        if self.__i < len(self.data.keys()) - 1:
            self.__i += 1
            return self.data[list(self.data.keys())[self.__i]]
        else:
            raise StopIteration
