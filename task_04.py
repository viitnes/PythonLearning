
c = int(input("Enter num: "))
a = 0
count = 0
max_value = c
min_value = c
paired = 0
unpaired = 0
while c != 0:
#Sum
    a += c
#Count
    count += 1
#Average
    b = a / count
#Min value
    if c < min_value:
        min_value = c
#Max value
    if c > max_value:
        max_value = c
#Paired and unpaired nums
    if c % 2 == 0:
        paired += 1
    else:
        unpaired += 1
        c = c // 10
    c = int(input("Enter num: "))
    if c == 0:
        break

print('\nCount of entered numbers:',count)
print('\nSum of entered numbers:',a)
print('\nAverage of entered numbers:',b)
print('\nMinimum value of entered numbers:',min_value)
print('\nMaximum value of entered numbers:',max_value)
print('\nPaired nums',paired)
print('\nUnpaired nums',unpaired)



