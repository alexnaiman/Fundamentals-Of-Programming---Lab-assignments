import datetime

from Models.Rental import Rental
from   pyforms import BaseWidget
from   pyforms.Controls import ControlButton, ControlLabel
from   pyforms.Controls import ControlText


# TO DO: write specifications

class RentalWindow(Rental, BaseWidget):
    def __init__(self, isCreating):
        Rental.__init__(self, '', '', '', '', '', '')
        BaseWidget.__init__(self, 'Rental')
        self.__isCreating = isCreating
        self._idField = ControlText("Id")
        self._clientIdField = ControlText("Client Id")
        self._movieIdField = ControlText("Movie Id")
        self._dueDateField = ControlText("Due Date")
        self._rentedDateField = ControlText("Rented Date")
        self._returnedDateField = ControlText("Returned Date")
        self._buttonField = ControlButton('Rent a new Movie')
        self._buttonField.value = self._updateAction
        self._rentedDateField.enabled = False
        self._returnedDateField.enabled = False
        self._label = ControlLabel("")
        if not isCreating:
            self._idField.enabled = False
            self._clientIdField.enabled = False
            self._movieIdField.enabled = False
            self._dueDateField.enabled = False
            self._returnedDateField.enabled = False
            self._rentedDateField.enabled = False
            self._buttonField.value = self.returnMovie
            self._buttonField.name = "Return movie"

    def returnMovie(self):
        self.parent.returnAMovie(self._idField.value)

    def getData(self, id, movieId, clientId, rentedDate, dueDate, returnedDate):
        self._idField.value = id
        self._movieIdField.value = movieId
        self._clientIdField.value = clientId
        self._rentedDateField.value = rentedDate
        self._dueDateField.value = dueDate
        self._returnedDateField.value = returnedDate
        if str(self._returnedDateField) != '-1':
            self._buttonField.enabled = False

    def _updateAction(self):
        self.id = self._idField.value
        self.movieId = self._movieIdField.value
        self.clientId = self._clientIdField.value
        self.returnedDate = self._returnedDateField.value
        self.rentedDate = self._rentedDateField.value
        self.dueDate = self._dueDateField.value
        self._label.hide()
        try:
            if self.parent is not None:
                if self.__isCreating:
                    self.parent.addRental(str(self.id), self.movieId, self.clientId,
                                          datetime.datetime.today().strftime('%Y-%m-%d'), self.dueDate,
                                          '-1')

                else:
                    self.parent.returnAMovie(self.id)
        except Exception as e:
            self._label.show()
            self._label.value = str(e)
