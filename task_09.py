s = list(map(int, input("Enter nums: ").split()))
index = 1
greatNeighbors = 0

while index < len(s) - 1:
    if s[index - 1] < s[index] > s[index + 1]:
        greatNeighbors += 1
        index += 2
    else:
        index += 1
print("\nWithdraw how many elements in this list are more than two of their neighbors:",(greatNeighbors))
