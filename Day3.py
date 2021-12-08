""""
Learning better flow control
"""

year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 != 0 and year % 4 == 0:
        print("Leap year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")

# ===================================================================================================
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

# Better way to do this is................
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

# ======================================================================================

# The love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").upper()
name2 = input("What is their name? \n").upper()

combined_names = name1 + name2

t = list(combined_names).count('T')
r = list(combined_names).count('R')
u = list(combined_names).count('U')
e = list(combined_names).count('E')
first_digit = t + r + u + e

l = list(combined_names).count('L')
o = list(combined_names).count('O')
v = list(combined_names).count('V')
e = list(combined_names).count('E')
second_digit = l + o + v + e

true_love = int(str(first_digit) + str(second_digit))

if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentors.")
elif 40 <= true_love <= 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")

# Treasure Island ====================================

print("""Welcome to Treasure Island.
Your mission is to find the treasure. Good Luck!""")

while True:
    print("You're at a cross road. Where do you want to go?", 'Type "left" or "right"')
    choice = input().lower().strip()
    if choice == "right":
        print('You get robbed and killed. Game Over.')
        break

    print("You come to a lake. There is an island in the middle of the lake.",
          'Type "wait" to wait for a boat. Type "swim" to swim across.')
    choice = input().lower().strip()
    if choice == "swim":
        print('You get eaten by a shark. Game Over.')
        break

    print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue.",
          'Which color do you choose?')
    choice = input().lower().strip()
    if choice == "red" or "blue":
        print('You enter a room full of beasts. Game Over.')
        break
    print("Hurray! You found the treasure.")
