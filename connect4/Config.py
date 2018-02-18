import Constants
from Board import Board
from Console import Console
from GUI import GUI
from GameManager import GameManager


class Config:
    '''
    Reads the configs settings from the given file and changes the game properties
    '''

    def __init__(self, config):
        '''
        The class constructor
        :param config: the file name
        '''
        self.__config = config
        self.__settings = {}

    def readSettings(self):
        '''
        Reads the settings from the given file
        '''
        print(self.__config)
        with open(self.__config, "r") as f:
            lines = f.read().split("\n")
            settings = {}
            for line in lines:
                setting = line.split("=")
                if len(setting) > 1:
                    self.__settings[setting[0].strip()] = setting[1].strip()

    def config(self):
        '''
        :return: The game settings
        '''
        ui = None
        oponent = None
        board = Board(int(self.__settings['width']), int(self.__settings['height']))
        gm = GameManager(board, int(self.__settings['difficulty']))
        if self.__settings['ui'] == Constants.CONSOLE:
            ui = Console(gm)
        if self.__settings['ui'] == Constants.GUI:
            ui = GUI(gm)
        return ui
