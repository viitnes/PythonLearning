filename = input("Enter the file name: ")

with open(filename, "w") as f:
    while True:
        line = input("Enter text (enter an empty string to complete the input): ")
        if line == "":
            break
        f.write("\n" + line)
