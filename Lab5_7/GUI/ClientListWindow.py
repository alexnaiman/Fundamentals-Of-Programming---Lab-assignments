import GUI
from GUI.ClientWindow import ClientWindow
from pyforms import BaseWidget
from pyforms.Controls import ControlList, ControlText, ControlButton


# TO DO: write specifications
class ClientListWindow(BaseWidget):
    """
    This applications is a GUI implementation of the People class
    """

    def __init__(self, clientController, rentalController):
        # Client.__init__(self, R)
        BaseWidget.__init__(self, 'Client')
        # Definition of the forms fields2
        self._clientList = ControlList('Clients',
                                       plusFunction=self.__addClientBtnAction,
                                       minusFunction=self.__removeClientBtnAction)
        self.__controller = clientController
        self._searchInput = ControlText("Search")
        self._searchButton = ControlButton("Go")
        self._formset = [
            ('_searchInput',
             ('_searchButton')),
            ("_clientList")
        ]
        self._searchButton.value = self.searchData
        self.__rentalController = rentalController
        data = [[x.id, x.name] for x in self.__controller.getAllClients()]
        self._clientList.value += data
        self._clientList.selectEntireRow = True
        self._clientList.readOnly = True
        self._clientList.horizontalHeaders = ['Id', 'Name']
        self._clientList.cellDoubleClicked = self.updateClientAction

    def updateClientAction(self, row, item):
        win = ClientWindow(False)
        win.getData(*self._clientList.value[row])
        win.parent = self
        win.show()

    def __addClientBtnAction(self):
        """
        Add person button event.
        """
        # A new instance of the PersonWindow is opened and shown to the user.
        win = ClientWindow(True)
        win.parent = self
        win.show()

    def addClient(self, id, name):
        self.__controller.addClient(id, name)
        self.renderData()

    def updateClient(self, id, name):
        self.__controller.updateClient(id, name)
        self.renderData()

    def __removeClientBtnAction(self):
        """
        Remove client button event
        """
        # self.removePerson(self._peopleList.selected_row_index)
        if len(self._clientList.mouseSelectedRowsIndexes) == 1:
            self.__controller.removeClient(int(self._clientList.value[self._clientList.mouseSelectedRowIndex][0]))
            self.__rentalController.removeAllAppOfClient(
                self._clientList.value[self._clientList.mouseSelectedRowIndex][0])
        else:
            for i in self._clientList.mouseSelectedRowsIndexes:
                self.__controller.removeClient(int(self._clientList.value[i][0]))
                self.__rentalController.removeAllAppOfClient(self._clientList.value[i][0])
        self.renderData()

    def renderData(self):
        data = [[x.id, x.name] for x in GUI.MainApp.MainApp.clientController.getAllClients()]
        self._clientList.value = data

    def searchData(self):
        self.renderData()
        data = self._clientList.value
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
        self._clientList.value = values
