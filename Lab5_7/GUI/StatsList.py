from pyforms.Controls import ControlList


# TO DO: write specifications

class StatsList(ControlList):
    def __init__(self, name, data):
        ControlList.__init__(self, name)
        self.horizontalHeaders = ['Id', 'Title', 'Description', 'Genre', 'Times']
        self.value = [[x[0].id, x[0].title, x[0].description, x[0].genre, x[1]] for
                      x in
                      data]
        self.selectEntireRow = True
        self.readOnly = True

    def renderData(self, data):
        self.value = [[x[0].id, x[0].title, x[0].description, x[0].genre, x[1]] for
                      x in
                      data]
