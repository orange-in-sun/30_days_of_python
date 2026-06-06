import math

haein1 = 3.14
haein2 = 3
haein3 = "cute"
haein4 = (4 - 5) * (5 + 4) / 2

# exercise 1
# Print your age to the console.
print(25)

# exercise 2
# Calculate and print the number of days, weeks, and months in 27 years. Don’t worry about leap years!
def get_days_weeks_months(years):
    days = 365 * years
    weeks = 52 * years
    months = 12 * years
    return days, weeks, months

print('days:', get_days_weeks_months(27)[0])
print('weeks:', get_days_weeks_months(27)[1])
print("months:", get_days_weeks_months(27)[2])

# exercise 3
# Calculate and print the area of a circle with a radius of 5 units. You can be as accurate as you like with the value of pi.
def get_area_of_circle(radius):
    return math.pi * radius**2

print(get_area_of_circle(5))

