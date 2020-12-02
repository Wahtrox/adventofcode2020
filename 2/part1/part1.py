import os
import re

input_file = os.path.dirname(__file__) + '/../inputs/input_romain.txt'
file = open(input_file, 'r')

numbers = []

count = 0
for line in file:
    match = re.match(r'(.*)-(.*)\s(.*):\s(.*)', line)
    min_occurrence = int(match.group(1))
    max_occurrence = int(match.group(2))
    letter = match.group(3)
    code = match.group(4)
    number_of_occurrence = code.count(letter)
    if min_occurrence <= number_of_occurrence <= max_occurrence:
        count += 1

print(str(count) + ' passwords are correct')