#!/usr/bin/env python3

for i in range(11, 100000, 11):
    for j in range(2, 11):
        if i % j != 1:
            break

        if j == 9:
            print(i)

