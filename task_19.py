import random

def sort_matrix():
    M = int(input("Enter size of matrix: "))
    matrix = [[random.randint(1, 50) for j in range(M)] for i in range(M)]
    column_sums = [sum(column) for column in zip(*matrix)]
    column_indices = [i for i in range(M)]
    for i in range(M - 1):
        for j in range(M - i - 1):
            if column_sums[j] > column_sums[j + 1]:
                column_sums[j], column_sums[j + 1] = column_sums[j + 1], column_sums[j]
                column_indices[j], column_indices[j + 1] = column_indices[j + 1], column_indices[j]
                for k in range(M):
                    matrix[k][j], matrix[k][j + 1] = matrix[k][j + 1], matrix[k][j]
    for j in range(M):
        if j % 2 == 0:
            column = [matrix[i][j] for i in range(M)]
            column.sort()
            column = column[::-1] if j % 4 == 0 else column
            for i, val in enumerate(column):
                matrix[i][j] = val
    for row in matrix:
        for item in row:
            print("{:4d}".format(item), end="")
        print()
    for i in range(M):
        print("{:4d}".format(column_sums[i]), end="")
    print()

sort_matrix()
