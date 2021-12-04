""""
Adding two digit number input.
if user enters 39, the program does 3 + 9 = 12
"""
num = int(input('Enter a two digit number you would like to add?'))
a = num // 10  # To get the whole number i.e 3 in 3.9
b = num % 10  # TO get the reminder i.e. 9 in 3.9
result = a + b
print(result)
