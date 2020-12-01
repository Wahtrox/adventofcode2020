import os
from datetime import datetime

input_file = os.path.dirname(__file__) + '/../inputs/input_arnaud.txt'
file = open(input_file, 'r')

numbers = []
for line in file:
    numbers.append(int(line))

start_time = datetime.now()

pointer = 0
expected_numbers = []
founded = False

while founded is not True:
    diff = 2020 - numbers[pointer]
    if numbers[pointer] in expected_numbers:
        founded = True
        print(numbers[pointer] * diff)
    else:
        expected_numbers.append(diff)
        pointer += 1

end_time = datetime.now()
total_time = end_time - start_time
print('Executed in ', total_time.microseconds, ' microseconds')
