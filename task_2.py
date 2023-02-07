a = int(input("Enter num of students in Class 1: "))
b = int(input("Enter num of students in Class 2: "))
c = int(input("Enter num of students in Class 3: "))

n = (a // 2 + a % 2)
m = (b // 2 + b % 2)
o = (c // 2 + c % 2)

print('\nNumber of tables: ', n + m + o)
