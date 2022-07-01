# To instert a variable's value into a string, you place the f
# immediately before the opening quotation mark (like with full_name)

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# The full name is used in a sentence that greets the user, and the
# .title() method changes te name to the title case
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# Here ill used the f-strings  to compose a message, and then assign
# the entire message to a variable
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)

# f-strings in python 3.5 and below format is different
# full_name = "{} {}" .format(first_name, last_name)