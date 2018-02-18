from Assignment9.CustomDictionaryPackage import filter
from Controllers.BaseController import BaseController
from Models.Movie import Movie, MOVIE_GENRE
from Services.MovieValidator import MovieValidator


class MovieController(BaseController):
    '''
        Movie controller class used for to manage the movie repository
        a wrap up for the BaseController which "extends" the base operations of the base controller
    '''

    def __init__(self, repo):
        super().__init__(repo, Movie)

    def addMovie(self, movieId, title, description, genre):
        '''
            A function that validates and adds a movie to the repository
        :param movieId: integer
        :param title: string / cannot be empty
        :param description: string / cannot be empty
        :param genre: one of MOVIE_GENRE
        :return: True if the movie was added with success, raises errors if there are any validation problems
        '''
        if MovieValidator.validate(movieId, title, description, genre):
            movieId = int(movieId)
            movie = Movie(movieId, title, description, genre)
            if self.repo.getItemById(int(movieId)) is not False:
                raise ValueError("Error:\n The given id is already taken")
            self.addItem(movie)
            return True

    def removeMovie(self, movieId):
        '''
            A functions that removes a movie from the repository and raises exception if there are any errors
        :param movieId: integer
        :return: True if the movie was removed, false otherwise
        '''
        try:
            movieId = int(movieId)
            return self.removeItemById(movieId)
        except Exception as e:
            raise e
            raise ValueError("Error:\n Movie id must be integer")

    def updateMovieName(self, movieId, movieTitle):
        '''
            A functions that updates a movie's title and also provides data validation
        :param movieId: integer
        :param movieTitle: string // cannot be empty
        :return: True if the movie was updated, False, otherwise
        '''
        if ',' in movieTitle:
            raise ValueError("Error:\n Parameters should not contain the ',' character")
        try:
            movieId = int(movieId)
        except ValueError:
            raise ValueError("Error:\n Movie id must be integer")
        if len(movieTitle.strip()) == 0:
            raise ValueError("Error: \n Movie Title should not be empty")
        item = self.getItemById(movieId)
        if item is not False:
            item = Movie(*item)
            if len(movieTitle.strip()) > 0:
                item.title = movieTitle
                return self.updateItemById(int(movieId), item)
        else:
            raise ValueError("Error:\n Movie Id cannot be find")

    def updateMovieId(self, movieId, newId):
        '''
                A functions that updates a movie's ID and also provides data validation
            :param movieId: integer
            :param newId: intege
            :return: True if the movie was updated, False, otherwise
        '''
        try:
            movieId = int(movieId)
        except ValueError:
            raise ValueError("Error: \n Movie Id cannot be string")
        try:
            newId = int(newId)
        except ValueError:
            raise ValueError("Error: \n New Movie Id cannot be string")

        item = self.getItemById(movieId)
        newItem = self.getItemById(newId)

        if newItem:
            raise ValueError("Error:\n The given id is already taken")
        if item is not False:
            item = Movie(*item)
            item.id = newId
            return self.updateItemById(movieId, item)

    def updateMovieGenre(self, movieId, newGenre):
        '''
                A functions that updates a movie's genre and also provides data validation
            :param movieId: integer
            :param newGenre: string // cannot be empty
            :return: True if the movie was updated, False, otherwise
        '''
        if ',' in newGenre:
            raise ValueError("Error:\n Parameters should not contain the ',' character")
        try:
            movieId = int(movieId)
        except ValueError:
            raise ValueError("Error: \n Movie Id cannot be string")
        if newGenre not in MOVIE_GENRE:
            raise ValueError("Error: \n Movie genre isn't valid")
        item = self.getItemById(movieId)
        if item is not False:
            item = Movie(*item)
            item.genre = newGenre
            return self.repo.updateItemById(movieId, item)

    def updateMovieDescription(self, movieId, description):
        '''
                A functions that updates a movie's description and also provides data validation
            :param movieId: integer
            :param description: string // cannot be empty
            :return: True if the movie was updated, False, otherwise
        '''
        if ',' in description:
            raise ValueError("Error:\n Parameters should not contain the ',' character")
        try:
            movieId = int(movieId)
        except ValueError:
            raise ValueError("Error:\n Movie id must be integer")
        if len(description.strip()) == 0:
            raise ValueError("Error: \n Movie Description should not be empty")
        item = self.getItemById(movieId)
        if item is not False:
            item = Movie(*item)
            if len(description.strip()) > 0:
                item.description = description
                return self.updateItemById(int(movieId), item)
        else:
            raise ValueError("Error:\n Movie Id cannot be find")

    def updateMovie(self, movieId, title, description, genre):
        '''
            A function that updates a movie's all fields and also provides data validation
        :param movieId: integer
        :param movieNewId: integer
        :param title: string // cannot be empty
        :param description: string // cannot be empty
        :param genre: one of MOVIE_GENRE // cannot be empty
        :return: True if the movie was updated, False otherwise
        '''
        errors = ""
        MovieValidator.validate(movieId, title, description, genre)
        try:
            movieId = int(movieId)
        except ValueError:
            raise ValueError("Error:\n Movie id must be integer!")
        item = self.getItemById(movieId)
        if item is not False:
            item.title = title.strip()
            item.id = int(movieId)
            item.description = description.strip()
            item.genre = genre.strip()
            return self.updateItemById(movieId, item)
        else:
            raise ValueError("Error:\n Movie Id cannot be find")

    def getAllMovies(self):
        '''
            A function that returns all the movies from the repo
        :return: list of Movie's objects
        '''
        movies = self.getAllItems()
        moviesList = []
        if movies is 0:
            return []
        return movies

    def getMovieById(self, movieId):
        '''
            A function that returns a movie from the repo by its id
        :param movieId: integer
        :return: Movie item, False otherwise
        '''
        try:
            movieId = int(movieId)
        except ValueError:
            raise ValueError("Error:\n Movie id must be integer")
        movie = self.getItemById(movieId)
        if movie is not False:
            return movie
        return movie

    def searchMovieByTitle(self, title):
        '''
            Returns of lists of movies that contains the given string in their title
        :param title: string
        :return: list of Movies
        '''
        if len(title) == 0:
            raise ValueError("Search input cannot be empty!")
        movieList = self.getAllMovies()
        return list(filter(lambda movie: title.strip().lower() in movie.title.lower(), movieList))

    def searchMovieByDescription(self, desc):
        '''
            Returns of lists of movies that contains the given string in their description
        :param desc: string
        :return: list of Movies
        '''
        if len(desc) == 0:
            raise ValueError("Search input cannot be empty!")
        movieList = self.getAllMovies()
        return list(filter(lambda movie: desc.strip().lower() in movie.description.lower(), movieList))

    def searchMovieByGenre(self, genre):
        '''
            Returns of lists of movies that are from the given genre
        :param genre: string
        :return: list of Movies
        '''
        if len(genre) == 0:
            raise ValueError("Search input cannot be empty!")
        movieList = self.getAllMovies()
        return list(filter(lambda movie: genre.strip().lower() in movie.genre.lower(), movieList))

    def searchMovieById(self, id):
        id = id.strip()
        try:
            id = int(id)
        except ValueError:
            raise ValueError("Error:\n\tId must be integer")
        movies = self.getAllMovies()
        return list(filter(lambda movie: str(id) in str(movie.id), movies))
