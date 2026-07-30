# 1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 
# 1 and 100, and you should tell them whether their guess was too high or too low after each guess. 
# The loop should keeping running until the user guesses the number correctly.

while True:
    number = int(input("Enter number between 1 to 100: "))
    if number <= 20:
        print("Too low. Try again!")
    elif 20 < number < 58:
        print("Low. Try again!")
    elif 58 < number < 90:
        print("High. Try again!")
    elif number >= 90:
        print("Too high. Try again")
    elif number == 58:
        print("Correct!")
        break
    else:
        print("Invalid number")

# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".

for character in str("Python"):
    if character is "o":
        continue
    else:
        print(f"{character}")



# 3) Using one of the examples from earlier—or a solution entirely of your own—create a program 
# that prints out every prime number between 1 and 100.

for number in range(2, 101):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        print(number)