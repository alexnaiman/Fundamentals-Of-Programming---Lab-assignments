import GUI
from GUI.MovieWindow import MovieWindow
from pyforms import BaseWidget
from pyforms.Controls import ControlList, ControlText, ControlButton


# TO DO: write specifications

class MovieListWindow(BaseWidget):
    """
    This applications is a GUI implementation of the People class
    """

    def __init__(self, movieController, rentalController):
        # MovieController.__init__(self, R)
        BaseWidget.__init__(self, 'Movie')
        # Definition of the forms fields2
        self._searchInput = ControlText("Search")
        self._searchButton = ControlButton("Go")
        self._formset = [
            ('_searchInput',
             ('_searchButton')),
            ("_movieList")
        ]

        self._movieList = ControlList('Movies',
                                      plusFunction=self.__addPersonBtnAction,
                                      minusFunction=self.__removeMovieBtnAction)
        self.__controller = movieController
        self.__rentalController = rentalController
        data = [[x.id, x.title, x.description, x.genre] for x in self.__controller.getAllMovies()]
        self._movieList.value += data
        self._movieList.selectEntireRow = True
        self._movieList.readOnly = True
        self._movieList.horizontalHeaders = ['Id', 'Title', 'Description', 'Genre']
        self._movieList.cellDoubleClicked = self.updateMovieAction
        self._searchButton.value = self.searchData

    def updateMovieAction(self, row, item):
        win = MovieWindow(False)
        win.getData(*self._movieList.value[row])
        win.parent = self
        win.show()

    def __addPersonBtnAction(self):
        """
        Add person button event.
        """
        # A new instance of the PersonWindow is opened and shown to the user.
        win = MovieWindow(True)
        win.parent = self
        win.show()

    def addMovie(self, id, title, description, genre):
        self.__controller.addMovie(id, title, description, genre)
        self.renderData()

    def updateMovie(self, id, title, description, genre):
        self.__controller.updateMovie(id, title, description, genre)
        self.renderData()

    def __removeMovieBtnAction(self):
        """
        Remove movie button event
        """
        # self.removePerson(self._peopleList.selected_row_index)
        if len(self._movieList.mouseSelectedRowsIndexes) == 1:
            self.__controller.removeMovie(int(self._movieList.value[self._movieList.mouseSelectedRowIndex][0]))
            self.__rentalController.removeAllAppOfMovie(self._movieList.value[self._movieList.mouseSelectedRowIndex][0])
        else:
            for i in self._movieList.mouseSelectedRowsIndexes:
                self.__controller.removeMovie(int(self._movieList.value[i][0]))
                self.__rentalController.removeAllAppOfMovie(self._movieList.value[i][0])
        self.renderData()
        # Execute the application

    def renderData(self):
        data = [[x.id, x.title, x.description, x.genre] for x in GUI.MainApp.MainApp.movieController.getAllMovies()]
        self._movieList.value = data

    def searchData(self):
        self.renderData()
        data = self._movieList.value
        search = self._searchInput.value
        values = []
        if len(search.strip()) == 0:
            self.renderData()
            return
        for d in data:
            for l in d:
                if search.strip().lower() in l.lower():
                    values.append(d)
                    break
        self._movieList.value = values
