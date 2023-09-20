"""
    A base class representing geometry.

    It is to be used as a base for other geometry-related classes.
    It currently does not have any attributes or methods defined.

    Public Methods:
    - area(self): Calculate the area of the geometry.
        Raises:
         Exception: This method is not implemented in the base class.

    - integer_validator(self, name, value): Validate an integer value.
        Parameters:
         name (str): The name of the value being validated.
         value: The value to be validated.
        Raises:
         TypeError: If the value is not an integer.
         ValueError: If the value is less than or equal to 0.
    """


class BaseGeometry:
    """
    A base class representing geometry.

    It is to be used as a base for other geometry-related classes.
    It currently does not have any attributes or methods defined.
    """


class BaseGeometryMetaClass(type):
    def __dir__(cls):
        return [
            attribute for attribute in super().__dir__()
            if attribute != '__init_subclass__'
        ]


# I imported rather than writing the whole code
Rectangle = __import__("7-rectangle").Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    Public Methods:
    - __init__(self, size): Initialize a square with size.
    """

    def __init__(self, size):
        """
        Initialize a square with size.

        Parameters:
            size (int): The size of the square (both width and height).
        """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    # I also added this to fix the error
    def __dir__(cls):
        """
        Metaclass fix
        """
        return [
            attribute for attribute in super().__dir__()
            if attribute != '__init_subclass__']