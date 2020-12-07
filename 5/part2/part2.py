import os

input_file = os.path.dirname(__file__) + '/../inputs/input_romain.txt'
file = open(input_file, 'r')


def get_row_from_sequence(sequence):
    binary_row = ''
    for letter in sequence:
        if letter == 'B':
            binary_row += '1'
        else:
            binary_row += '0'
    return int(binary_row, 2)


def get_column_from_sequence(sequence):
    binary_row = ''
    for letter in sequence:
        if letter == 'R':
            binary_row += '1'
        else:
            binary_row += '0'
    return int(binary_row, 2)


def get_seat_id_from_sequence(sequence):
    row = get_row_from_sequence(sequence[:7])
    column = get_column_from_sequence(sequence[7:10])
    return row * 8 + column

elems = []
for line in file:
    elems.append(get_seat_id_from_sequence(line))

elems.sort()

founded = False

cursor = min(elems)
while not founded:
    if cursor not in elems:
        founded = True
        print(cursor)
    cursor += 1

print(elems)

