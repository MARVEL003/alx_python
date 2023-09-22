"""
Defining a class that has both private and instances
"""


class Base:
    """
    Creating our first class.
    """
    """
     A private class
     """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        function __init__ calling self and an id
        """
        self.id = None

        """
        Initialize instance with id.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects