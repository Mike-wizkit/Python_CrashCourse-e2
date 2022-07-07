countries = ["Australia", "Peru", "Indonesia", "Brazil", "Japan"]

print("Original order:")
print(countries)

print("\nAlpabethical order:")
print(sorted(countries))

print("Original order:")
print(countries)

print("\nReverse alphabetical:")
print(sorted(countries, reverse=True))

print("Original order:")
print(countries)

print("\nReversed:")
countries.reverse()
print(countries)

print("Original order:")
countries.reverse()
print(countries)

print("\nAlphabethical:")
countries.sort()
print(countries)

print("\n Reverse alpabethical")
countries.sort(reverse=True)
print(countries)
