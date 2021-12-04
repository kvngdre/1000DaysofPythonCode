""""
Starting at the basics
"""
num_ = input('Enter a two digit number you would like to add?')
num = int(num_)
a = num // 10  # To get the whole number i.e 3 in 3.9
b = num % 10  # TO get the reminder i.e. 9 in 3.9
result = a + b
print(result)

# OR
a_ = int(num_[0])
b_ = int(num_[1])
result_ = a_ + b_
print(result_)
