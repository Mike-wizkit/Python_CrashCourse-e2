invited = ['Albert Einstein', 'Nicola tesla', 'Johannes Gutenberg']

name = invited[0]
print(f"{name}, please come to my dinner.")

name = invited[1]
print(f"{name}, please come to my dinner.")

name = invited[2]
print(f"{name}, please come to my dinner.")

name = invited[1]
print(f"\nSorry, {name} can't make it to dinner.")

# time to change
del(invited[1])
invited.insert(1, 'gary snyder')

# print new list
name = invited[0]
print(f"\n{name}, please come to my dinner.")

name = invited[1]
print(f"{name}, please come to my dinner.")

name = invited[2]
print(f"{name}, please come to my dinner.")