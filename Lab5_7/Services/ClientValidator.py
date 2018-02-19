from functools import reduce


class ClientValidator:
    '''
        Class which purpose is to validate data needed to create a Client object
    '''

    @staticmethod
    def validate(clientId, name):
        '''
            Static function that validate each field and raises an error with a list of messages
        :param clientId: integer
        :param name: string // cannot be empty
        :return: True if the number was validated correctly, raises errors otherwise
        '''
        errors = []
        try:
            clientId = int(clientId.strip())
        except ValueError:
            errors.append("Client ID should not be string, expected integer!")
        if len(name.strip()) == 0:
            errors.append("Client Name should not pe empty!")
        if ',' in name:
            errors.append("Name cannot contain ',' character")

        if len(errors) > 0:
            errorMessage = reduce(lambda x, y: str(x) + '\n' + str(y), errors)
            errorMessage = "Errors:\n" + errorMessage
            raise ValueError(errorMessage)
        return True
