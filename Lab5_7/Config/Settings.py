import pyforms
from Controllers.ClientController import ClientController
from Controllers.MovieController import MovieController
from Controllers.RentalController import RentalController
from GUI.MainApp import MainApp
from Models.Client import Client
from Models.Movie import Movie
from Models.Rental import Rental
from Repositories.FileRepository import FileRepository
from Repositories.InMemoryRepository import InMemoryRepository
from Repositories.JsonRepository import JsonRepo
from Repositories.PickleRepo import PickleRepo
from Repositories.SqlRepository import SqlRepo
from UI import Console

config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'lab5_7',
    'port': '3306',
    'raise_on_warnings': True,
    'use_pure': False,
}


class Settings:
    def __init__(self, config):
        self.__config = config
        self.__settings = {}

    def readSettings(self):
        print(self.__config)
        with open(self.__config, "r") as f:
            lines = f.read().split("\n")
            settings = {}
            for line in lines:
                setting = line.split("=")
                if len(setting) > 1:
                    self.__settings[setting[0].strip()] = setting[1].strip()

    def config(self):
        clientRepo = None
        movieRepo = None
        rentalRepo = None
        if self.__settings['repository'] == "text-file":
            clientRepo = FileRepository(self.__settings["clients"], "Client repo", Client.clientToFile,
                                        Client.clientFromFile)
            movieRepo = FileRepository(self.__settings["movies"], "Movie Repo", Movie.movieToFile, Movie.movieFromFile)
            rentalRepo = FileRepository(self.__settings["rentals"], "Rental repo", Rental.rentalToFile,
                                        Rental.rentalFromFile)
        if self.__settings['repository'] == "in-memory":
            clientRepo = InMemoryRepository()
            movieRepo = InMemoryRepository()
            rentalRepo = InMemoryRepository()

        if self.__settings['repository'] == "binary":
            clientRepo = PickleRepo(self.__settings["clients"], "Client repo")
            movieRepo = PickleRepo(self.__settings["movies"], "Movie Repo")
            rentalRepo = PickleRepo(self.__settings["rentals"], "Rental repo")

        if self.__settings['repository'] == 'json':
            clientRepo = JsonRepo(self.__settings["clients"], "ClientRepo", Client.clientFromJson)
            movieRepo = JsonRepo(self.__settings["movies"], "Movie Repo", Movie.movieFromJson)
            rentalRepo = JsonRepo(self.__settings["rentals"], "Rental repo", Rental.rentalFromJson)
        if self.__settings['repository'] == "sql":
            clientRepo = SqlRepo(config, Client, Client.clientToSql, "client", "(id,name)")
            movieRepo = SqlRepo(config, Movie, Movie.movieToSql, "movie", "(id,title,description,genre)")
            rentalRepo = SqlRepo(config, Rental, Rental.rentalToSql, "rental",
                                 "(id,movieId,clientId,rentedDate,dueDate,returnedDate)")
        mc = MovieController(movieRepo)
        cc = ClientController(clientRepo)
        rc = RentalController(rentalRepo, cc, mc)
        if self.__settings['ui'] == "console":
            console = Console.ConsoleUI(mc, cc, rc)
            console.mainMenu()
        if self.__settings['ui'] == 'gui':
            MainApp.clientController = cc
            MainApp.rentalController = rc
            MainApp.movieController = mc
            pyforms.startApp(MainApp)
