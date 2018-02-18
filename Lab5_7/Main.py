from Config.Settings import Settings
from Models.Client import Client
from Models.Movie import Movie
from Models.Rental import Rental
from Repositories.FileRepository import FileRepository


class App:
    '''
        Our main class which initialize the entire app
    '''

    @staticmethod
    def start():
        """
            The start functions with the linking between our main classes and entities
        :return:
        """
        movieRepository = FileRepository('./data/Movies', "Movie", Movie.movieToFile, Movie.movieFromFile)
        clientRepository = FileRepository('./data/Clients', "Client", Client.clientToFile, Client.clientFromFile)
        rentalRepository = FileRepository('./data/Rentals', "Rental", Rental.rentalToFile, Rental.rentalFromFile)
        settings = Settings("settings.properties")
        settings.readSettings()
        settings.config()


if __name__ == '__main__':
    try:
        App.start()
    except Exception as e:
        print("\033[91m" + str(e) + "\033[0m")
