import os

input_file = os.path.dirname(__file__) + '/../inputs/input_arnaud.txt'
file = open(input_file, 'r')

count = 0
formatted_lines = ['']
ok = 0

for line in file:
    if len(line) > 1:
        formatted_lines[count] += line
    else:
        count += 1
        formatted_lines.append('')

for formatted_line in formatted_lines:
    splitted_line = formatted_line.split()

    field = []
    for field_value in splitted_line:
        field.append(field_value.split(':')[0])
    check = True

    if 'byr' not in field:
        check = False
    if 'iyr' not in field:
        check = False
    if 'eyr' not in field:
        check = False
    if 'hgt' not in field:
        check = False
    if 'hcl' not in field:
        check = False
    if 'ecl' not in field:
        check = False
    if 'pid' not in field:
        check = False

    if check:
        ok += 1

print(ok)
