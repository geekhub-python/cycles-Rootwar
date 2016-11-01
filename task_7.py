#!/usr/bin/env python3

first_length_track = 10
total_length = 0
all_length = 0

print('a)')
for i in range(10, 19):
    coefficient = i * 0.1
    new_length = i + coefficient
    all_length += new_length

    if i < 16:
        total_length += new_length

    print('New length track in day %s -' % (2 + i - first_length_track), new_length,'km')


print('\nb)')
print('Total length track to 7 days: ', first_length_track + total_length,'km')

print('\nc)')
print('This is 64 day')

print('\nd)')
print('Total length track to n days: ', first_length_track + all_length,'km')

