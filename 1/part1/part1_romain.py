import os
from datetime import datetime

input_file = os.path.dirname(__file__) + '/../inputs/input_romain.txt'
file = open(input_file, 'r')

numbers = []
for line in file:
    numbers.append(int(line))

start_time = datetime.now()

numbers.sort()

smallPos = 0
bigPos = len(numbers) - 1

number_found = False

while number_found is not True:
    number_sum = numbers[smallPos] + numbers[bigPos]
    if number_sum == 2020:
        print(numbers[smallPos] * numbers[bigPos])
        number_found = True
    elif number_sum > 2020:
        bigPos -= 1
    else:
        smallPos += 1

end_time = datetime.now()
total_time = end_time - start_time
print('Executed in ', total_time.microseconds, ' microseconds')
