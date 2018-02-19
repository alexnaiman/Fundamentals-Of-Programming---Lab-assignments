import datetime


class ConsoleUI:
    def __init__(self, movieController, clientController, rentalController):
        self.__movieController = movieController
        self.__clientController = clientController
        self.__rentalController = rentalController

    def __test(self, x, y):
        return x * y

    def __addMovie(self):
        '''
            Reads input for adding a movie and prints the corresponding messages
        '''
        print("\033[92mCreate a new movie!\033[0m")
        movieId = input("Give movie id: ")
        movieTitle = input("Give movie title: ")
        movieDescription = input("Give movie description: ")
        movieGenre = input("Give movie genre: ")
        try:
            if self.__movieController.addMovie(movieId, movieTitle, movieDescription, movieGenre):
                print("\033[92m Movie added successfully!\033[0m")
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __removeMovie(self):
        '''
            Reads input for removing a movie and prints the corresponding messages
        '''
        movieId = input("Give the movie id you want to remove: ")
        try:
            if self.__movieController.removeMovie(movieId) is not False:
                self.__rentalController.setGroup(True)
                self.__rentalController.removeAllAppOfMovie(movieId)
                self.__rentalController.setGroup(False)

                print("\033[92m Movie removed successfully!\033[0m")
            else:
                print("\033[91m Movie id cannot be find")
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __updateMovie(self):
        '''
            Reads input for adding a movie and prints the correspondingly messages
        '''
        print("\033[92mUpdate an existing movie!\033[0m")
        movieId = input("Give movie id: ")
        movieTitle = input("Give movie title: ")
        movieDescription = input("Give movie description: ")
        movieGenre = input("Give movie genre: ")

        try:
            if self.__movieController.updateMovie(movieId, movieTitle, movieDescription, movieGenre):
                print("\033[92m Movie updated successfully!\033[0m")
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __printSubmenu(self, listOfOptions):
        '''
            Prints a submene from a dictioary
        :param listOfOptions: dictionary of form {key:(function, message)}
        '''
        for option in listOfOptions:
            print(listOfOptions[option][1])
        print("0.Exit")

    def __listAllMovies(self):
        '''
           Lists all the movies and prints the corresponding messages
        '''
        movieList = self.__movieController.getAllMovies()
        if len(movieList) > 0:
            print("List all movies:")
            for movie in movieList:
                print("\t" + str(movie))
        else:
            print("\033[91m\033[;1mNO\033[91m movie are in the list \033[0m")

    def __findMovieById(self):
        '''
                Reads input for finding  a movie by its id and prints the correspondingly messages
        '''
        movieId = input("Give movie id: ")
        movie = self.__movieController.getMovieById(movieId)
        if movie is not False:
            print("\033[92m" + str(movie) + "\033[0m")
        else:
            print("\033[91mError:\nCannot find movie! \033[0m")

    def __movieMenu(self):
        '''
            Prints and controls the movie menu
        '''
        options = {1: (self.__addMovie, "1.Add movie to the list"),
                   2: (self.__removeMovie, "2.Remove movie from the list"),
                   3: (self.__updateMovie, "3.Update movie by id"),
                   4: (self.__listAllMovies, "4.List all movies"),
                   5: (self.__findMovieById, "5.Find movie by id"),
                   }
        while True:
            self.__printSubmenu(options)
            try:
                option = int(input("\033[1;36mSelect one of the above!\n\033[0m"))
                if option == 0:
                    break
                else:
                    options[option][0]()
            except Exception as e:
                print("\033[91mError: \n Invalid command\033[0m")
                continue
            except KeyError:
                print("\033[91mError: \n Invalid command\033[0m")
                continue

    def __clientMenu(self):
        '''
            Prints and controls the movie menu
        '''
        options = {1: (self.__addClient, "1.Add client to the list"),
                   2: (self.__removeClient, "2.Remove client from the list"),
                   3: (self.__updateClient, "3.Update client by id"),
                   4: (self.__listAllClient, "4.List all clients"),
                   5: (self.__findClientByID, "5.Find client by id"),
                   }
        while True:
            self.__printSubmenu(options)
            try:
                option = int(input("\033[1;36mSelect one of the above!\n\033[0m"))
                if option == 0:
                    break
                else:
                    options[option][0]()
            except Exception as e:
                print("\033[91mError: \n Invalid command\033[0m")
                continue
            except KeyError:
                print("\033[91mError: \n Invalid command\033[0m")
                continue

    def __addClient(self):
        '''
            Reads input for adding a client and prints the corresponding messages
        '''
        print("\033[92mCreate a new client!\033[0m")
        clientId = input("Give client id: ")
        clientName = input("Give client name: ")
        try:
            if self.__clientController.addClient(clientId, clientName):
                print("\033[92m Client added successfully!\033[0m")
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __removeClient(self):
        '''
            Reads input for removing a client and prints the corresponding messages

        '''
        clientId = input("Give the client id you want to remove: ")
        try:
            if self.__clientController.removeClient(clientId) is not False:
                self.__rentalController.setGroup(True)
                self.__rentalController.removeAllAppOfClient(clientId)
                self.__rentalController.setGroup(False)
                print("\033[92m Client removed successfully!\033[0m")
            else:
                print("\033[91m Client id cannot be find\033[0m")
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __updateClient(self):
        '''
                Reads input for updating a client and prints the corresponding messages
        '''
        print("\033[92mUpdate an existing client!\033[0m")
        clientId = input("Give client id: ")
        clientName = input("Give new client name: ")
        try:
            if self.__clientController.updateClient(clientId, clientName):
                print("\033[92m Client added successfully!\033[0m")
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __listAllClient(self):
        '''
           Lists all the movies and prints the corresponding messages
        '''
        clients = self.__clientController.getAllClients()
        if len(clients) != 0:
            print("List all clients:")
            for client in clients:
                print("\t" + str(client))
        else:
            print("\033[91m\033[;1mNO\033[91m clients are in the list \033[0m")

    def __listAllRentals(self):
        rentals = self.__rentalController.getAllRentals()
        if len(rentals) != 0:
            print("List all rentals:")
            for rental in rentals:
                print("\t" + str(rental))
        else:
            print("\033[91m\033[;1mNO\033[91m Rental are in the list \033[0m")
    def __findClientByID(self):
        '''
            Reads input for finding  a client by its id and  prints the correspondingly messages
        '''
        clientId = input("Give client id: ")
        client = self.__clientController.getClientById(clientId)
        if client is not False:
            print("\033[92m" + str(client) + "\033[0m")
        else:
            print("\033[91mError:\nCannot find client! \033[0m")

    def __rentMovie(self):
        '''
            Reads input for renting a movie and prints the correspondingly messages
        :return:
        '''
        print("\033[92m Rent an available movie!\033[0m")
        rentalId = input("Give rental Id: ")
        movieId = input("Give movie Id: ")
        clientId = input("Give client Id: ")
        dueDate = input("Give due date: ")
        returnedDate = -1
        rentDate = datetime.datetime.today().strftime('%Y-%m-%d')
        try:
            if self.__rentalController.rent(rentalId, movieId, clientId, rentDate, dueDate, returnedDate):
                print("\033[92m Movie rented successfully!\033[0m")
        except ValueError as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __returnAMovie(self):
        '''
            Reads input for returning a movie and prints the correspondingly messages
        '''
        print("\033[92m Return a movie that you rented!\033[0m")
        rentalId = input("Give your rental id: ")
        try:
            if self.__rentalController.returnAMovie(rentalId):
                print("\033[92m Movie returned successfully!\033[0m")

        except ValueError as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __searchMovie(self):
        '''
            Reads input for searching a movie by its field and prints the correspondingly messages
        '''
        options = {
            1: (self.__searchMovieById, '1.Search Movie by id'),
            2: (self.__searchMovieByTitle, '2.Search Movie by title'),
            3: (self.__searchMovieByDescription, '3.Search movie by description'),
            4: (self.__searchMovieByGenre, '4.Search movie by genre')
        }
        while True:
            self.__printSubmenu(options)
            try:
                option = int(input("\033[1;36mSelect one of the above!\n\033[0m"))
                if option == 0:
                    break
                else:
                    options[option][0]()
            except Exception:
                print("\033[91mError: \n Invalid command\033[0m")
                continue
            except KeyError:
                print("\033[91mError: \n Invalid command\033[0m")
                continue

    def __searchMovieById(self):
        movieId = input("Give movie id: ")
        try:
            movieList = self.__movieController.searchMovieById(movieId)
            if len(movieList) == 0:
                print("\033[91mSorry! \nCannot find any movie! \033[0m")
                return
            print("\033[92mResults:")
            for movie in movieList:
                print("\033[92m" + str(movie) + "\033[0m")
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __searchMovieByTitle(self):
        title = input("Give movie title: ")
        try:
            movieList = self.__movieController.searchMovieByTitle(title)
            if len(movieList) == 0:
                print("\033[91mSorry! \nCannot find any movie! \033[0m")
                return
            print("\033[92mResults:")
            for movie in movieList:
                print("\033[92m" + str(movie) + "\033[0m")
        except Exception as e:
            print("\033[91mError: \n " + str(e) + " \033[0m")

    def __searchMovieByDescription(self):
        desc = input("Give movie description: ")
        try:
            movieList = self.__movieController.searchMovieByDescription(desc)
            if len(movieList) == 0:
                print("\033[91mSorry! \nCannot find any movie! \033[0m")
                return
            print("\033[92mResults:")
            for movie in movieList:
                print("\033[92m" + str(movie) + "\033[0m")
        except Exception as e:
            print("\033[91mError: \n " + str(e) + " \033[0m")

    def __searchMovieByGenre(self):
        genre = input("Give movie genre: ")
        try:
            movieList = self.__movieController.searchMovieByGenre(genre)
            if len(movieList) == 0:
                print("\033[91mSorry! \nCannot find any movie! \033[0m")
                return
            print("\033[92mResults:")
            for movie in movieList:
                print("\033[92m" + str(movie) + "\033[0m")
        except Exception as e:
            print("\033[91mError: \n " + str(e) + " \033[0m")

    def __searchClient(self):
        '''
            Reads input for searching a movie by its field and prints the correspondingly messages
        '''
        options = {
            1: (self.__searchClientById, '1.Search Client by id'),
            2: (self.__searchClientByName, '2.Search Client by name'),
        }
        while True:
            self.__printSubmenu(options)
            try:
                option = int(input("\033[1;36mSelect one of the above!\n\033[0m"))
                if option == 0:
                    break
                else:
                    options[option][0]()
            except Exception:
                print("\033[91mError: \n Invalid command\033[0m")
                continue
            except KeyError:
                print("\033[91mError: \n Invalid command\033[0m")
                continue

    def __searchClientById(self):
        clientId = input("Give client id: ")
        try:
            clientList = self.__clientController.searchClientById(clientId)
            if len(clientList) == 0:
                print("\033[91mSorry! \nCannot find any client! \033[0m")
                return
            print("\033[92mResults:")
            for client in clientList:
                print("\033[92m" + str(client) + "\033[0m")
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __searchClientByName(self):
        name = input("Give client name: ")
        try:
            clientList = self.__clientController.searchClientByName(name)
            if len(clientList) == 0:
                print("\033[91mSorry! \nCannot find any client! \033[0m")
                return
            print("\033[92mResults:")
            for client in clientList:
                print("\033[92m" + str(client) + "\033[0m")
        except Exception as e:
            print("\033[91mError: \n " + str(e) + " \033[0m")

    def __stats(self):
        options = {
            1: (self.__mostRentedMovieNumber, "1.Most rented movies by the number of times the were rented "),
            2: (self.___mostRentedMovieDays, "2.Most rented movies by the number of times the were rented"),
            3: (self.__allRentedMovies, "3.All rented movies"),
            4: (self.__lateRentals, "4.Late rentals")
        }
        while True:
            self.__printSubmenu(options)
            try:
                option = int(input("\033[1;36mSelect one of the above!\n\033[0m"))
                if option == 0:
                    break
                else:
                    options[option][0]()
            except Exception as e:
                print("\033[91mError: \n Invalid command\033[0m")
                continue
            except KeyError:
                print("\033[91mError: \n Invalid command\033[0m")
                continue

    def __mostRentedMovieNumber(self):
        print("\033[92mMost rented movies are:\033[0m")
        movieList = self.__rentalController.mostRentedMoviesByNumber()
        if len(movieList) == 0:
            print("\033[91mThere are no movies in the list ☹\033[0m")
        for m in movieList:
            print("\t" + str(m[0]) + " rented " + str(m[1]) + " times")

    def ___mostRentedMovieDays(self):
        print("\033[92mMost rented movies by number of days are:\033[0m")
        movieList = self.__rentalController.mostRentedMoviesByDays()
        if len(movieList) == 0:
            print("\033[91mThere are no movies in the list ☹\033[0m")
        for m in movieList:
            print("\t" + str(m[0]) + " rented " + str(m[1]) + " days")

    def __allRentedMovies(self):
        print("\033[92mAll rented movies are:\033[0m")
        movieList = self.__rentalController.allRentedMovies()
        if len(movieList) == 0:
            print("\033[91mThere are no movies in the list ☹\033[0m")
        for m in movieList:
            print("\t" + str(m))

    def __lateRentals(self):
        print("\033[92mAll late rentals are:\033[0m")
        movieList = self.__rentalController.lateRentals()
        if len(movieList) == 0:
            print("\033[91mThere are no movies in the list ☹\033[0m")
        for m in movieList:
            print("\t" + str(m[0]) + " \033[91mlate: " + str(m[1]) + " days\033[0m")

    def __undo(self):
        try:
            self.__movieController.undo()
            print("\033[92mUndo done successfully\033[0m")
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")

    def __redo(self):
        try:
            self.__movieController.redo()
            print("\033[92mUndo done successfully\033[0m")
        except Exception as e:
            print("\033[91m" + str(e) + "\033[0m")

    def mainMenu(self):
        '''
            Our main menu function the prints and controls the app
        '''
        options = {1: (self.__movieMenu, "1.Movie options"),
                   2: (self.__clientMenu, "2.Client options"),
                   3: (self.__rentMovie, "3.Rent a movie"),
                   4: (self.__returnAMovie, "4.Return a movie"),
                   5: (self.__searchMovie, "5.Search Movies"),
                   6: (self.__searchClient, "6.Search Clients"),
                   7: (self.__stats, "7.Statistics"),
                   8: (self.__undo, "8.Undo"),
                   9: (self.__redo, "9.Redo"),
                   10: (self.__listAllRentals, "10.List rentals")
                   }

        while True:
            self.__printSubmenu(options)
            try:
                option = int(input("\033[1;36mSelect one of the above!\n\033[0m"))
                if option == 0:
                    break
                else:
                    options[option][0]()
            except Exception as e:
                print("\033[91mError: \n Invalid command\033[0m")
                continue
