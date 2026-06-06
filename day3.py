first_name = "haein"
last_name = "kim"
full_name = first_name + " " + last_name

# print(full_name + str(10))

hello = 13
hi = "17"

print(hello + int(hi)) # 30
print(str(hello) + hi) # 1317


# string format
print("{} is {} years old!".format("John", 24))

output = "{name} is {age} years old, and {name} works as a {job}."
print(output.format(name="John", age=24, job="developer"))

# f-string
name = "John"
age = 24

print(f"{name} is {age} years old!")
print(f"{name} is {age * 12} months old!")

# string processing
"Hello, World!".lower()       # "hello, world!"
"Hello, World!".upper()       # "HELLO, WORLD!"
"Hello, World!".capitalize()  # "Hello, world!"
"hello, world!".title()       # "Hello, World!"
"  Hello, World!  ".strip()   # "Hello, World!"

print("haein is cute".capitalize())

######################## Exercises ########################

# exercise 1:
# Using the variable below, print "Hello, world!".
# greeting = "Hello, world"

# You can add the missing exclamation mark using string concatenation, format, or f-strings. The choice is yours.

greeting = "Hello, world"
print(greeting + "!")
print(f"{greeting}!")

# exercise 2:
# Ask the user for their name, and then greet the user, using their name as part of the greeting. The name should be in title case, and shouldn't be surrounded by any excess white space.
# For example, if the user enters "lewis ", your output should be something like this:

# Hello, Lewis!

name = input("Enter your name: ")
name = name.strip().capitalize()
print(f"Hello, {name}!")

# exercise 3
# Concatenate the string "I am " and the integer 29 to produce a string which reads "I am 29".
# Remember that we can only concatenate strings to other strings, 
# so you will have to convert the integer to a string before you can perform the concatenation.

my_age = "I am " + "29"
my_age_2 = f"I am {29}"
print(my_age)
print(my_age_2)


# exercise 4
# Format and print the information below using string interpolation:
# title = "Joker"
# director = "Todd Phillips"
# release_year = 2019

# The output should look like this:

# Joker (2019), directed by Todd Phillips

title = "Joker"
director = "Todd Phillips"
release_year = 2019

print(f"{title} ({release_year}), directed by {director}")
