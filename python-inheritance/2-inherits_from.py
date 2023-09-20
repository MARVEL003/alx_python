"""
    Check if the given object is an instance of a class
     Also if it is inherited from the specified class.

    Parameters:
        obj: Any Python object.
        a_class:class name to compare the type of the object against.

    Returns:
    True if the object is an instance of a subclass of the specified class;
    Otherwise False.
    Example:
        >>> class Animal:
        ...     pass
        ...
        >>> class Dog(Animal):
        ...     pass
        ...
        >>> class Cat(Animal):
        ...     pass
        ...
        >>> class Bird:
        ...     pass
        ...
        >>> obj1 = Dog()
        >>> obj2 = Cat()
        >>> obj3 = Bird()
        >>>
        >>> inherits_from(obj1, Animal)
        True
        >>> inherits_from(obj2, Animal)
        True
        >>> inherits_from(obj3, Animal)
        False
    """


def inherits_from(obj, a_class):
    """Check if the given object is an instance of a class
    Also if it is inherited from the specified class."""
    return (
        issubclass(type(obj), a_class) and
        type(obj) != a_class
    )