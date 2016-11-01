#!/usr/bin/env python3

for i in range(ord('a'), ord('z')+1):
    print(chr(i), end=' ')

    if (i-1) % 5 == 0:
        print()

print()