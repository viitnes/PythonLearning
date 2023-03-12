def number_collaps(num):
    if num <= 0:
        return "Error: enter num > 0"
    while num >= 10:
        digits = list(str(num))
        num = sum(int(d) for d in digits)

    return num

print(number_collaps(123))
print(number_collaps(0))