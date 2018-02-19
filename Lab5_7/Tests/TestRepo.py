import unittest

from Models.Client import Client
from Repositories.BaseRepository import Repository
from Repositories.RepositoryException import RepositoryException


class RepoTestCase(unittest.TestCase):
    def setUp(self):
        self.__c0 = Client(1, "Ghita")
        self.__c1 = Client(2, "Marcel")
        self.__c2 = Client(3, "Birhan")
        self.__c3 = Client("4", "Erik")
        self.__c4 = Client(1, "Bbf")

    def test_Repo(self):
        self.r = Repository()
        self.r.create(self.__c0)
        self.assertEqual(self.r.getAll(), [self.__c0])
        self.assertEqual(len(self.r), 1)
        self.assertEqual("1, Ghita\n", str(self.r))
        self.assertEqual(self.__c0, self.__c0)
        self.r.create(self.__c1)
        self.assertEqual(self.r.find(10), False)
        self.r.update(self.__c4)
        self.assertEqual(self.__c4, self.r.find(self.__c4.id))
        self.assertRaises(RepositoryException, self.r.update, self.__c3)
        self.assertRaises(RepositoryException, self.r.create, self.__c0)
        self.assertRaises(RepositoryException, self.r.delete, 77)

        c = self.__c4
        self.r.delete(c.id)
        self.assertEqual(self.r.find(1), False)
