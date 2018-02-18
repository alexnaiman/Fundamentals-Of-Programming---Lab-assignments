from Models.ObjId import ObjId


class Client(ObjId):
    '''
        Movie Model which encapsulate all the necessary fields for a movie
    '''

    def __init__(self, id, name):
        super().__init__(id)
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __str__(self):
        return str(self.id) + ", " + str(self.name)

    def __eq__(self, other):
        if self.id == other.id and self.name == other.name:
            return True
        return False

    def __ne__(self, other):
        """Overrides the default implementation (unnecessary in Python 3)"""
        return not self.__eq__(other)

    @staticmethod
    def clientFromFile(params):
        params = [param.strip() for param in params.split(',')]
        cId = int(params[0].strip())
        name = params[1].strip()
        return Client(cId, name)

    @staticmethod
    def clientToFile(client):
        return str(client)

    @staticmethod
    def clientFromJson(json):
        id = json['_ObjId__id']
        name = json['_Client__name']
        return Client(id, name)

    @staticmethod
    def clientToSql(client):
        return client.id, client.name
