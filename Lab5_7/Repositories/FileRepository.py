from Repositories.BaseRepository import Repository


class FileRepository(Repository):
    '''
        A generic class for a repository for a given class
    '''

    def __init__(self, fileName, name, objToFile, objFromFile):
        '''
            The constructor of the Repository class
        :param fileName: the location of the file we want to read from
        :param name: the name of the repository
        '''
        super().__init__()
        self.__fileName = fileName
        self.__name = name
        self.__objToFile = objToFile
        self.__objFromFile = objFromFile
        self.__actualIndex = 0

    def readAllLines(self):
        '''
        Function that opens the file, read it content and convert it to the given objects
        :return:
        '''
        self.clear()
        try:
            with open(self.__fileName, 'r') as f:
                data = f.read().splitlines()
                for i in data:
                    if len(i) > 0:
                        self.create(self.__objFromFile(i))
        except IOError:
            raise ValueError("Data source error: cannot find item at " + str(self.__fileName) + " repository")

    def writeAllToFile(self):
        '''
        Function that writes all our data to file
        :return:
        '''
        try:
            with open(self.__fileName, 'w') as f:
                f.write(str(self))
        except IOError:
            pass

    def getItemById(self, itemId):
        '''
        Returns an item by its id
        :param itemId:
        :return: object
        '''
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
