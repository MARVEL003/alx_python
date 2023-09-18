def raise_exception():
    a = 15
    b = "classic"
    result = a + b

    if __name__ == "__main__":
        try:
            raise_exception()
        except TypeError as te:
            print("Exception raised")