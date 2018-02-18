import random

import Constants


class Console:
    '''
    UI cli
    '''

    def __init__(self, gm):
        self.__gm = gm
        self._exit = False

    def __addPoint(self):
        pass

    def __printBoard(self):
        print(self.__gm.boardToString())

    def __printSubmenu(self, listOfOptions):
        '''
            Prints a submenu from a dictioary
        :param listOfOptions: dictionary of form {key:(function, message)}
        '''
        for option in listOfOptions:
            print(listOfOptions[option][1])
        print("0.Exit")

    def __move(self):
        while True:
            column = input("What column do you choose?(-1 to exit the game)\n")
            if column.strip() == "-1":
                self._exit = True
                break
            try:

                self.__gm.move(column, "human")
                break
            except ValueError as e:
                print("\033[1;91m" + str(e) + "\033[0m")
                continue

    def run(self):
        if random.randint(0, 1) == 0:
            turn = Constants.COMPUTER
        else:
            turn = Constants.HUMAN
        while True and not self._exit:
            self.__printBoard()
            if turn == Constants.HUMAN:
                # Human player's turn.
                self.__move()
                # If the player is winning we end the game and display the message
                if self.__gm.checkWinner(Constants.HUMAN):
                    print("\033[93mYou win! Hooray! ☻")
                    self.__printBoard()
                    break
                turn = Constants.COMPUTER  # switch to other player's turn
            else:
                pass
                print("\033[93mYour's oponent turn")
                print(self.__gm.computerMove())
                turn = Constants.HUMAN
                # If the computer is winning we end the game and display the message
                if self.__gm.checkWinner(Constants.COMPUTER):
                    print("\033[1;91mYou lost! ☹ ")
                    self.__printBoard()
                    break
