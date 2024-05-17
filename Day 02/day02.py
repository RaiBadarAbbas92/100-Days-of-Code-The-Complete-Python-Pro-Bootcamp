# Day 2 of 100 days of code in python
#lenght
len(input("What is your name?"))
print(len(input("What is your name?")))

# Data Types
# String
print("Hello"[0])
print("Hello"[4])
print("123" + "345")
# Integer
print(123 + 345)
# Float
print(3.14159)
# Boolean
True
False
# Type Error, Type Checking and Type Conversion\
num_char = len(input("What is your name?"))
print(type(num_char))
# Type Conversion
new_num_char = str(num_char)
print("Your name has " + new_num_char)
# Mathematical Operations
3 + 5
7 - 4
3 * 2
6 / 3
2 ** 3
# PEMDASLR
# ()
# **
# * /
# + -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)
# Number Manipulation and F Strings
print(round(8 / 3))
print(round(8 / 3, 2))
print(8 // 3)
result = 4 / 2
result /= 2
print(result)
score = 0
score += 1
print(score)
# F Strings
score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")
# Life in Weeks Exersice
age = input("What is your current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)
# Tip Calculator Exersice
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")

      
