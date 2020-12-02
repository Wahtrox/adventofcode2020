import os
import re

input_file = os.path.dirname(__file__) + '/../inputs/input_romain.txt'
file = open(input_file, 'r')

numbers = []

count = 0
for line in file:
    match = re.match(r'(.*)-(.*)\s(.*):\s(.*)', line)
    first_position = int(match.group(1))
    second_position = int(match.group(2))
    letter = match.group(3)
    code = match.group(4)
    if bool(code[first_position - 1] is letter) ^ bool(code[second_position - 1] is letter):
        count += 1

print(str(count) + ' passwords are correct')