import unittest

from Controllers.ClientController import ClientController
from Controllers.MovieController import MovieController
from Controllers.RentalController import RentalController
from Models.Rental import Rental
from Repositories.Repository import Repository
from Services.RentalValidator import RentalValidator


class RentalTestCase(unittest.TestCase):
    def setUp(self):
        self.Rental = Rental('1', '2', '3', '2017-10-23', '2018-10-23', -1)
        self.repo = Repository('testRentals', 'testRentals')
        self.movieRepo = Repository('testMovies', 'TestClients')
        self.clientRepo = Repository('testClients', 'TestClients')
        self.controller = RentalController(self.repo, self.movieRepo, self.clientRepo)

    def test_strRental(self):
        self.assertEqual(str(self.Rental), '1, 2, 3, 2017-10-23, 2018-10-23, -1')

    def test_AddRental(self):
        open("testRentalsRental", 'w').close()
        open("testRentalsMovie", 'w').close()
        open("testRentalsClients", 'w').close()
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        mc.addMovie("1", "title", "sds", "action")
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        cc.addClient('1', 'Ghita')
        controller = RentalController(repo, cc, mc)
        self.assertEqual(controller.addRental('1', '1', '1', "2017-10-23", "2018-10-23", -1), True)

    def test_AddRental2(self):
        open("testRentalsRental", 'w').close()
        open("testRentalsMovie", 'w').close()
        open("testRentalsClients", 'w').close()
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        mc.addMovie("2", "title", "sds", "action")
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        cc.addClient('2', 'Ghita')
        controller = RentalController(repo, cc, mc)
        self.assertEqual(controller.addRental('2', '2', '2', "2017-10-23", "2018-10-23", -1), True)

    def test_removeRental(self):
        f = open("testRentalsRental", 'w')
        f.write("1, 1, 1,  2017-11-20, 2019-11-20, -1")
        f.close()
        f = open("testRentalsMovie", 'w')
        f.write("1, title, sdfs, action")
        f.close()
        f = open("testRentalsClients", 'w')
        f.write("1, title")
        f.close()
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        controller = RentalController(repo, cc, mc)
        self.assertEqual(controller.removeRental('1'), True)

    def test_removeRental2(self):
        f = open("testRentalsRental", 'w')
        f.write("2, 2, 2,  2017-11-20, 2019-11-20, -1")
        f.close()
        f = open("testRentalsMovie", 'w')
        f.write("2, title, sdfs, action")
        f.close()
        f = open("testRentalsClients", 'w')
        f.write("2, title")
        f.close()
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        controller = RentalController(repo, cc, mc)
        self.assertEqual(controller.removeRental('2'), True)

    def test_UpdateRental(self):
        f = open("testRentalsRental", 'w')
        f.write("1, 1, 1,  2017-11-20, 2019-11-20, -1")
        f.close()
        f = open("testRentalsMovie", 'w')
        f.write("1, title, sdfs, action")
        f.close()
        f = open("testRentalsClients", 'w')
        f.write("1, title")
        f.close()
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        controller = RentalController(repo, cc, mc)
        self.assertEqual(controller.updateRental('1', '1', '1', '1', '2017-01-23', '2017-11-20', -1), True)

    def test_GetAllRentals(self):
        f = open("testRentalsRental", 'w')
        f.write("1, 1, 1,  2017-11-20, 2019-11-20, -1")
        f.close()
        f = open("testRentalsMovie", 'w')
        f.write("1, title, sdfs, action")
        f.close()
        f = open("testRentalsClients", 'w')
        f.write("1, title")
        f.close()
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        controller = RentalController(repo, cc, mc)
        rental = Rental("1", "1", "1", "2017-11-20", "2019-11-20", "-1")
        self.assertEqual(controller.getAllRentals(), [rental])

    def test_getRentalById(self):
        f = open("testRentalsRental", 'w')
        f.write("1, 1, 1,  2017-11-20, 2019-11-20, -1")
        f.close()
        f = open("testRentalsMovie", 'w')
        f.write("1, title, sdfs, action")
        f.close()
        f = open("testRentalsClients", 'w')
        f.write("1, title")
        f.close()
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        controller = RentalController(repo, cc, mc)
        rental = Rental("1", "1", "1", "2017-11-20", "2019-11-20", "-1")
        self.assertEqual(controller.getRentalById(1), rental)

    def test_getRentalById2(self):
        f = open("testRentalsRental", 'w')
        f.write("2, 2, 2,  2017-11-20, 2019-11-20, -1")
        f.close()
        f = open("testRentalsMovie", 'w')
        f.write("2, title, sdfs, action")
        f.close()
        f = open("testRentalsClients", 'w')
        f.write("2, title")
        f.close()
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        controller = RentalController(repo, cc, mc)
        rental = Rental("2", "2", "2", "2017-11-20", "2019-11-20", "-1")
        self.assertEqual(controller.getRentalById(2), rental)

    def test_Rent(self):
        f = open("testRentalsRental", 'w')
        f.write("1, 2, 2,  2017-11-20, 2019-11-20, -1")
        f.close()
        f = open("testRentalsMovie", 'w')
        f.write("1, title, sdfs, action")
        f.close()
        f = open("testRentalsClients", 'w')
        f.write("1, title")
        f.close()
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        controller = RentalController(repo, cc, mc)
        self.assertEqual(controller.rent("2", "1", "1", "2017-11-20", "2018-11-20", -1), True)

    def test_returnedMovie(self):
        f = open("testRentalsRental", 'w')
        f.write("1, 2, 2,  2017-11-20, 2019-11-20, -1")
        f.close()
        f = open("testRentalsMovie", 'w')
        f.write("1, title, sdfs, action")
        f.close()
        f = open("testRentalsClients", 'w')
        f.write("1, title")
        f.close()
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        controller = RentalController(repo, cc, mc)
        self.assertEqual(controller.returnAMovie("1"), True)
        self.assertRaises(ValueError, controller.removeAllAppOfMovie, '2s')
        self.assertRaises(ValueError, controller.removeAllAppOfClient, '2s')
        self.assertRaises(ValueError, controller.updateClientIdFromRental, '2s', '2')

    def test_RentalSetters(self):
        r = Rental(1, 2, 3, "2017-10-20", "2017-11-20", "2018-01-20")
        r.id = 4
        r.movieId = 5
        r.clientId = 6
        r.returnedDate = "2017-12-20"
        r.dueDate = "2017-12-20"
        r.rentedDate = "2017-08-09"
        a = r.dueDate
        a = r.returnedDate
        self.assertNotEqual(r, Rental(4, 5, 6, "2017-12-20", "2017-12-20", "2017-08-09"))
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        controller = RentalController(repo, cc, mc)
        self.assertEqual(controller.lateRentals(), [])
        self.assertEqual(controller.allRentedMovies(), mc.getAllMovies())
        s = mc.getAllMovies()
        self.assertEqual(controller.mostRentedMoviesByNumber(), controller.mostRentedMoviesByNumber())
        self.assertEqual(controller.mostRentedMoviesByDays(), controller.mostRentedMoviesByDays())
        self.assertRaises(ValueError, controller.updateClientIdFromRental, "s", "2")
        self.assertRaises(ValueError, controller.updateClientIdFromRental, "2", "s")
        controller.removeAllAppOfClient("1")
        controller.removeAllAppOfMovie("1")
        controller.updateMovieIdFromRental("1", "1")
        controller.updateClientIdFromRental("1", "1")
        self.assertRaises(ValueError, controller.updateClientIdFromRental, "2", "s")
        self.assertRaises(ValueError, controller.updateClientIdFromRental, "s", "2")

    def test_ValidateRental(self):
        self.assertRaises(ValueError, RentalValidator.validate, "", "", "", "", "", "-29999999")
        self.assertRaises(ValueError, RentalValidator.validate, "", "", "", "", "", "-299999999")
        self.assertRaises(ValueError, RentalValidator.validate, "", "22222-2222", "22222-22222", "2222-22222",
                          "2222-22222", "2222-22-22")
        self.assertRaises(ValueError, RentalValidator.validate, '4', '5', '6', "2017-12-20", "2017-10-20", "2017-08-20")

    def test_raises(self):
        repo = Repository("testRentalsRental", "test")
        movieRepo = Repository("testRentalsMovie", "tes2")
        mc = MovieController(movieRepo)
        clientRepo = Repository("testRentalsClients", "test3")
        cc = ClientController(clientRepo)
        controller = RentalController(repo, cc, mc)
        self.controller.undo()
