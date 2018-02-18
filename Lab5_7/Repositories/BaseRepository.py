from Repositories.RepositoryException import RepositoryException


class Repository:
    """
    Repository for storing IDObject instances
    """

    def __init__(self):
        self._data = {}

    def create(self, obj):
        if self.find(obj.id) is not False:
            raise RepositoryException("Element having id=" + str(obj.id) + " already stored!")
        self._data[obj.id] = obj

    def update(self, object):
        """
        Update the instance given as parameter. The provided instance replaces the one having the same ID
        :param object: The object that will be updated
        :raises: Repo1sitoryException in case the object is not contained within the repository
        """
        if self.find(object.id) is False:
            raise RepositoryException("Element not found!")
        self._data[object.id] = object

    def find(self, objectId):
        if objectId not in self._data.keys():
            return False
        return self._data[objectId]

    def delete(self, objectId):
        """
        Remove the object with given objectId from repository
        :param objectId:  The objectId that will be removed
        :return: the object that was removed
        :raises: RepositoryException if object with given objectId is not contained in the repository
        """
        object = self.find(objectId)
        if object is False:
            raise RepositoryException("Element not in repository!")
        del (self._data[objectId])

    def getAll(self):
        '''
            Returns all data
        :return:
        '''
        if len(self) == 0:
            return 0
        return list(self._data.values())

    def clear(self):
        '''
        Clear's the in memory dict
        :return:  None
        '''
        self._data = {}

    def __len__(self):
        return len(self._data)

    def __str__(self):
        r = ""
        for e in self._data.values():
            r += str(e)
            r += "\n"
        return r
