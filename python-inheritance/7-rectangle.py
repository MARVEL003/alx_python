"""
    A base class representing geometry.

    This class is intended to be used as a base for other geometry-related classes.
    It currently does not have any attributes or methods defined.

    Public Methods:
    - area(self): Calculate the area of the geometry.
        Raises:
            NotImplementedError: This method is not implemented in the base class.

    - integer_validator(self, name, value): Validate an integer value.
        Parameters:
            name (str): The name of the value being validated (assumed to be a string).
            value: The value to be validated.
        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
    """


class BaseGeometry:
    """
    A base class representing geometry.

    This class is intended to be used as a base for other geometry-related classes.
    It currently does not have any attributes or methods defined.
    """


class BaseGeometryMetaClass(type):
    def __dir__(cls):
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']


class BaseGeometry(metaclass=BaseGeometryMetaClass):
    """
    A base class representing geometry
    """

    def __dir__(self):
        """
        Customization of the attributes visible when calling `dir()`.
        """
        return [attribute for attribute in super().__dir__() if attribute != '__init_subclass__']

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Parameters:
            name (str): The name of the value being validated (assumed to be a string).
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Public Methods:
    - __init__(self, width, height): Initialize a rectangle with width and height.
    - area(self): Calculate the area of the rectangle.
    - __str__(self): Return a string representation of the rectangle.
    """

    def __init__(self, width, height):
        """
        Initialize a rectangle with width and height.

        Parameters:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string with the rectangle description in the format '[Rectangle] <width>/<height>'.
        """
        return f"[Rectangle] {self.__width}/{self.__height}"