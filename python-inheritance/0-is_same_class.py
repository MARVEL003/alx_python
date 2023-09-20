"""
    Check if the given object is exactly an instance of the specified class.

    Parameters:
        obj: Any Python object.
        a_class: A Python class or class name to compare the type of the object against.

    Returns:
        bool: True if the object is an instance of the specified class; otherwise, False.

    Example:
        >>> class MyClass:
        ...     pass
        ...
        >>> obj1 = MyClass()
        >>> obj2 = "Hello"
        >>> obj3 = 42
        >>>
        >>> is_same_class(obj1, MyClass)
        True
        >>> is_same_class(obj2, str)
        True
        >>> is_same_class(obj3, list)
        False
    """


def is_same_class(obj, a_class):
    """
    Check if the given object is exactly an instance of the specified class.
    """
    return type(obj) is a_class