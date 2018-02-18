import unittest
from Models.Movie import Movie
from Repositories.Repository import Repository
from Controllers.MovieController import MovieController
from Services.MovieValidator import MovieValidator


class MovieTestCase(unittest.TestCase):
    def setUp(self):
        self.movie = Movie(3, 'Titanic4', 'supers', 'action')
        self.repo = Repository('testMovies', 'testMovies')
        self.controller = MovieController(self.repo)
        if self.controller.getMovieById(77) is not False:
            self.controller.removeMovie(77)
        if self.controller.getMovieById(772) is not False:
            self.controller.removeMovie(772)
        if self.controller.getMovieById(773) is not False:
            self.controller.removeMovie(773)
        if self.controller.getMovieById(23) is False:
            self.controller.addMovie("23", "title", "description", "action")
        if self.controller.getMovieById('233333') is not False:
            self.controller.removeMovie('233333')
        if self.controller.getMovieById(20) is False:
            self.controller.addMovie("20", "title", "description", "action")
        if self.controller.getMovieById(200) is False:
            self.controller.addMovie("200", "title", "description", "action")
        if self.controller.getMovieById(90) is False:
            self.controller.addMovie("90", "title", "description", "action")
        if self.controller.getMovieById(123) is False:
            self.controller.addMovie("123", "title", "description", "action")
        if self.controller.getMovieById(234) is False:
            self.controller.addMovie("234", "title", "description", "action")
        if self.controller.getMovieById(33) is False:
            self.controller.addMovie("33", "title", "description", "action")
        if self.controller.getMovieById(90) is not False:
            self.controller.removeMovie(99)
        if self.controller.getMovieById(323) is False:
            self.controller.addMovie("323", "title", "description", "action")
        if self.controller.getMovieById(929) is not False:
            self.controller.removeMovie(929)
        if self.controller.getMovieById(33) is False:
            self.controller.addMovie("333", "title", "description", "action")
        if self.controller.getMovieById(939) is not False:
            self.controller.removeMovie(939)

    def test_strMovie(self):
        self.movie.id = 3
        self.movie.genre = 'action'
        self.movie.title = 'Titanic4'
        self.movie.description = 'supers'
        m = Movie(3, 'sd', 'sds', 'action')
        self.assertNotEqual(m, self.movie)
        m = self.movie
        self.assertEqual(m, self.movie)
        self.assertEqual(str(self.movie), '3, Titanic4, supers, action')

    def test_AddMovie(self):
        self.assertEqual(self.controller.addMovie('772', 'nume', 'descriere', 'action'), True)

    def test_AddMovie2(self):
        self.controller.addMovie("10000", "sd", "sdf", "action")
        self.assertRaises(ValueError, self.controller.addMovie, "10000", "df", "sdf", "action")
        self.controller.removeMovie("10000")

    def test_AddMovie3(self):
        self.assertEqual(self.controller.addMovie('773', 'nume', 'descriere', 'action'), True)

    def test_RemoveMovie(self):
        self.assertEqual(self.controller.removeMovie(20), True)

    def test_RemoveMovie2(self):
        self.assertRaises(ValueError, self.controller.removeMovie, "sdfgs")

    def test_UpdateMovie(self):
        self.assertEqual(self.controller.updateMovie('23', '233333', "teeest2", "sdfsdfssfs", "action"), True)

    def test_UpdateMovie2(self):
        self.assertRaises(ValueError, self.controller.updateMovie, '23d', '233333', "teeest2", "sdfsdfssfs", "action")

    def test_UpdateMovie3(self):
        self.assertRaises(ValueError, self.controller.updateMovie, '23', '2333dd33', "teeest2", "sdfsdfssfs", "action")

    def test_UpdateMovie4(self):
        self.controller.addItem(Movie(20000000000, "sds", "sdfs", "action"))
        self.assertRaises(ValueError, self.controller.updateMovie, '23', '233333', "", "sdfsdfssfs", "action")
        self.controller.removeMovie(20000000000)

    def test_UpdateMovie5(self):
        self.controller.addItem(Movie(20000000000, "sds", "sdfs", "action"))
        # self.controller.addItem(Movie(200000000000,"sds","sdfs","action"))
        # self.assertRaises(ValueError, self.controller.updateMovie, '20000000000', '200000000000', "sds", "sdfsdfssfs", "action")
        # self.controller.removeMovie(20000000000),
        # self.controller.removeMovie(20000000000),
        # self.controller.addMovie("9987", "sd", "sd", "action")
        # self.controller.addMovie("9988", "sd", "sd", "action")
        # self.assertRaises(ValueError, self.controller.updateMovie,"9987", "9988", "d", "d", "action")
        # self.controller.removeMovie(9987)
        # self.controller.removeMovie(9988)

    def test_UpdateMovieName(self):
        self.assertEqual(self.controller.updateMovieName('90', 'nuuummmeee tesr'), True)

    def test_UpdateMovieName2(self):
        self.assertEqual(self.controller.updateMovieName('90', 'nuuummmeee test2'), True)

    def test_UpdateMovieName3(self):
        self.assertEqual(self.controller.updateMovieName('90', 'nuuummmeee test3'), True)

    def test_UpdateMovieDescription(self):
        self.assertEqual(self.controller.updateMovieDescription('123', 'test descriereeeee'), True)

    def test_UpdateMovieDescription2(self):
        self.assertEqual(self.controller.updateMovieDescription('123', 'test descriereeeee2'), True)

    def test_UpdateMovieDescription3(self):
        self.assertEqual(self.controller.updateMovieDescription('123', 'test descriereeeee33'), True)

    def test_UpdateMovieGenre(self):
        self.assertEqual(self.controller.updateMovieGenre("234", 'family'), True)

    def test_UpdateMovieGenre2(self):
        self.assertRaises(ValueError, self.controller.updateMovieGenre, "s2345", 'action')

    def test_UpdateMovieGenre3(self):
        self.assertRaises(ValueError, self.controller.updateMovieGenre, "234", 'comedys')

    def test_UpdateMovieId(self):
        self.assertEqual(self.controller.updateMovieId("33", '99'), True)

    def test_UpdateMovieId2(self):
        self.assertEqual(self.controller.updateMovieId("323", '929'), True)

    def test_UpdateMovieId3(self):
        self.assertEqual(self.controller.updateMovieId("333", '939'), None)

    def test_GetAllMovies(self):
        repo2 = Repository('movieUpdateTest', "test2")
        movie = Movie("2", "223", '22320', 'action')
        controller2 = MovieController(repo2)
        l = controller2.getAllMovies()
        self.assertEqual(controller2.getAllMovies(), [movie])

    def test_getMovieById(self):
        if self.controller.getMovieById('11111111') is False:
            self.controller.addMovie('11111111', 'sfsdfsf', 'sdfdsfsfdsfdsfs', 'action')
        self.assertEqual(self.controller.getMovieById('11111111'),
                         Movie('11111111', 'sfsdfsf', 'sdfdsfsfdsfdsfs', 'action'))

    def test_getMovieById2(self):
        if self.controller.getMovieById('111211111') is False:
            self.controller.addMovie('111211111', 'sfsdfsf', 'sdfdsfsfdsfdsfs', 'action')
        self.assertRaises(ValueError, self.controller.getMovieById, '111211111d')

    def test_ValidateMovie(self):
        self.assertRaises(ValueError, MovieValidator.validate, "", "", "", "")
        self.assertRaises(ValueError, MovieValidator.validate, "", ",", ",", ",")

    def test_search(self):
        c = MovieController(Repository("testSearch", "d"))
        c.addItem(Movie(3, "action", "sdf", "family"))
        self.assertEqual(c.searchMovieByGenre("action"), [])
        c.removeMovie(3)
        self.assertEqual(c.searchMovieByTitle("d"), [])
        self.assertEqual(c.searchMovieByDescription("descriere"), [])
        self.assertRaises(ValueError, c.searchMovieByDescription, "")
        self.assertRaises(ValueError, c.searchMovieByGenre, "")
        self.assertRaises(ValueError, c.searchMovieByTitle, "")
