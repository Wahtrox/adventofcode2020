import os
import re

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
    check = True
    field = []
    for field_value in splitted_line:
        key_value = field_value.split(':')
        field.append(key_value[0])
        if 'byr' == key_value[0]:
            if not (1920 <= int(key_value[1]) <= 2002):
                check = False
        if 'iyr' == key_value[0]:
            if not (2010 <= int(key_value[1]) <= 2020):
                check = False
        if 'eyr' == key_value[0]:
            if not (2020 <= int(key_value[1]) <= 2030):
                check = False
        if 'hgt' == key_value[0]:
            match = re.match(r'([0-9]+)(cm|in)', key_value[1])
            if match is None:
                check = False
            else:
                if not (match.group(2) == 'cm'
                        and 150 <= int(match.group(1)) <= 193
                        or match.group(2) == 'in'
                        and 59 <= int(match.group(1)) <= 76):
                    check = False
        if 'hcl' == key_value[0]:
            match = re.match(r'^#[0-9a-f]{6}$', key_value[1])
            if match is None:
                check = False
        if 'ecl' == key_value[0]:
            if key_value[1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                check = False
        if 'pid' == key_value[0]:
            match = re.match(r'^[0-9]{9}$', key_value[1])
            if match is None:
                check = False

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
