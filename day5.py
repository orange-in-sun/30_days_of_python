print(5 < 10) #True
print(bool(0)) #False
print(10 <= 20) #True
print(0 == "0") #False
a = [1,2,3,4]
b = [1,2,3,4]
print(a == b) #True
print(a is b) #False
print(id(a))
print(id(b))
a = b
print(a is b)

age = int(input("How old are you?"))
if age < 18:
    print("Sorry, we cannot serve you")


#Exercises

#1) Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.
a = [1,2,3,4]
b = [1,2,3,4]
print(id(a) == id(b)) #False

#2) Try to use the is operator or the id function to investigate the difference between this:

numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]

print(numbers is new_numbers) #False

# And this:

numbers = [1, 2, 3, 4]
numbers.append(5)

print(numbers is new_numbers) #False

# Are new_numbers and numbers the same thing? What about numbers before and after we append 5?

# 3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
age = int(input("Enter your age: "))
if age == 0:
    print("Enter again")
elif age >= 19:
    print("Good good")
else:
    print("Get out")


# 4) Write a program to determine whether an employee is owed any overtime. 
# You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.

# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, 
# as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. 
# In effect, the employees get paid 110% of their hourly wage for any overtime.

hourly_wage = float(input("Enter your hourly wage: "))
work_time = float(input("How many hours did you work this week?: "))
over_time = float(work_time - 40)

if work_time <= 40:
    print(f"Your wage is {work_time*hourly_wage} won ")
else:
    print(f"Your overtime is {over_time} hours and your wage is {hourly_wage*(40 + over_time*1.1)} won")