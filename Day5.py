""""
Random Password Generator
"""
import random
import string

# if you would like only the lower use print(string.ascii_lowercase) and print(string.ascii_uppercase)
en_alphabet = list(string.ascii_letters)  # Both lower and upper case letters.
numbers = [str(i) for i in range(10)]
signs = ['!', '@', '#', '$', '%', '^', '&', '~', '-', '_', '=', '+', '?', '/']

print("How many letters would you like in your random password?")
num_letters = int(input(">"))
print("How many numbers would you like in your random password?")
num_numbers = int(input(">"))
print("How many signs would you like in your random password?")
num_signs = int(input(">"))

letter = [random.choice(en_alphabet) for _ in range(num_letters) if num_letters > 0]
number = [random.choice(numbers) for _ in range(num_numbers) if num_numbers > 0]
sign = [random.choice(signs) for _ in range(num_signs) if num_signs > 0]

rand_password = letter + number + sign
random.shuffle(rand_password)

rand_password = "".join(rand_password).strip()
print(f"Your random password is: {rand_password}")
