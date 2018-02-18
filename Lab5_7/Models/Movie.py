from Models.ObjId import ObjId

MOVIE_GENRE = ('action', 'animation', 'adventure', 'comedy', 'crime', 'documentary', 'family', 'horror', 'cartoon',
               'romance', 'fantasy', 'drama')


class Movie(ObjId):
    '''
        Movie Model which encapsulate all the necessary fields for a movie
    '''

    def __init__(self, id, title, description, genre):
        super().__init__(id)
        self.__id = id
        self.__title = title
        self.__description = description
        self.__genre = genre

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    def __str__(self):
        return str(self.__id) + ', ' + str(self.__title) + ', ' + str(self.__description) + ', ' + str(self.__genre)

    def __eq__(self, other):
        try:
            if self.genre == other.genre and self.description == other.description and self.id == other.id and self.title \
                    == other.title:
                return True
        except Exception as e:
            pass
        return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

    @staticmethod
    def movieFromFile(params):
        params = [param.strip() for param in params.split(',')]
        movieId = int(params[0])
        title = params[1]
        description = params[2]
        genre = params[3]
        return Movie(movieId, title, description, genre)

    @staticmethod
    def movieToFile(movie):
        return str(movie)

    @staticmethod
    def movieFromJson(json):
        genre = json['_Movie__genre']
        title = json['_Movie__title']
        description = json['_Movie__description']
        id = json['_ObjId__id']
        return Movie(id, title, description, genre)

    @staticmethod
    def movieToSql(movie):
        return movie.id, movie.title, movie.description, movie.genre
