d = {
  'apple': ['malum', 'pomum', 'popula'],
  'fruit': ['baca', 'bacca', 'popum'],
  'punishment': ['malum', 'multa']
}

invert_d = {}

for key, value in d.items():
    for item in value:
        if invert_d.get(item):
            invert_d[item].append(key)
        else:
            invert_d[item] = [key]
print("\nWithdraw inverted dict: ", invert_d)