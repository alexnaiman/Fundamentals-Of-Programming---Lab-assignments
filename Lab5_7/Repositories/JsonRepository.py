import json

from Repositories.BaseRepository import Repository


class JsonRepo(Repository):
    '''
        A generic class for a repository for a given class
    '''

    def __init__(self, fileName, name, objFromJson):
        '''
            The constructor of the Repository class
        :param fileName: the location of the file we want to read from
        :param name: the name of the repository
        '''
        super().__init__()
        self.__fileName = fileName
        self.__name = name
        self.__objFromJson = objFromJson
        self.readAllLines()

    def readAllLines(self):
        self.clear()
        f = open(self.__fileName, "rb")

        """
        You cannot json-deserializen an empty file
            - ValueError means the file is empty
            - Exception means no file, not accessible and so on...
            - finally makes sure we close the input file, regardless of error
        """
        try:
            data = json.loads(f.read().decode())
            for line in data:
                self.create(self.__objFromJson(line))
        except ValueError:
            self._data = {}
        except Exception as e:
            raise e
        finally:
            f.close()

    def writeAllToFile(self):

        f = open(self.__fileName, "wb")
        f.write(json.dumps([x.__dict__ for x in list(self._data.values())], indent=4, sort_keys=True,
                           ).encode())
        f.close()

    def getItemById(self, itemId):
        self.readAllLines()
        return self.find(itemId)

    def getAllLines(self):
        '''
            A function that returns all the lines from file
        :return: a list of lists of form (*params) where params are the attributes of the given class
        '''
        self.readAllLines()
        return self.getAll()

    def createItem(self, item):
        '''
            Create a new item in the repository and adds it to the file as a new line
        :param item: object - the item we want to add in the repository
        :return: returns True if there wasn't any errors and we successfully added the new item
        '''
        self.readAllLines()
        self.create(item)
        self.writeAllToFile()
        return True

    def updateItemById(self, itemId, item):
        '''
            A function that updates an item from the repository by a given id
        :param itemId: the id of the item we want to modify
        :param item: the item with the new given properties
        :return: returns True if there wasn't any errors and the item was updated with success
        '''
        self.readAllLines()
        if self.getItemById(itemId) is False:
            return False
        self.update(item)
        self.writeAllToFile()
        return True

    def deleteItemById(self, itemId):
        '''
            A functions that deletes an item by a given id
        :param itemId: the item's id we want to delete
        :return: True, if there wasn't any errors and the item was successfully deleted
        '''
        self.readAllLines()
        self.delete(itemId)
        self.writeAllToFile()

    def __str__(self):
        return Repository.__str__(self)
