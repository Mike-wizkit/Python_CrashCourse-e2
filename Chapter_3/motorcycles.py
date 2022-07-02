# list to work with
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# to change a variable to another variable follow example below (works on all items in list)
motorcycles[0] = 'ducati'
print(motorcycles)

# to append (add) a variable to the list folow example below (append item method)
motorcycles.append('bmw')
print(motorcycles)

# to start a clean list follow the example below (empty append method)
motorcycles_empty = []

motorcycles_empty.append('honda')
motorcycles_empty.append('yamaha')
motorcycles_empty.append('suzuki')

print(motorcycles_empty)

# to insert items to a list follow the example below (insert method)
motorcycles_insert = ['honda', 'yamaha', 'suzuki']
motorcycles_insert.insert(0, 'ducati')
print(motorcycles_insert)

# to remove a known variable out of the list use example below (del method)
motors_del = ['honda', 'yamaha', 'suzuki']
del motors_del[0]
print(motors_del)

# to remove a variable and use them again later folow the example below (pop method)
motorcycles =['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# other example of the pop method
motorcycles = [ 'honda', 'yamaha', 'suzuki']
last_owned =motorcycles.pop()
print(f"The last motorcycle I owed was a {last_owned.title()}.")

# poping items from any position in a list
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

# removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# removing an item by value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

to_expensive = 'ducati'
motorcycles.remove(to_expensive)
print(motorcycles)
print(f"\nA {to_expensive.title()} is to expensive for me.")