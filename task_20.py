import random

m = int(input("Enter the number of lines: "))
n = int(input("Enter number of columns: "))

matrix = [[random.randint(1, 9) for j in range(n)] for i in range(m)]

for row in matrix:
    row_sum = 0
    for element in row:
        print("{:<5}".format(element), end="")
        row_sum += element
    print("{:<5}".format(row_sum))

col_sums = [0] * n
for i in range(n):
    col_sum = 0
    for j in range(m):
        col_sum += matrix[j][i]
    col_sums[i] = col_sum
    print("{:<5}".format(col_sum), end="")


print("{:<5}".format(""), end="")

