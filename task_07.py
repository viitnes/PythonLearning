s = input("Enter text:")
ch = input("Enter character:")

index = -1
is_found = False
while True:
    index = s.find(ch, index + 1)
    if index == -1:
        break
    print(f"Found at index {index}")
    is_found = True

if not is_found:
    print(f"The character '{ch}' was not found in '{s}'")


