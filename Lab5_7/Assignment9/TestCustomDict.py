import unittest

from Assignment9.CustomDictionaryPackage import CustomDict, filter, sort


class TestDict(unittest.TestCase):
    def test_CustomDict(self):
        dictt = CustomDict()
        dictt[1] = 2
        dictt[3] = 4
        dictt[5] = 6
        dictt[7] = 8
        for i in dictt.keys():
            self.assertEqual(dictt[i], int((i + 1)))
        self.assertEqual(list(dictt.keys()), [1, 3, 5, 7])
        self.assertEqual(list(dictt.values()), [2, 4, 6, 8])
        l = list(filter(lambda a: a > 4, dictt.values()))
        l2 = list(filter(lambda a: a > 2, dictt.values()))
        self.assertEqual(l2, [4, 6, 8])
        self.assertEqual(l, [6, 8])
        sort(l2, reverse=True)
        self.assertEqual(l2, [8, 6, 4])
