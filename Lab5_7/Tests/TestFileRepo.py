from Models.Client import Client
from Repositories.FileRepository import FileRepository
from Tests.TestRepo import RepoTestCase


class FileRepoTestCase(RepoTestCase):
    def setUp(self):
        RepoTestCase.setUp(self)
        self.fileRepo = FileRepository("../Tests/testFileRepo", "Repo for test", Client.clientToFile,
                                       Client.clientFromFile)
        with open("../Tests/testFileRepo", "w") as f:
            f.write("3, Birhan\n")

    def tearDown(self):
        open("testFileRepo", "w").close()

    def test_FileRepo(self):
        self.test_Repo()
        self.assertEqual(self.fileRepo.getItemById(3), Client(3, "Birhan"))
        c = Client(4, "numeFaaaain")
        self.fileRepo.createItem(c)
        self.assertEqual(self.fileRepo.getItemById(4), c)
        self.fileRepo.updateItemById(4, Client(4, "lapteeee"))
        self.fileRepo.deleteItemById(4)
        self.assertEqual(self.fileRepo.getItemById(4), False)
