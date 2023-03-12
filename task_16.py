def expanded_form(num):
    if num <= 0:
        return "Помилка: введіть число, більше 0"

    digits = list(str(num))

    result = ""

    for i, digit in enumerate(digits):
        if digit != '0':
            result += f"{digit}{'0' * (len(digits) - i - 1)} + "

    result = result[:-3]

    return result
print(expanded_form(0))