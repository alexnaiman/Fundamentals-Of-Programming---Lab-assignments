from Repositories.BaseRepository import Repository


class InMemoryRepository(Repository):
    '''
        A generic class for a repository for a given class
    '''

    def __init__(self):
        '''
            The constructor of the Repository class
        :param fileName: the location of the file we want to read from
        :param name: the name of the repository
        '''
        super().__init__()

    def getItemById(self, itemId):
        return self.find(itemId)

    def getAllLines(self):
        '''
            A function that returns all the lines from file
        :return: a list of lists of form (*params) where params are the attributes of the given class
        '''
        return self.getAll()

    def createItem(self, item):
        '''
            Create a new item in the repository and adds it to the file as a new line
        :param item: object - the item we want to add in the repository
        :return: returns True if there wasn't any errors and we successfully added the new item
        '''
        self.create(item)
        return True

    def updateItemById(self, itemId, item):
        '''
            A function that updates an item from the repository by a given id
        :param itemId: the id of the item we want to modify
        :param item: the item with the new given properties
        :return: returns True if there wasn't any errors and the item was updated with success
        '''
        if self.getItemById(itemId) is False:
            return False
        self.update(item)
        return True

    def deleteItemById(self, itemId):
        '''
            A functions that deletes an item by a given id
        :param itemId: the item's id we want to delete
        :return: True, if there wasn't any errors and the item was successfully deleted
        '''
        self.delete(itemId)

    def __str__(self):
        return Repository.__str__(self)
