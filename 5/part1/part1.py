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


get_seat_id_from_sequence("BBFFBFFRRL ")

highestSeat = 0
for line in file:
    highestSeat = max(highestSeat, get_seat_id_from_sequence(line))
print("result = " + str(highestSeat))
