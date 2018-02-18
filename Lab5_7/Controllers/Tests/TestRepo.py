import unittest

from Repositories.Repository import Repository


class RentalTestCase(unittest.TestCase):
    def setUp(self):
        self.repo = Repository("", "")
        pass

    def test_OpenFile(self):
        self.assertRaises(IOError, self.repo.createItem, "")
        self.assertRaises(IOError, self.repo.getItemById, "")
        self.assertRaises(IOError, self.repo.updateItemById, "2", 2)
        self.assertRaises(IOError, self.repo.getItemById, "")
        self.assertRaises(IOError, self.repo.getAllLines)
