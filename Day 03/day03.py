# Day 3 of 100 days of code in python
# Control flow and if else condition
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm"))
if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")

# Comparison Operators
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to
# Modulo Operation
7 % 2
2 + 2 + 2 + 1
7 % 3
3 + 3 + 1
7 % 4
4 + 2 + 2 + 1
7 % 5
5 + 2 + 2 + 1
7 % 6
6 + 1
7 % 7
7
# Nested if/else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm"))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")

else:
  print("Sorry, you have to grow taller before you can ride.")

# if/elif/else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm"))
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")

else:
  print("Sorry, you have to grow taller before you can ride.")

# BMI 2.0 Exersice
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")

elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")

elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")

elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")

else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# Leap Year Exersice
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# Multiple if Statements in Succession
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm"))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  else:
    bill = 12
    print("Adult tickets are $12.")

  wants_photo = input("Do you want a photo taken? Y or N.")
  if wants_photo == "Y":
    bill += 3

  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")


