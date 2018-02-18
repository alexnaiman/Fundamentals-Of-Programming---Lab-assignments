from GUI.ClientListWindow import ClientListWindow
from GUI.MovieListWindow import MovieListWindow
from GUI.RentalListWindow import RentalListWindow
from GUI.StatsList import StatsList
from pyforms import BaseWidget
from pyforms.Controls import ControlEmptyWidget
from pyforms.Controls import ControlText, ControlList, ControlButton


# TO DO: write specifications


class MainApp(BaseWidget):
    movieController = None
    clientController = None
    rentalController = None

    def __init__(self):
        super(MainApp, self).__init__('Simple example 1')
        self._movieWindow = ControlEmptyWidget()
        self._clientWindow = ControlEmptyWidget()
        self._rentalWindow = ControlEmptyWidget()
        self._rentalWindow.value = RentalListWindow(MainApp.rentalController)
        self._movieWindow.value = MovieListWindow(MainApp.movieController, MainApp.rentalController)
        self._clientWindow.value = ClientListWindow(MainApp.clientController, MainApp.rentalController)
        self._middlename = ControlText("sd")
        self._lateRentals = ControlEmptyWidget()
        self._lateRentals.value = StatsList("Late Rentals", MainApp.rentalController.lateRentals())
        self._mostRentedMoviesByDays = ControlEmptyWidget()
        self._mostRentedMoviesByDays.value = StatsList("Most rented movies by number of days",
                                                       MainApp.rentalController.mostRentedMoviesByDays())
        self._mostRentedMoviesByNumber = ControlEmptyWidget()
        self._mostRentedMoviesByNumber.value = StatsList("Most rented movies by number of times they were rented",
                                                         MainApp.rentalController.mostRentedMoviesByDays())
        self._allRentedMovies = ControlEmptyWidget()
        self._allRentedMovies.value = ControlList("Currently rented movies")
        self._allRentedMovies.value.value = [[x.id, x.title, x.description, x.genre] for x in
                                             MainApp.rentalController.allRentedMovies()]
        self._allRentedMovies.value.horizontalHeaders = ['Id', 'Title', 'Description', 'Genre']
        self._refresh = ControlButton("Refresh")
        self._refresh.value = self.refresh
        self._undo = ControlButton("Undo")
        self._undo.value = self._undoAction
        self._redo = ControlButton("Redo")
        self._redo.value = self._redoAction
        self._refreshMovies = ControlButton("Refresh")
        self._refreshMovies.value = self._refreshMoviesAction
        self.formset = [{
            'Movies': ['_movieWindow'],
            'Clients': ['_clientWindow'],
            'Rentals': ['_rentalWindow', '=', '_refreshMovies'],
            'Statistics': ["_lateRentals", "||", "_mostRentedMoviesByNumber", '||', '_mostRentedMoviesByDays', '||',
                           "_allRentedMovies", '=', '_refresh']

        },
            '=',
            ['_undo', '||', '_redo']]

    def _refreshMoviesAction(self):
        self._rentalWindow.value.renderData()

    def _undoAction(self):
        try:
            MainApp.rentalController.undo()
            self._movieWindow.value.renderData()
            self._clientWindow.value.renderData()
            self._rentalWindow.value.renderData()
        except Exception as e:
            print(e)

    def _redoAction(self):
        try:
            MainApp.rentalController.redo()
            self._movieWindow.value.renderData()
            self._clientWindow.value.renderData()
            self._rentalWindow.value.renderData()
        except Exception as e:
            pass

    def __clientWindow(self):
        self._clientWindow.value.renderData()
        ######TODOOOOOOOOOO######

    def __rentalWindow(self):
        print("rental")

    def refresh(self):
        self._mostRentedMoviesByNumber.value.renderData(MainApp.rentalController.mostRentedMoviesByNumber())
        self._mostRentedMoviesByDays.value.renderData(MainApp.rentalController.mostRentedMoviesByDays())
        self._lateRentals.value.renderData(MainApp.rentalController.lateRentals())
        self._allRentedMovies.value.value = [[x.id, x.title, x.description, x.genre] for x in
                                             MainApp.rentalController.allRentedMovies()]
