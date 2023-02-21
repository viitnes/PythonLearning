counter = {}
k = input("Enter text: ").split()
for word in k:
    if counter.get(word, None):
        counter[word] += 1
    else:
        counter[word] = 1
for word in counter:
    print(f"\nThe word '{word}' occurs '{counter[word]}' times in the text")
