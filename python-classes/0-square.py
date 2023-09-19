"""This module is mostly on the __size which is considered private when used due to the double underscore"""

class Square:
    """This a class considered as a parent to all instances being made in this module """

    def __init__(self, size):
        """using a double underscore with a name after a function makes it private."""
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)
    """A function to a method showing the attribute my_square while raising an exception"""
    try:
        print(my_square.size)
    except AttributeError as e:
        print(e)

    try:
        print(my_square.__size)
    except AttributeError as e:
        print(e)