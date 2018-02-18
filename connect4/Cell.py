import Constants


class Cell:
    '''
        A class used for describing one point of the board game
        Its main role is to describe whether an point is used by the computer or by the player
    '''

    def __init__(self, entity, x, y):
        '''

        :param entity: oneOf("human", "computer")
        :param x: the x coordinate
        :param y: the y coordinate
        '''
        self.__entity = entity
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def entity(self):
        return self.__entity

    @entity.setter
    def entity(self, enity):
        self.__entity = enity

    def __repr__(self):
        return '(' + str(self.__x) + ',' + str(self.y) + ')'

    def __str__(self):
        '''
        Used for representing the cells in the console UI
        :return: string
        '''
        if self.entity == Constants.COMPUTER:
            return "\033[1;91m⚫" + "\033[0;0m"
        elif self.entity == Constants.HUMAN:
            return "\033[93m⚫" + "\033[0;0m"
        else:
            return "⚪"

    def __eq__(self, other):
        return self.entity == other.entity and self.x == other.x and self.y == other.y
