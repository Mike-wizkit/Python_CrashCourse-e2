# all brand-names are in a list and ill ask to print the whole list
# including the brackets
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

# here ill ask for the first item out of the list
print(bicycles[0])

# here ill ask for the first item out of the list with title marks
print(bicycles[0].title())

# here ill use a special syntax to show the last item of the list
# -2 -3 and so on works the same
print(bicycles[-1])

# here ill use an f-string to create a message based on the variables in
# the list

message = f"My first bicycle was a {bicycles[0].title()}."
print(message)