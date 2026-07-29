# numbers = [1, 2, 3, 4, 5]

# stringified_numbers = []

# for number in numbers:
#     stringified_numbers.append(str(number))

# print(', '.join(stringified_numbers)) # 1, 2, 3, 4, 5

# sample_string = "Python"

# print(list(sample_string)) # ['P', 'y', 't', 'h', 'o', 'n']
# print(tuple(sample_string)) # ('P', 'y', 't', 'h', 'o', 'n')


# Exercises

# 1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names, 
# and then assign each name to a different variable. 
# For this exercise, you can assume that the user has a single given name and a single surname.

name = input("Type your full name: ").split()
surname = name[1]
given_name = name[0]

# 2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. 
# Remember that you can only join collections of strings, so you’re going to need to do some initial processing 
# of the list of numbers.

numbers_list = [ 1, 2, 3, 4, 5 ]
print(f"{'|'.join(map(str, numbers_list))}")
print(f"{' | '.join([str(i) for i in numbers_list])}")

# 3) Below you’ll find a short list of quotes:

quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
 ]

for quote in quotes:
    print(quote[1:-1])
# Each quote is a string, but each string actually contains quote characters at the start and end. 
# Using slicing, extract the text from each string, without these extra quote marks, and print each quote.

# You may also want to try a solution using strip.

# 4) Ask the user to enter a word, and then print out the length of the word. 
# You should account for any excess whitespace in the user’s input, so you’re going to have to process 
# the string before you find its length.

word = (input("Enter a word: "))
print(len(word.strip()))

# If you want to take this a little bit further, you an ask the user for a long piece of text. 
# You can then tell them how many characters are in the text overall, and you can also provide them a word count.

text = input("Enter text: ").strip()
print(f"There are {len(text)} characters and {len(text.split())} words.")

#day7_project


movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

#-------------------my answer----------------------

number = int(input("How many movie you want to add: "))

for i in range(number):
    print(f"\n({i+1})")
    title = input("Enter movie name: ").strip()
    budget = int(input("Enter movie budget: "))
    movies.append((title, budget))

average = 0
for a in movies:
    average = average + a[1] / len(movies)+number

expensive_movie = []
for b in movies:
    if b[1] > average:
        print(f"{b[0]}, {b[1]-average}")
        expensive_movie.append(b[0])
print(len(expensive_movie))