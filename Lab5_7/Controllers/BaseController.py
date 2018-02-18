class BaseController:
    actions = []
    redoActions = []
    lastPerformedAction = -1
    canRecord = True
    isGrouped = False

    def __init__(self, repo, constructor):
        self.__repo = repo
        self.__constructor = constructor

    @property
    def repo(self):
        return self.__repo

    def setGroup(self, value):
        BaseController.isGrouped = value

    def addItem(self, item):
        '''
        Add an item to the list
        :param item: item - object of desired type
        :return: True if the item was added successfully
        '''
        if BaseController.canRecord:
            if len(BaseController.redoActions) > 0:
                BaseController.redoActions = []
            BaseController.actions.append(
                [BaseController.isGrouped, Command(self.addItem, [item], self.removeItemById, [int(item.id)])])
        return self.__repo.createItem(item)

    def removeItemById(self, itemId):
        '''
        Removes an item by its ID
        :param itemId: integer - item's id which we want to remove
        :return: True if the item was added successfully
        '''
        if BaseController.canRecord and self.getItemById(itemId) is not False:
            if len(BaseController.redoActions) > 0:
                BaseController.redoActions = []
            BaseController.actions.append([BaseController.isGrouped,
                                           Command(self.removeItemById, [itemId], self.addItem,
                                                   [self.getItemById(itemId)])])
        return self.__repo.deleteItemById(itemId)

    def updateItemById(self, itemId, item):
        '''
        Updates an item by its id
        :param itemId: integer
        :param item: intger
        :return: True if the item was updated, False otherwise
        '''
        if BaseController.canRecord and self.getItemById(itemId) is not False:
            if len(BaseController.redoActions) > 0:
                BaseController.redoActions = []
            BaseController.actions.append([BaseController.isGrouped,
                                           Command(self.updateItemById, [itemId, item], self.updateItemById,
                                                   [item.id, self.getItemById(itemId)])])
        return self.__repo.updateItemById(itemId, item)

    def getAllItems(self):
        '''
        Gets all item from the repo
        :return: list of all items (list of strings)
        '''
        return self.__repo.getAllLines()

    def getItemById(self, itemId):
        '''
        Returns an item from the repo by its id
        :param itemId: integer
        :return: ordered list with the item's fields
        '''
        return self.__repo.getItemById(itemId)

    def undo(self):
        if len(BaseController.actions) <= 0:
            raise ValueError("Nothing to undo here")
        BaseController.canRecord = False
        while BaseController.actions[-1][0]:
            BaseController.actions[-1][1].undo()
            BaseController.redoActions.append(BaseController.actions.pop())
        BaseController.actions[-1][1].undo()
        BaseController.redoActions.append(BaseController.actions.pop())
        BaseController.canRecord = True

    def redo(self):
        if len(BaseController.redoActions) <= 0:
            raise ValueError("Nothing to redo here")
        BaseController.canRecord = False
        BaseController.redoActions[-1][1].do()
        BaseController.actions.append(BaseController.redoActions.pop())
        while len(BaseController.redoActions) > 0 and BaseController.redoActions[-1][0]:
            BaseController.redoActions[-1][1].do()
            BaseController.actions.append(BaseController.redoActions.pop())
        if len(BaseController.redoActions) == 1:
            BaseController.redoActions[-1][1].do()
            BaseController.actions.append(BaseController.redoActions.pop())

        BaseController.canRecord = True


class Command:
    def __init__(self, redo, redoParams, undo, undoParams):
        self.__redo = redo
        self.__redoParams = redoParams
        self.__undo = undo
        self.__undoParams = undoParams

    def undo(self):
        self.__undo(*self.__undoParams)

    def do(self):
        self.__redo(*self.__redoParams)
