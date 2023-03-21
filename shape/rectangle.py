from shape.error import LengthIsNegativeError, WidthIsNegativeError

class Rectangle:
    """Class that represents rectangle with length and width.

    Detailed information about the rectangle.
    """

    def __init__(self, arg1, arg2):
        """

        :param arg1: The length of the rectangle. \n
        :type arg1: float
        :param arg2: The width of the rectangle.
        :type arg2: float

        :raise LengthIsNegativeError: In case arg1 is <= 0.0
        :raise WidthIsNegativeError: In case arg2 is <= 0.0
        """
        if arg1 <= 0:
            raise LengthIsNegativeError("In rectangle")
        if arg2 <= 0:
            raise WidthIsNegativeError

        self._length = arg1
        self._width = arg2

    def area(self):
        """ Calculates the area of the rectangle.

        :return: Calculated area.
        :rtype: float
        """
        return self._width * self._length

    def perimeter(self):
        """ Calculates the perimeter of the rectangle.

        :return: Calculated area.
        :rtype: float
        """
        return (self._width + self._length) * 2.0

    def __str__(self):
        """ String representation of rectangle

        :return: String with length and width
        :rtype: str
        """
        return f"{self.__class__.__name__}: length = {self._length}, width = {self._width}"

    def set_length(self, value):
        if value >= 0.0:
            self._length = value

    def get_length(self):
        return self._length