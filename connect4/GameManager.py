import copy
import random

import Constants


class GameManager:
    '''
        Class used for managing the game and it's resources - board, moves, AI
    '''

    def __init__(self, board, difficulty):
        self.__board = board
        self.__difficulty = difficulty

    def boardToString(self):
        '''
        :return: string
        '''
        return str(self.__board)

    def move(self, column, entity):
        '''
            Functions that checks a column and places the point in the desired spot
        :param column: integer
        :param entity: oneOf("human", "computer")
        :return: None
        :raises: ValuerError
        '''
        try:
            column = int(column)
        except ValueError:
            raise ValueError("Error: column must be integer!")
        self.__board.move(column - 1, entity)
        return True

    def checkWinner(self, entity):
        '''
            Check if a given entity had won the game
        :param entity: oneOf("human", "computer")
        :return: True if victory, False otherwise
        '''
        return self.__board.isWinner(entity)

    def getPotentialMoves(self, board, entity, difficulty):
        '''
         This is the functions that represents the brain of the AI of the game
         it tries every possibilty and returns an array of "grades" for each column
        :param board: the board for which we want to determine the potential moves
        :param entity: oneOf("human", "computer")
        :param difficulty: t
        :return: 
        '''
        if difficulty == 0 or board.isBoardFull(board):
            return [0] * board.width
        if entity == Constants.HUMAN:
            enemyEntity = Constants.COMPUTER
        else:
            enemyEntity = Constants.HUMAN

        potentialMoves = [0] * board.width
        for firstMove in range(board.width):
            auxBoard = copy.deepcopy(board)
            if not auxBoard.isValidMove(firstMove):
                continue
            auxBoard.move(firstMove, entity)
            if auxBoard.isWinner(entity):
                potentialMoves[firstMove] = 1
                break
            else:
                if auxBoard.isBoardFull(auxBoard):
                    potentialMoves[firstMove] = 0
                else:
                    for counterMove in range(auxBoard.width):
                        auxboard2 = copy.deepcopy(auxBoard)
                        if not auxboard2.isValidMove(counterMove):
                            continue
                        auxboard2.move(counterMove, enemyEntity)
                        if auxboard2.isWinner(enemyEntity):
                            potentialMoves[firstMove] = -1
                            break
                        else:
                            results = self.getPotentialMoves(auxboard2, entity, difficulty - 1)
                            potentialMoves[firstMove] += (sum(results) / board.width) / board.width
        return potentialMoves

    def computerMove(self):
        '''
        It covers all the possibilities and chooses one random move from the ones with the best fitness
        '''
        potentialMoves = self.getPotentialMoves(self.__board, Constants.COMPUTER, self.__difficulty)
        bestMoveFitness = -1
        for i in range(self.__board.width):
            if potentialMoves[i] > bestMoveFitness and self.__board.isValidMove(i):
                bestMoveFitness = potentialMoves[i]
        bestMoves = []
        for i in range(len(potentialMoves)):
            if potentialMoves[i] == bestMoveFitness and self.__board.isValidMove(i):
                bestMoves.append(i)
        i = random.choice(bestMoves) + 1
        self.move(i, Constants.COMPUTER)
        return i

    def clear(self):
        self.__board.board = self.__board.createBoard()

    def isFull(self):
        return self.__board.isBoardFull(self.__board)

    def boardWidth(self):
        return self.__board.width

    def boardHeight(self):
        return self.__board.height

    def board(self):
        return self.__board
