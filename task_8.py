#!/usr/bin/env python3

for i in range(1000, 10000):
    if str(i).find('5') >= 0:
        continue
    elif str(i).find('6') >= 0:
        continue
    print(i)