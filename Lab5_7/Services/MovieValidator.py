from Models import Movie


class MovieValidator:
    '''
        Class which purpose is to validate data  needed to create a Movie object
    '''

    @staticmethod
    def validate(movieId, title, description, genre):
        '''
        Static function that validate each field and raises an error with a list of messages
        :param movieId: integer
        :param title: string
        :param description: string
        :param genre: one of MOVIE_GENRE
        :return: True if the number was validated correctly, raises errors otherwise
        '''
        errors = []
        try:
            movieId = int(movieId.strip())
        except ValueError:
            errors.append("Movie ID should not be string, expected integer")
        if len(title.strip()) == 0:
            errors.append(" Movie title should not pe empty")
        if ',' in title:
            errors.append(" Movie title cannot contain ',' character")
        if ',' in description:
            errors.append(" Movie description cannot contain ',' character")
        if ',' in genre:
            errors.append(" Movie genre cannot contain ',' character")
        if len(description.strip()) == 0:
            errors.append(" Movie description should not pe empty")
        if genre.strip().lower() not in Movie.MOVIE_GENRE:
            errors.append(" Movie Genre isn't valid")

        if len(errors) > 0:
            errorMessage = "Errors:\n "
            for error in errors:
                errorMessage += error + "\n"
            raise ValueError(errorMessage)
        return True
