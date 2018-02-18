class ObjId:
    def __init__(self, id):
        """
        :type id: integer
        """
        self.__id = id

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id
