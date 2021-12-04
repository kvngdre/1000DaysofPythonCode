""""
type casting.
"""
num = 395
print(num % 10)

#  Say you only live till 90, how long do you have left.

age = input("Enter your current age: ")

years_left = 90 - int(age)
days = years_left * 365
days = "{:,}".format(days)
weeks = years_left * 52
months = years_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")

"""
A tip calculator.
"""
total_bill = input("What is your total bill? ")
percentage = input("What percentage tip would you like to give? 10, 12, 15, 20? ")
num_of_split = input("How many people are splitting the bill? ")

if total_bill[0].isdecimal():
    total_bill = float(total_bill)
else:
    total_bill = float(total_bill[1:])

per_person = total_bill / int(num_of_split)
tip = round(per_person * float(int(percentage)/100 + 1), 2)

print(f"Each person is to pay: ${tip}")
