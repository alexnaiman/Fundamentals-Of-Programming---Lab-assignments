import Constants
from Cell import Cell


class Board:
    '''
     Class that represents the game board
    '''

    def __init__(self, width, height):
        '''
            The board's constructor
        :param width: int > 4
        :param height: int > 4
        '''
        self.__height = height
        self.__width = width
        self.board = self.createBoard()

    def createBoard(self):
        '''
            Function that creates an empty game board
        :return: matrix of cell
        '''
        board = []
        for x in range(self.__height):
            board.append([])
            for y in range(self.__width):
                board[x].append(Cell(Constants.EMPTY, x, y))
        return board

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def isBoardFull(self, board):
        '''

        :param board: matrix of cells
        :return: True if there are no empty spaces anywhere on the board.
        '''
        for x in range(board.height):
            for y in range(board.width):
                if board.board[x][y].entity == Constants.EMPTY:
                    return False
        return True

    def __str__(self):
        '''

        :return: string thate represents the game board
        '''
        b = "\033[93m "
        for x in range(self.width):
            b += str(x + 1) + " "
        b += "\033[0m\n"
        for row in self.board:
            for y in row:
                b += str(y) + " "
            b += "\n"
        return b

    def getLowestPoint(self, column):
        '''
        :param column: int
        :return: the row number of the lowest empty row in the given column.
        '''
        for y in range(self.height - 1, -1, -1):
            if self.board[y][column].entity == Constants.EMPTY:
                return y
        return -1

    def isValidMove(self, column):
        '''
        :param column: int
        :return: True if the column is valid or not
        '''
        if column < 0 or column >= self.width or self.board[0][column].entity != Constants.EMPTY:
            return False
        return True

    def move(self, column, entity):
        '''
        :param column: int
        :param entity: oneOf("human", "computer")
        '''
        if self.isValidMove(column):
            self.board[self.getLowestPoint(column)][column].entity = entity
        else:
            raise ValueError("Error: Column is full")

    def isWinner(self, entity):
        '''
         Check if the given entity is a winner or not
        :param entity: oneOf("computer", "human")
        :return: True if winner, false otherwise
        '''
        # checks the horizontal possibilities
        for x in range(self.height):
            for y in range(self.width - 3):
                if self.board[x][y].entity == entity and \
                                self.board[x][y + 1].entity == entity and \
                                self.board[x][y + 2].entity == entity and \
                                self.board[x][
                                            y + 3].entity == entity:
                    return True
        # checks vertical possibilities
        for x in range(self.height - 3):
            for y in range(self.width):
                if self.board[x][y].entity == entity and self.board[x + 1][y].entity == entity and self.board[x + 2][
                    y].entity == entity and \
                                self.board[x + 3][
                                    y].entity == entity:
                    return True

        # checks the / diagonal possibilities
        for x in range(self.height - 3):
            for y in range(self.width - 3):
                if self.board[x][y].entity == entity and self.board[x + 1][y + 1].entity == entity and \
                                self.board[x + 2][
                                            y + 2].entity == entity and self.board[x + 3][
                            y + 3].entity == entity:
                    return True
        # checks the / diagonal possibilities
        for x in range(self.height - 3):
            for y in range(3, self.width):
                if self.board[x][y].entity == entity and self.board[x + 1][y - 1].entity == entity and \
                                self.board[x + 2][
                                            y - 2].entity == entity and self.board[x + 3][
                            y - 3].entity == entity:
                    return True
        return False
