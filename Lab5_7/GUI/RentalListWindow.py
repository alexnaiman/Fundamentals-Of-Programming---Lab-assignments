from GUI.RentalWindow import RentalWindow
from pyforms import BaseWidget
from pyforms.Controls import ControlList


# TO DO: write specifications

class RentalListWindow(BaseWidget):
    """
    This applications is a GUI implementation of the People class
    """

    def __init__(self, rentalController):
        BaseWidget.__init__(self, 'Rentals')
        self._rentalList = ControlList('Rentals',
                                       plusFunction=self.__addRentalBtnAction)
        self.__controller = rentalController
        self.__rentalController = rentalController
        data = [[x.id, x.movieId, x.clientId, x.rentedDate, x.dueDate, x.returnedDate] for x in
                self.__controller.getAllRentals()]
        self._rentalList.value += data
        self._rentalList.selectEntireRow = True
        self._rentalList.readOnly = True
        self._rentalList.horizontalHeaders = ['Id', 'MovieId', 'ClientId', 'Rented Date', 'Due Date', 'Returned Date']
        self._rentalList.cellDoubleClicked = self.updateRentalAction

    def updateRentalAction(self, row, item):
        win = RentalWindow(False)
        win.getData(*self._rentalList.value[row])
        win.parent = self
        win.show()

    def __addRentalBtnAction(self):
        """
        Add person button event.
        """
        # A new instance of the PersonWindow is opened and shown to the user.
        win = RentalWindow(True)
        win.parent = self
        win.show()

    def addRental(self, id, movieId, clientId, rentedDate, dueDate, returnedDate):
        self.__controller.rent(id, movieId, clientId, rentedDate, dueDate, returnedDate)
        self.renderData()

    def updateRental(self, id, movieId, clientId, rentedDate, dueDate, returnedDate):
        self.__controller.updateRental(id, movieId, clientId, rentedDate, dueDate, returnedDate)
        self.renderData()

    def returnAMovie(self, id):
        self.__rentalController.returnAMovie(id)
        self.renderData()

    def __removeRentalBtnAction(self):
        # self.removePerson(self._peopleList.selected_row_index)
        if len(self._rentalList.mouseSelectedRowsIndexes) == 1:
            self.__controller.removeRental(int(self._rentalList.value[self._rentalList.mouseSelectedRowIndex][0]))
        else:
            for i in self._rentalList.mouseSelectedRowsIndexes:
                self.__controller.removeRental(int(self._rentalList.value[i][0]))
        self.renderData()

    # def return
    def renderData(self):
        data = [[x.id, x.movieId, x.clientId, x.rentedDate, x.dueDate, x.returnedDate] for x in
                self.__controller.getAllRentals()]
        self._rentalList.value = data
