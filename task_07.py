s = input("Enter text:")
ch = input("Enter symbol:")

indexesString = ""
for i in range(len(s)):
    if s[i] == ch:
        if len(indexesString) > 0:
            indexesString += f", {i}"
        else:
            indexesString = f"{i}"

print(f"Symbol of '{ch}' in '{s}': {indexesString}")



