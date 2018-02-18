from Models.Client import Client
from   pyforms import BaseWidget
from   pyforms.Controls import ControlButton, ControlLabel
from   pyforms.Controls import ControlText


# TO DO: write specifications

class ClientWindow(Client, BaseWidget):
    def __init__(self, isCreating):
        Client.__init__(self, '', '')
        BaseWidget.__init__(self, 'Client')
        self.__isCreating = isCreating
        self._idField = ControlText("Id")
        if not isCreating:
            self._idField.enabled = False
        self._nameField = ControlText("Name")
        self._buttonField = ControlButton('Add a new client')
        self._buttonField.value = self._updateAction
        self._label = ControlLabel("")

    def getData(self, id, name):
        self._idField.value = id
        self._nameField.value = name

    def _updateAction(self):
        self.id = self._idField.value
        self.name = self._nameField.value
        self._label.hide()
        try:
            if self.parent is not None:
                if self.__isCreating:
                    self.parent.addClient(str(self.id), self.name)

                else:
                    self.parent.updateClient(str(self.id), self.name)
        except Exception as e:
            self._label.show()
            self._label.value = str(e)
