from Assignment9.CustomDictionaryPackage import filter
from Controllers.BaseController import BaseController
from Models.Client import Client
from Services.ClientValidator import ClientValidator


class ClientController(BaseController):
    '''
        Client controller class used for to manage the client repository
        a wrap up for the BaseController which "extends" the base operations of the base controller
    '''

    def __init__(self, repo):
        super().__init__(repo, Client)

    def addClient(self, clientId, name):
        '''
            A function that validates and adds a client to the repository
        :param clientId: integer
        :param name: string // cannot be empty
        :return: True if the client was added with success
        '''
        if ClientValidator.validate(clientId, name):
            clientId = int(clientId)
            client = Client(clientId, name)
            if self.getItemById(int(clientId)) is not False:
                raise ValueError("Error:\n The given id is already taken")
            self.addItem(client)
            return True

    def removeClient(self, clientId):
        '''
            A functions that removes a client from the repository and raises exception if there are any errors
        :param clientId: integer
        :return: True if the client was removed, False otherwise
        '''
        try:
            clientId = int(clientId)
            return self.removeItemById(clientId)
        except Exception as e:
            raise ValueError("Error:\n Client id must be integer")

    def updateClientName(self, clientId, clientName):
        '''
            A functions that updates a client's name and also provides data validation
        :param clientId: integer
        :param clientName: string // cannot be empty
        :return: True if the client was updated, False otherwise
        '''
        if ',' in clientName:
            raise ValueError("Error:\n Parameters should not contain the ',' character")
        try:
            clientId = int(clientId)
        except ValueError:
            raise ValueError("Error:\n Client Id must be integer")
        if len(clientName.strip()) == 0:
            raise ValueError("Error: \n Client Name should not be empty")
        item = self.getItemById(clientId)
        if item is not False:
            item = Client(*item)
            if len(clientName.strip()) > 0:
                item.name = clientName
                return self.updateItemById(int(clientId), item)
        else:
            raise ValueError("Error:\n Client Id cannot be find")

    def updateClientId(self, clientId, newId):
        '''
                A functions that updates a client's id and also provides data validation
            :param clientId: integer
            :param newId: integer
            :return: True if the client was updated, False otherwise
        '''
        try:
            clientId = int(clientId)
        except ValueError:
            raise ValueError("Error: \n Client Id cannot be string")
        try:
            newId = int(newId)
        except ValueError:
            raise ValueError("Error: \n New Client Id cannot be string")

        item = self.getItemById(clientId)
        newItem = self.getItemById(newId)

        if newItem is not False and clientId != newId:
            raise ValueError("Error:\n The given id is already taken")
        if item is not False:
            item = Client(*item)
            item.id = newId
            return self.updateItemById(clientId, item)

    def updateClient(self, clientId, name):
        '''
            A function that updates a clients's all fields and also provides data validation
        :param clientId: integer
        :param name: string // cannot be empty
        :return: True if the client was updated, False otherwise
        '''
        ClientValidator.validate(clientId, name)
        try:
            clientId = int(clientId)
        except ValueError:
            raise ValueError("Error: \n Client Id cannot be string")
        item = self.getItemById(clientId)
        if item is not False:
            item.name = name
            return self.updateItemById(clientId, item)

    def getAllClients(self):
        '''
            A function that returns all the clients from the repo
            :return: list of Client's objects
        '''
        clients = self.getAllItems()
        if clients is 0:
            return []
        return clients

    def getClientById(self, clientId):
        '''
            A function that returns a client from the repo by its id
        :param clientId: integer
        :return: Client object, False otherwise
        '''
        try:
            clientId = int(clientId)
        except ValueError:
            raise ValueError("Error:\n Movie id must be integer")
        client = self.getItemById(clientId)
        if client is not False:
            return client
        return client

    def searchClientByName(self, name):
        '''
            Returns of lists of clients that contains the given string in their name
        :param name: string
        :return: list of Clients
        '''
        if len(name) == 0:
            raise ValueError("Search input cannot be empty!")
        clientList = self.getAllClients()
        return list(filter(lambda movie: name.strip().lower() in movie.description.lower(), clientList))

    def searchClientById(self, id):
        id = id.strip()
        try:
            id = int(id)
        except ValueError:
            raise ValueError("Error:\n\tId must be integer")
        clients = self.getAllClients()
        return list(filter(lambda client: str(id) in str(client.id), clients))
