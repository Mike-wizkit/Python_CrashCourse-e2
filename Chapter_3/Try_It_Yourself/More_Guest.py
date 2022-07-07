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

# bigger table so lets add more people
print("\nWe got a bigger table!")
invited.insert(0, 'jhon doe')
invited.insert(2, 'jane doe')
invited.append('keaira ugly')

name = invited[0].title()
print(f"{name}, please come to my dinner.")

name = invited[1].title()
print(f"{name}, please come to my dinner.")

name = invited[2].title()
print(f"{name}, please come to my dinner.")

name = invited[3].title()
print(f"{name}, please come to my dinner.")

name = invited[4].title()
print(f"{name}, please come to my dinner.")

name = invited[5].title()
print(f"{name}, please come to my dinner.")

# shijt the table cant come on time
print("\nSorry, we can only invite two people to dinner.")

name = invited.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = invited.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = invited.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# there should be two people left. let's invite them.
name = invited[0].title()
print(f"{name}, please come to my dinner.")

name = invited[1].title()
print(f"{name}, please come to my dinner.")

# empty the list
del(invited[0])
del(invited[1])

# check remove
print(invited)
