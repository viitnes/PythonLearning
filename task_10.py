n = [int(s) for s in input("Enter nums: ").split()]
k = int(input("Enter index: "))

for i in range(k + 1, len(n)):
    n[i - 1] = n[i]
n.pop()

print("\nDisplay list without removed element:", ' '.join([str(i) for i in n]))
