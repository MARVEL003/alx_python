def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, element in enumerate(row):

            if index != 0:
                print(" ", end="")

            print("{:d}".format(element), end="")
        print()


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
if __name__ == "__main__":
    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()