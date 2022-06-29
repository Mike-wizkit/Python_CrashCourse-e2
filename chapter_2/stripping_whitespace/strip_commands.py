# rule 1 contains extra whitespace at the end of the string
# .rstrip is used for removing whitespace (but only temporarily)
favorite_language = 'python '
favorite_language = favorite_language.rstrip()
print(favorite_language)

# removes white space on the leftside
favorite_language = ' python'
favorite_language = favorite_language.lstrip()
print(favorite_language)

# this removes whitespace allround
favorite_language = ' python '
favorite_language = favorite_language.strip()
print(favorite_language)