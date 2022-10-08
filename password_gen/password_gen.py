#!/usr/bin/python3
print("NB: This generator creates a mixed character password")
pass_length = int(input("Password length: "))
from random import sample
list0 = [str(numbers) for numbers in range(10)]
list1 = [chr(letters) for letters in range(97, 123)]
list2 = [chr(letters) for letters in range(65, 91)]
list3 = ['!', '@', '#', '$', '%', '&', '*', '(', ')', '[', ']', '<', '>', '?', '|', '\\', '{', '}', '^']

conjuction = list0 + list1 + list2 + list3
pass_list = sample(conjuction, pass_length)
password = "".join(pass_list)
print(password)
