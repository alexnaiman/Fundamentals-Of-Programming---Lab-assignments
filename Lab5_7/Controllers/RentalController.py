from collections import Counter
from datetime import date, datetime
from functools import reduce

from Assignment9.CustomDictionaryPackage import filter, sort
from Controllers.BaseController import BaseController
from Models.Rental import Rental
from Services.RentalValidator import RentalValidator


class RentalController(BaseController):
    '''
        Rental controller class used for to manage the rental repository
        a wrap up for the BaseController which "extends" the base operations of the base controller
   '''

    def __init__(self, repo, clientController, movieController):
        self.__clientControler = clientController
        self.__movieController = movieController
        super().__init__(repo, Rental)

    def addRental(self, rentalId, movieId, clientId, rentedDate, dueDate, returnedDate):
        '''
                A function that validates and adds a rental to the repository
        :param rentalId: integer
        :param movieId: integer
        :param clientId: integer
        :param rentedDate: string of format YYYY-MM-DD
        :param dueDate: string of format YYYY-MM-DD
        :param returnedDate: string of format YYYY-MM-DD
        :return: True if the item was added, False otherwise
        '''
        if RentalValidator.validate(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate):
            rentalId = int(rentalId)
            movieId = int(movieId)
            clientId = int(clientId)
            rental = Rental(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate)
            if self.getItemById(int(rentalId)) is not False:
                raise ValueError("Error:\n The given id is already taken")
            self.addItem(rental)
            return True

    def removeRental(self, rentalId):
        '''
            A functions that removes a rental from the repository and raises exception if there are any errors
        :param rentalId: integer
        :return: True if the rental was removed successfully, False otherwise
        '''
        try:
            rentalId = int(rentalId)
            return self.removeItemById(rentalId)
        except Exception as e:
            raise ValueError("Error:\n Rental id must be integer \n" + str(e))

    def updateRental(self, rentalId, newRentalId, movieId, clientId, rentedDate, dueDate, returnedDate):
        '''
            A function that updates a movie's all fields and also provides data validation
        :param rentalId: integer
        :param newRentalId: integer
        :param movieId: integer
        :param clientId: integer
        :param rentedDate: string of format YYYY-MM-DD
        :param dueDate: string of format YYYY-MM-DD
        :param returnedDate:  string of format YYYY-MM-DD
        :return: True if the rental was updated, False otherwise
        '''
        RentalValidator.validate(newRentalId, movieId, clientId, rentedDate, dueDate, returnedDate)
        item = self.getItemById(int(rentalId))
        checkForId = self.getItemById(newRentalId)
        if checkForId is not False and newRentalId.strip() != rentalId.strip():
            raise ValueError("Error:\n The given id is already taken")
        if item is not False:
            item = Rental(newRentalId, movieId, clientId, rentedDate, dueDate, returnedDate)
            return self.updateItemById(int(rentalId), item)

    def getAllRentals(self):
        '''
            A function that returns all the rentals from the repo
            :return: list of Rental's objects
        '''
        rentals = self.getAllItems()
        rentalsList = []
        if rentals == 0:
            return []
        if rentals is not False:
            for rental in rentals:
                rentalsList.append(rental)
        return rentalsList

    def getRentalById(self, rentalId):
        '''
                A function that returns a list from the repo by its id
            :param rentalId: integer
            :return: Rental item, False otherwise
        '''
        try:
            rentalId = int(rentalId)
        except ValueError:
            raise ValueError("Error:\n Movie id must be integer")
        rental = self.getItemById(rentalId)
        if rental is not False:
            return rental
        return rental

    def rent(self, rentalID, movieId, clientId, rentedDate, dueDate, returnedDate):
        '''
            Functions that creates a new rental, validating all the necessary fields
        :param rentalID: integer
        :param movieId: integer
        :param clientId: integer
        :param rentedDate: string of format YYYY-MM-DD
        :param dueDate: string of format YYYY-MM-DD
        :param returnedDate: string of format YYYY-MM-DD
        :return: True if the rent was valid and added, False otherwise
        '''
        rentalList = [a for a in self.getAllRentals()]
        try:
            x = int(rentalID)
        except ValueError:
            raise ValueError("Error:\n Rental id should be integer!")
        try:
            x = int(movieId)
        except ValueError:
            raise ValueError("Error:\n Movie id should be integer!")
        try:
            x = int(clientId)
        except ValueError:
            raise ValueError("Error:\n Client id should be integer!")
        if len(dueDate) == 10:
            try:
                year, month, day = map(int, dueDate.split('-'))
                auxDate = date(year, month, day)
            except Exception as e:
                raise ValueError("Error:\n Due date is not in the correct format")
        else:
            raise ValueError("Error:\n Due date is not in the correct format")
        if auxDate < date.today():
            raise ValueError("Error:\n Due date cannot be smaller than today's date")
        for rental in rentalList:
            if str(rental.clientId) == str(clientId):
                try:
                    year, month, day = map(int, rental.dueDate.split('-'))
                    auxDate = date(year, month, day)
                    now = date.today()
                    if auxDate < now:
                        raise TypeError("Error:\n You cannot rent any movie until you don't return the rented movies!")
                except ValueError as e:
                    raise ValueError("Error:\n Due date cannot be smaller than today's date")
                except TypeError:
                    raise ValueError("Error:\n You cannot rent any movie until you don't return the rented movies!")

        for rental in rentalList:
            if str(rental.movieId) == str(movieId) and str(rental.returnedDate) == '-1':
                raise ValueError("Error:\n That movie is already rented!")
        if self.__movieController.getMovieById(movieId) is False:
            raise ValueError("Error:\n That movie doesn't exist")
        if self.__clientControler.getClientById(clientId) is False:
            raise ValueError("Error:\n That client doesn't exist")
        return self.addRental(rentalID, movieId, clientId, rentedDate, dueDate, returnedDate)

    def returnAMovie(self, rentalId):
        '''
            Functions that returns a movie, validating all the necessary fields
        :param rentalId:  integer
        :return: True if the movie was successfully returned
        '''
        try:
            rentalId = int(rentalId)
        except ValueError:
            raise ValueError("Error:\n Rental Id should be integer")
        rental = self.getRentalById(rentalId)
        if rental is False:
            raise ValueError("Error: \n Cannot find the rental!")
        returnedDate = datetime.today().strftime('%Y-%m-%d')
        rental.returnedDate = returnedDate
        return self.updateItemById(rentalId, rental)

    def removeAllAppOfMovie(self, movieId):
        try:
            movieId = int(movieId)
        except ValueError:
            raise ValueError("Error:\n Movie id must be integer")
        rentals = self.getAllRentals()
        if rentals == 0:
            return
        for rental in rentals:
            if str(rental.movieId) == str(movieId):
                self.setGroup(True)
                self.removeRental(rental.id)
                self.setGroup(False)


    def removeAllAppOfClient(self, clientId):
        try:
            clientId = int(clientId)
        except ValueError:
            raise ValueError("Error:\n Movie id must be integer")
        rentals = self.getAllRentals()
        if rentals == 0:
            return
        for rental in rentals:
            if str(rental.clientId) == str(clientId):
                self.setGroup(True)
                self.removeRental(rental.id)
                self.setGroup(False)


    def updateMovieIdFromRental(self, movieId, newMovieId):
        try:
            movieId = int(movieId)
        except ValueError:
            raise ValueError("Error:\n Movie id must be integer")
        rentals = self.getAllRentals()
        for rental in rentals:
            if rental.movieId == str(movieId):
                self.updateRental(rental.id, rental.id, newMovieId, rental.clientId, rental.rentedDate, rental.dueDate,
                                  rental.returnedDate)

    def updateClientIdFromRental(self, clientId, newClientId):
        try:
            clientId = int(clientId)
        except ValueError:
            raise ValueError("Error:\n Movie id must be integer")
        rentals = self.getAllRentals()
        for rental in rentals:
            if rental.clientId == str(clientId):
                self.updateRental(rental.id, rental.id, rental.movieId, newClientId, rental.rentedDate, rental.dueDate,
                                  rental.returnedDate)

    def mostRentedMoviesByNumber(self):
        movies = self.__movieController.getAllMovies()
        rentals = self.getAllRentals()
        top = list(map(lambda r: r.movieId, rentals))
        c = Counter(top)
        topMovies = list(map(lambda m: [m, 0 if m.id not in c.keys() else c[m.id]], movies))
        sort(topMovies, key=lambda x: x[1], reverse=True)
        return topMovies

    def mostRentedMoviesByDays(self):
        movies = self.__movieController.getAllMovies()
        rentals = self.getAllRentals()
        topDays = list(map(lambda r: (r.movieId, abs(self.getDays(r.rentedDate, r.returnedDate))), rentals))
        sort(topDays, key=lambda x: x[0])
        c = Counter([x[0] for x in topDays])
        auxList = [list(filter(lambda x: x[0] == cs, topDays)) for cs in c.keys()]
        auxList = list(map(lambda x: reduce(lambda a, b: [a[0], b[1] + a[1]], x), auxList))
        d = {a[0]: a[1] for a in auxList}
        topMovies = list(map(lambda m: [m, 0 if m.id not in d.keys() else d[m.id]], movies))
        sort(topMovies, key=lambda a: a[1], reverse=True)
        return topMovies

    def getDays(self, date1, date2):
        if date2 == '-1':
            date2 = datetime.now().date()
        else:
            date2 = date(*list(map(int, date2.split('-'))))
        date1 = date(*list(map(int, date1.split('-'))))
        return (date1 - date2).days

    def allRentedMovies(self):
        movies = self.__movieController.getAllMovies()
        rentals = self.getAllRentals()
        movieId = list(map(lambda x: x.movieId, rentals))
        return list(filter(lambda x: x.id in movieId, movies))

    def lateRentals(self):
        rentals = self.getAllRentals()
        lateRentals = list(filter(lambda r: r.returnedDate == '-1' and self.getDays(r.dueDate, '-1') < 0, rentals))
        lateRentalsWithDays = list(map(lambda m: [m, abs(self.getDays(m.dueDate, '-1'))], lateRentals))
        movies = self.__movieController.getAllMovies()
        if not movies:
            return []
        lateRentalsWithDays = list(
            map(lambda x: [self.__movieController.getMovieById(x[0].movieId), x[1]], lateRentalsWithDays))
        sort(lateRentalsWithDays, key=lambda a: a[1], reverse=True)
        return lateRentalsWithDays
