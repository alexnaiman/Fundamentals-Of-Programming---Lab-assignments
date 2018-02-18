from Models.ObjId import ObjId


class Rental(ObjId):
    '''
            Rental Model which encapsulate all the necessary fields for a movie
    '''

    def __init__(self, id, movieId, clientId, rentedDate, dueDate, returnedDate):
        super().__init__(id)
        self.__id = id
        self.__movieId = movieId
        self.__clientId = clientId
        self.__rentedDate = rentedDate
        self.__dueDate = dueDate
        self.__returnedDate = returnedDate

    @property
    def movieId(self):
        return self.__movieId

    @movieId.setter
    def movieId(self, movieId):
        self.__movieId = movieId

    @property
    def clientId(self):
        return self.__clientId

    @clientId.setter
    def clientId(self, clientId):
        self.__clientId = clientId

    @property
    def rentedDate(self):
        return self.__rentedDate

    @rentedDate.setter
    def rentedDate(self, rentedDate):
        self.__rentedDate = rentedDate

    @property
    def dueDate(self):
        return self.__dueDate

    @dueDate.setter
    def dueDate(self, dueDate):
        self.__dueDate = dueDate

    @property
    def returnedDate(self):
        return self.__returnedDate

    @returnedDate.setter
    def returnedDate(self, returnedDate):
        self.__returnedDate = returnedDate

    @staticmethod
    def rentalToFile(rental):
        return str(rental)

    @staticmethod
    def rentalFromFile(params):
        params = [param.strip() for param in params.split(',')]
        rentalId = int(params[0])
        movieId = int(params[1])
        clientId = int(params[2])
        rentedDate = params[3]
        dueDate = params[4]
        returnedDate = params[5]
        return Rental(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)

    def __str__(self):
        return str(self.__id) + ", " + str(self.__movieId) + ", " + str(self.__clientId) + ", " + str(
            self.__rentedDate) + ", " + str(self.__dueDate) + ", " + str(self.__returnedDate)

    def __eq__(self, other):
        if self.id == other.id and self.clientId == other.clientId and self.movieId == other.movieId and self.rentedDate \
                == other.rentedDate:
            return True
        return False

    @staticmethod
    def rentalFromJson(json):
        id = json["_Rental__id"]
        movieId = json["_Rental__movieId"]
        clientId = json["_Rental__clientId"]
        returnedDate = json["_Rental__returnedDate"]
        dueDate = json["_Rental__dueDate"]
        rentedDate = json["_Rental__rentedDate"]
        return Rental(id, movieId, clientId, rentedDate, dueDate, returnedDate)

    @staticmethod
    def rentalToSql(rental):
        return rental.id, rental.movieId, rental.clientId, rental.rentedDate, rental.dueDate, rental.returnedDate
