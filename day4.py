names = ["Haein", "Kichul", "Diego", "Tommy"]
print(names[2:])
names.append("Yubin")
print(names)
print(names + ["Yoseb"])
names.insert(1, "Sein")
names.pop(1)
print(names)
last_in_line = names.pop()
print(last_in_line)
names.clear()
movies = [
    ( "Lala Land" , 2018),
    ( "Interstella" , 2015),
    ( "Mamma Mia" , 2010)
]
print(movies[0][0])



# Exercise 1
# Create a movies list containing a single tuple. 
# The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
movies = [ 
    ("Lala Land", 2034, "Kichul", 300)
    ]

# Exercise 2
# Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
movie_title = input("Enter the title of the movie: ")
movie_release_year = int(input("Enter the release year of the movie: "))
movie_director = input("Enter the director of the movie: ")
movie_budget = int(input("Enter the budget of the movie: "))

# Exercise 3
# Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
new_movie = (movie_title, movie_release_year, movie_director, movie_budget)

# Exercise 4
#  Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"{movie_title}, {movie_release_year}")

# Exercise 5
# Add the new movie tuple to the movies collection using append.
movies.append(new_movie)

# Exercise 6
# Print both movies in the movies collection.
print(movies[0])
print(movies[1])

# Exercise 7
# Remove the first movie from movies. Use any method you like.
del movies[0]
print(movies)