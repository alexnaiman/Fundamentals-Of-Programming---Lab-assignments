from Models.Movie import Movie, MOVIE_GENRE
from   pyforms import BaseWidget
from   pyforms.Controls import ControlButton, ControlCombo, ControlLabel
from   pyforms.Controls import ControlText, ControlTextArea


# TO DO: write specifications

class MovieWindow(Movie, BaseWidget):
    def __init__(self, isCreating):
        Movie.__init__(self, '', '', '', '')
        BaseWidget.__init__(self, 'Movie')
        self.__isCreating = isCreating
        self._idField = ControlText("Id")
        self._titleField = ControlText("Title")
        self._descriptionField = ControlTextArea("Description")
        self._genre = ControlCombo("Genre")
        for i in MOVIE_GENRE:
            self._genre += i
        self._buttonField = ControlButton('Add a new movie')
        self._buttonField.value = self._updateAction
        if not isCreating:
            self._idField.enabled = False
            self._buttonField.name = "Update movie"
        self._label = ControlLabel("")

    def getData(self, id, title, description, genre):
        self._idField.value = id
        self._titleField.value = title
        self._descriptionField.value = description
        self._genre.value = genre

    def _updateAction(self):
        self.id = self._idField.value
        self.description = self._descriptionField.value
        self.genre = self._genre.value
        self.title = self._titleField.value
        self._label.hide()
        try:
            if self.parent is not None:
                if self.__isCreating:
                    self.parent.addMovie(str(self.id), self.title, self.description, self.genre)

                else:
                    self.parent.updateMovie(str(self.id), self.title, self.description, self.genre)
        except Exception as e:
            self._label.show()
            self._label.value = str(e)
