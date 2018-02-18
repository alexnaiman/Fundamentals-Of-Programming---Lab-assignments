import mysql.connector
from Repositories.BaseRepository import Repository
from mysql.connector import errorcode


class SqlRepo(Repository):
    '''
        A generic class for a repository for a given class
    '''

    def __init__(self, config, objFromSql, objToSql, db, db_params):
        '''
            The constructor of the Repository class
        :param fileName: the location of the file we want to read from
        :param name: the name of the repository
        '''
        super().__init__()
        self.__config = config
        self.__objFromSql = objFromSql
        self.__objToSql = objToSql
        self.__db = db
        self.__db_params = db_params

    def getItemById(self, itemId):
        command = "SELECT * FROM " + self.__db + " where id = " + str(itemId)
        try:
            cnx = mysql.connector.connect(**self.__config)
            cursor = cnx.cursor()
            cursor.execute(command)
            data = cursor.fetchall()
            cnx.commit()
            if len(data) > 0:
                return self.__objFromSql(*data[0])
            return False
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError("Database does not exist")
            else:
                pass
        else:
            cnx.close()

    def executeSqlCommand(self, command):
        try:
            cnx = mysql.connector.connect(**self.__config)
            cursor = cnx.cursor()
            cursor.execute(command)
            data = cursor.fetchall()
            cnx.commit()
            return self.__objFromSql(*data[0])
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError("Database does not exist")
            else:
                pass
        else:
            cnx.close()

    def getAllLines(self):
        '''
            A function that returns all the lines from file
        :return: a list of lists of form (*params) where params are the attributes of the given class
        '''
        command = "SELECT * from " + self.__db
        try:
            cnx = mysql.connector.connect(**self.__config)
            cursor = cnx.cursor()
            cursor.execute(command)
            data = cursor.fetchall()
            cnx.commit()
            return list(map(lambda x: self.__objFromSql(*x), data))
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError("Database does not exist")
            else:
                raise ValueError(err)
        else:
            cnx.close()

    def createItem(self, item):
        '''
            Create a new item in the repository and adds it to the file as a new line
        :param item: object - the item we want to add in the repository
        :return: returns True if there wasn't any errors and we successfully added the new item
        '''
        if self.getItemById(item) is not None:
            raise ValueError("The given id is l")
        command = "INSERT INTO " + self.__db + self.__db_params + " Values("
        item = self.__objToSql(item)
        sqlItem = ""
        for i in item:
            if item.index(i) != len(item) - 1:
                if isinstance(i, int):
                    sqlItem += '%s, ' % i
                else:
                    sqlItem += "'%s', " % (i)
            else:
                sqlItem += "'%s'" % (i)

        command = command + sqlItem + ");"
        try:
            cnx = mysql.connector.connect(**self.__config)
            cursor = cnx.cursor()
            cursor.execute(command)
            cnx.commit()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError("Database does not exist")
            else:
                print(err)
                pass
        else:
            cnx.close()
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
        self.deleteItemById(itemId)
        self.createItem(item)
        return True

    def deleteItemById(self, itemId):
        '''
            A functions that deletes an item by a given id
        :param itemId: the item's id we want to delete
        :return: True, if there wasn't any errors and the item was successfully deleted
        '''
        command = "Delete from " + self.__db + " where id= " + str(itemId)
        try:
            cnx = mysql.connector.connect(**self.__config)
            cursor = cnx.cursor()
            cursor.execute(command)
            cnx.commit()
            return True
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise ValueError("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise ValueError("Database does not exist")
            else:
                raise ValueError(str(err))
        else:
            cnx.close()

    def __str__(self):
        return Repository.__str__(self)
