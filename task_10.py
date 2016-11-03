#!/usr/bin/env python3

import random

quantity_letter = random.randrange(2, 17)
password = []

#number for password
for i in range(5):
  number = int(random.random() * 10)
  password.append(str(number))

#letter for password
for j in range(quantity_letter):
    if j % random.randrange(2, 5):
        letter = chr(random.randrange(ord('a'), ord('z')))
    else:
        letter = chr(random.randrange(ord('a'), ord('z'))).upper()
    password.append(letter)

password.append('_')
password = sorted(password, key=lambda *args: random.random())

#deleted double symbols
for k in range(len(password)):
    if k + 1 < len(password) and password[k] == password[k + 1]:
        del password[k]

print(''.join(password))
