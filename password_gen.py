# passwords can use ascii characters #33 through #126
# but here I will be using the string library

import random
import string
import pyperclip

# used this to find valid indices are 0 to 93
# for i, c in enumerate(string.printable):
#     print(i, c)

password_length = 20
password = ""
for i in range(password_length):
    random_value = random.random()  # decimal value between 0 and 1
    index = int(random_value * 93)
    password += string.printable[index]

pyperclip.copy(password)
print("New password copied to clipboard")
