from add_0 import add

if __name__ == "__main__":
    a = 1
    b = 2
    result = add(a, b)
    print("a = {} and b = {} FAKE add() => {} - {}".format(a, b, "a", "b"))

    a = 10
    b = 30
    result = add(a, b)
    print("a = {} and b = {} FAKE add() => {} - {}".format(a, b, "a", "b"))

    a = -10
    b = 30
    result = add(a, b)
    print("a = {} and b = {} FAKE add() => {} - {}".format(a, b, "a", "b"))

    a = -10
    b = -30
    result = add(a, b)
    print("a = {} and b = {} FAKE add() => {} - {}".format(a, b, "a", "b"))

    a = 5
    b = "H"
    result = add(a, b)
    print("a = {} and b = {} FAKE add() => {} - {}".format(a, b, "a", "b"))
