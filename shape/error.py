class HourIsNegativeError(ValueError):
    pass

class LengthIsNegativeError(ValueError):

    def __init__(self, cause):
        self.__cause = cause

    def __str__(self):
        return f"LengthIsNegativeError with cause {self.__cause}"

class WidthIsNegativeError(ValueError):
    pass