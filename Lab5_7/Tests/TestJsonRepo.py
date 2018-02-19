from Models.Rental import Rental
from Repositories.JsonRepository import JsonRepo
from Tests.TestFileRepo import FileRepoTestCase


class JsonRepoTestCase(FileRepoTestCase):
    def setUp(self):
        FileRepoTestCase.setUp(self)
        self.jsonRepo = JsonRepo("../Tests/testJsonRepo", "Repo for test", Rental.rentalFromJson)
        open("../Tests/testJsonRepo", "w").close()

    def tearDown(self):
        open("testFileRepo", "w").close()

    def test_JsonRepo(self):
        self.test_FileRepo()
        c = Rental(4, 4, 4, "2017-12-10", "2017-12-20", "2017-12-14")
        self.jsonRepo.createItem(c)
        self.assertEqual(self.jsonRepo.getItemById(4), c)
        self.jsonRepo.updateItemById(4, Rental(4, 4, 4, "2017-12-12", "2017-12-22", "2017-12-24"))
        self.jsonRepo.deleteItemById(4)
        self.assertEqual(self.jsonRepo.getItemById(4), False)
