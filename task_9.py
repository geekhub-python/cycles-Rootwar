#!/usr/bin/env python3

letter = input('Enter letter: ').lower()

for i in range(ord(letter)+1, ord(letter)+4):
    if i > ord('z'):
        print(chr(i-26), end=' ')
    else:
        print(chr(i), end=' ')

print()