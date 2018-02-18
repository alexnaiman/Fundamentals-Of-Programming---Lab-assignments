import unittest

from Board import Board
from Cell import Cell


class Tests(unittest.TestCase):
    def testCell(self):
        c1 = Cell("human", 2, 4)
        c2 = Cell("human", 2, 4)
        self.assertEqual(c1, c2)
        self.assertEqual(c1.x, 2)

    def test_Board(self):
        b = Board(6, 7)
        self.assertEqual(b.width, 6)
        self.assertEqual(b.height, 7)
        self.assertEqual(b.isWinner("human"), False)
        b.move(1, "human")
        b.move(1, "human")
        b.move(1, "human")
        b.move(1, "human")
        self.assertEqual(b.isWinner("human"), True)
        b = Board(6, 7)
        self.assertEqual(b.width, 6)
        self.assertEqual(b.height, 7)
        self.assertEqual(b.isWinner("human"), False)
        b.move(1, "human")
        b.move(2, "human")
        b.move(3, "human")
        b.move(4, "human")
        self.assertEqual(b.isWinner("human"), True)
        b = Board(6, 7)
        self.assertEqual(b.width, 6)
        self.assertEqual(b.height, 7)
        self.assertEqual(b.isWinner("human"), False)
        b.move(1, "human")
        b.move(2, "human")
        b.move(3, "human")
        b.move(4, "human")
        b.move(2, "human")
        b.move(3, "human")
        b.move(4, "computer")
        b.move(3, "human")
        b.move(4, "human")
        b.move(4, "human")
        self.assertEqual(b.isWinner("human"), True)
