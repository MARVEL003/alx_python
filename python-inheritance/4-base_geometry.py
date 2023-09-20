"""
    A base class representing geometry.

    This class is intended to be used as a base for other geometry-related classes.
    It currently does not have any attributes or methods defined.
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
            NotImplementedError: This method is not implemented in the base class.
        """
        raise Exception("area() is not implemented")