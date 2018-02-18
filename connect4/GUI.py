import random
import sys

import Constants
import pygame
from pygame.locals import *


class GUI:
    def __init__(self, gm):
        self.__gm = gm
        self.clock = pygame.time.Clock()
        self.humanWinImg = pygame.image.load('images/win.png')
        self.computerWinImg = pygame.image.load('images/lost.png')
        self.tieImg = pygame.image.load('images/tie.png')
        self.rectWin = self.humanWinImg.get_rect()
        self.screenHeight = min(720, self.__gm.boardHeight() * Constants.CELLSIZE + 200)
        self.screenWidth = min(1080, self.__gm.boardWidth() * Constants.CELLSIZE + 200)
        self.rectWin.center = (int(self.screenWidth / 2), int(self.screenHeight / 2))
        self.display = pygame.display.set_mode((self.screenWidth, self.screenHeight))
        self.marginX = int((self.screenWidth - self.__gm.boardWidth() * Constants.CELLSIZE) / 2)
        self.marginY = int((self.screenHeight - self.__gm.boardHeight() * Constants.CELLSIZE) / 2)
        self.redToken = pygame.image.load('images/redCoin.PNG')
        self.redToken = pygame.transform.smoothscale(self.redToken, (Constants.CELLSIZE, Constants.CELLSIZE))
        self.blackToken = pygame.image.load('images/yellowCoin.PNG')
        self.blackToken = pygame.transform.smoothscale(self.blackToken, (Constants.CELLSIZE, Constants.CELLSIZE))
        self.boardImg = pygame.image.load('images/board.PNG')
        self.boardImg = pygame.transform.smoothscale(self.boardImg, (Constants.CELLSIZE, Constants.CELLSIZE))
        self.redCoin = pygame.Rect(int(Constants.CELLSIZE / 2),
                                   self.screenHeight - int(3 * Constants.CELLSIZE / 2), Constants.CELLSIZE,
                                   Constants.CELLSIZE)
        self.blackCoin = pygame.Rect(self.screenWidth - int(3 * Constants.CELLSIZE / 2),
                                     self.screenHeight - int(3 * Constants.CELLSIZE / 2),
                                     Constants.CELLSIZE,
                                     Constants.CELLSIZE)
        self.repeat = False

    def run(self):
        pygame.init()
        pygame.display.set_caption('Connect4')
        # main loop
        while True:
            self.playGame()

    def dropToken(self, column, entity):
        x = self.marginX + column * Constants.CELLSIZE
        y = self.marginY - column * Constants.CELLSIZE
        dropSpeed = 1.0

        lowestEmptySpace = self.__gm.board().getLowestPoint(column)

        while True:
            y += int(dropSpeed)
            dropSpeed += 0.5
            if int((y - self.marginY) / Constants.CELLSIZE) >= lowestEmptySpace:
                return
            self.boardToImg({'x': x, 'y': y, 'entity': entity})
            pygame.display.update()
            self.clock.tick()

    def __humanMove(self):
        isDragging = False
        x, y = None, None
        while True:
            for event in pygame.event.get():  # listen to every event in the game
                if event.type == QUIT:  # we quit the game
                    pygame.quit()
                    sys.exit()
                    # if we touch the red point
                elif event.type == MOUSEBUTTONDOWN and not isDragging and self.redCoin.collidepoint(event.pos):
                    # we start to drag the point.
                    isDragging = True
                    x, y = event.pos
                elif event.type == MOUSEMOTION and isDragging:
                    # we update the event position
                    x, y = event.pos
                elif event.type == MOUSEBUTTONUP and isDragging:
                    # if we were dragging the button now we have let it drop
                    if y < self.marginY and self.marginX < x < self.screenWidth - self.marginX:
                        # we calculate if we have dropped the point in a correct spot
                        column = int((x - self.marginX) / Constants.CELLSIZE)
                        try:
                            # we try to make the move
                            if self.__gm.move(column + 1, Constants.HUMAN):
                                # we animate the dropping
                                self.dropToken(column, Constants.HUMAN)
                                # we print the board to the screen
                                self.boardToImg()
                                # we update the game display
                                pygame.display.update()
                        except ValueError as e:
                            if "full" in str(e):
                                self.repeat = True
                            pass
                        pygame.display.update()
                        return
                    # we reset the event position after the dropping
                    x, y = None, None
                    isDragging = False
            if x is not None and y is not None:
                # we print the boar with the given position
                self.boardToImg({'x': x - int(Constants.CELLSIZE / 2), 'y': y - int(Constants.CELLSIZE / 2),
                                 'entity': Constants.HUMAN})
            else:
                self.boardToImg()
            pygame.display.update()
            self.clock.tick()

    def __computerMove(self):
        '''
            A function that animates the AI's move
        '''
        # we call the AI to perform its move
        column = self.__gm.computerMove()
        # we start animating the AI's move
        x = self.blackCoin.left
        y = self.blackCoin.top
        speed = 2.0
        # moving the point vertically along the board
        while y > (self.marginY - Constants.CELLSIZE):
            y -= int(speed)
            speed += 0.5
            self.boardToImg({'x': x, 'y': y, 'entity': Constants.COMPUTER})
            pygame.display.update()
            self.clock.tick()
        # moving the point horizontally along the board
        y = self.marginY - Constants.CELLSIZE
        speed = 1.0
        while x > (self.marginX + column * Constants.CELLSIZE):
            x -= int(speed)
            speed += 0.5
            self.boardToImg({'x': x, 'y': y, 'entity': Constants.COMPUTER})
            pygame.display.update()
            self.clock.tick()
        # we animate the dropping of the AI's move
        self.dropToken(column - 1, Constants.COMPUTER)

    def boardToImg(self, choosenPoint=None):
        '''
        A function that draws the board game
        :param choosenPoint: the next token to be placed
                - dictionary of type
                {
                    'x': x coordinate,
                    'y': y coordinate,
                    'entity': oneOf("human", "computer")
        '''
        # set the backgroundColor
        self.display.fill(Constants.BG)
        # create the cell accordingly to the constants
        cell = pygame.Rect(0, 0, Constants.CELLSIZE, Constants.CELLSIZE)

        # display the board point
        for x in range(self.__gm.boardWidth()):
            for y in range(self.__gm.boardHeight()):
                cell.topleft = (self.marginX + (x * Constants.CELLSIZE), self.marginY + (y * Constants.CELLSIZE))
                if self.__gm.board().board[y][x].entity == Constants.HUMAN:
                    self.display.blit(self.redToken, cell)
                elif self.__gm.board().board[y][x].entity == Constants.COMPUTER:
                    self.display.blit(self.blackToken, cell)
        # display the next point that was chosen
        if choosenPoint != None:
            if choosenPoint['entity'] == Constants.HUMAN:
                self.display.blit(self.redToken,
                                  (choosenPoint['x'], choosenPoint['y'], Constants.CELLSIZE, Constants.CELLSIZE))
            elif choosenPoint['entity'] == Constants.COMPUTER:
                self.display.blit(self.blackToken,
                                  (choosenPoint['x'], choosenPoint['y'], Constants.CELLSIZE, Constants.CELLSIZE))
        # display the board itself
        for x in range(self.__gm.boardWidth()):
            for y in range(self.__gm.boardHeight()):
                cell.topleft = (self.marginX + (x * Constants.CELLSIZE), self.marginY + (y * Constants.CELLSIZE))
                self.display.blit(self.boardImg, cell)
        # display the left and right coins
        self.display.blit(self.redToken, self.redCoin)
        self.display.blit(self.blackToken, self.blackCoin)

    def playGame(self):
        # randomly choose one player
        if random.randint(0, 1) == 0:
            turn = Constants.COMPUTER
        else:
            turn = Constants.HUMAN

        while True:
            if turn == Constants.HUMAN:
                # the human's move
                self.__humanMove()
                # check if he is the winner or not
                if self.__gm.checkWinner(Constants.HUMAN):
                    # if so, we end the loop
                    win = self.humanWinImg
                    break
                # change the turn
                turn = Constants.COMPUTER
            else:
                if self.repeat:
                    turn = Constants.HUMAN
                    self.repeat = False
                    continue
                # the computer's move
                self.__computerMove()
                # check if the computer is the winner or not
                if self.__gm.checkWinner(Constants.COMPUTER):
                    # if so, we end the loop
                    win = self.computerWinImg
                    break
                turn = Constants.HUMAN
            if self.__gm.isFull():
                win = self.tieImg
                break

        while True:
            # loop until the player clicks or quits the game
            self.boardToImg()
            self.display.blit(win, self.rectWin)
            pygame.display.update()
            self.clock.tick()
            for event in pygame.event.get():  # check if we should quit or restart the game
                if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONUP:
                    self.__gm.clear()
                    return
