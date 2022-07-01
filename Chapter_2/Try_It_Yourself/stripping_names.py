
message = "Hello my name is \t"
name = "\t Michael Wizkit \n"
learn = " and i am learning python \n"

# here ill print my variables and with a tab and new rule
print(message, name, learn)

# here ill use .lstrip to remove the whitespace to the left
print(message.lstrip(), name.lstrip(), learn.lstrip())

# here ill use .rstrip to remove the whitespace from the right side
print(message.rstrip(), name, learn)

# here ill use .strip to remove all whitespace
print(message.strip(), name.strip(), learn.strip())