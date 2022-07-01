
#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 1
        for col in row:
             print("{}".format(col), end="")
             if i != len(row):
                 print(" ", end="")
             else:
                 print('')
             i += 1
