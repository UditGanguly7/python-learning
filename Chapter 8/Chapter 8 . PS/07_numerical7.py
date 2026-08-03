# Write a python to remove a given word from a list ad strip it at the same time.
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))

l = ["Harry", "Rohan", "Shubham", "an"]

print(rem(l, "an"))    # Test