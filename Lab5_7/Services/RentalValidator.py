from Models import Movie
from functools import reduce
from datetime import date


class RentalValidator:
    @staticmethod
    def validate(rentalId, movieId, clientId, rentedDate, dueDate, returnedDate):
        errors = []
        dateRent = -1
        dateDue = -1
        try:
            movieId = int(movieId.strip())
        except ValueError:
            errors.append("Movie ID should not be string, expected integer")
        try:
            clientId = int(clientId.strip())
        except ValueError:
            errors.append("Client ID should not be string, expected integer")
        try:
            rentalId = int(rentalId.strip())
        except ValueError:
            errors.append("Rental ID should not be string, expected integer")
        if len(rentedDate) == 10:
            try:
                year, month, day = map(int, rentedDate.split('-'))
                dateRent = date(year, month, day)
            except Exception as e:
                errors.append("Rented Date is not in the correct format")
        else:
            errors.append("Rented date is not in the correct format")

        if int(returnedDate) != -1:
            if len(returnedDate) == 10:
                try:
                    year, month, day = map(int, returnedDate.split('-'))
                    datet = date(year, month, day)
                except Exception as e:
                    errors.append("Returned date is not in the correct format")
            else:
                errors.append("Returned date is not in the correct format")

        if len(dueDate) == 10:
            try:
                year, month, day = map(int, dueDate.split('-'))
                dateDue = date(year, month, day)
            except Exception as e:
                errors.append("Due date is not in the correct format")
        else:
            errors.append("Due date is not in the correct format")
        if isinstance(dateDue, date) and isinstance(dateRent, date):
            if dateDue < dateRent:
                errors.append("Due date cannot be smaller than rent date")
        if len(errors) > 0:
            errorMessage = "Errors:\n "
            for error in errors:
                errorMessage += error + "\n"

            raise ValueError(errorMessage)
        return True
