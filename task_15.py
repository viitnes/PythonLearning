#Спочатку я намагався зробити таким методом, але довго не міг зрозуміти як зробити останню фігуру


#Figure A
height = int(input("Enter height of figure: "))

for i in range(height):
    if i == 0:
        print(" " * (height - 1) + "*")
    elif i == height - 1:
        print("* " * (height - 1) + "*")
    else:
        print(" " * (height - i - 1) + "*" + " " * (2 * i - 1) + "*")


#Figure B
height = int(input("Enter height of figure: "))

for i in range(height):
    print(" " * (height - i - 1), end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

#Figure C
height = int(input("Enter height of figure: "))

for i in range(height):
    for j in range(height-i-1):
        print(" ", end="")
    for j in range(2*i+1):
        print("*", end="")
    print()
for i in range(height):
    for j in range(i):
        print(" ", end="")
    for j in range(2*(height-i)-1):
        if j == 0 or j == 2*(height-i)-2 or i == height-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Потім передивився урок з розбором домашок і зробив вашим методом всі фігури

def triangle_up(height, in_l=" ", in_r=" ", in_m=" "):
    for i in range(height):
        print(" " * (height - i), end="")
        if i != 0:
            print("*", end="")
            print(in_l * (i-1), end="")
            print(in_m, end="")
            print(in_r * (i-1), end="")
            print("*", end="")
        else:
            print("*", end="")
        print()
    print("*" * (height * 2 +1))

def triangle_down(height, in_l=" ", in_r=" ", in_m=" "):
    for i in range(height-1, -1, -1):
        print(" " * (height - i), end="")
        if i != 0:
            print("*", end="")
            print(in_l * (i-1), end="")
            print(in_m, end="")
            print(in_r * (i-1), end="")
            print("*", end="")
        else:
            print("*", end="")
        print()
    print("*" * (height * 2 +1))

if __name__ == "__main__":
    triangle_up(8)
    print()
    triangle_up(8, in_l="*", in_m="*", in_r="*")
    print()
    triangle_up(8, in_l="*", in_m="*", in_r="*")
    triangle_down(8)
    print()
    triangle_up(8, in_l="*", in_m="*", in_r="*")
    triangle_down(8, in_m="*")
    print()