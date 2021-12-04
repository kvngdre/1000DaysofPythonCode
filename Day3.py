""""
Flow control
"""

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0 and year % 4 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")


print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


total_bill = 0
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total_bill = 15 + 2 + 1
        else:
            total_bill = 15 + 2
    else:
        if extra_cheese == "Y":
            total_bill = 15 + 1
        else:
            total_bill = 15
elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            total_bill = 20 + 3 + 1
        else:
            total_bill = 20 + 3
    else:
        if extra_cheese == "Y":
            total_bill = 20 + 1
        else:
            total_bill = 20
else:
    if size == "L":
        if add_pepperoni == "Y":
            if extra_cheese == "Y":
                total_bill = 25 + 3 + 1
            else:
                total_bill = 25 + 3
        else:
            if extra_cheese == "Y":
                total_bill = 25 + 1
            else:
                total_bill = 25
    else:
        print("Invalid input.")

print(f"Your final bill is: ${total_bill}.")

# Better way to do this is...
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")
