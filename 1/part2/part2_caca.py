import os
from datetime import datetime

input_file = os.path.dirname(__file__) + '/../inputs/input_arnaud.txt'
file = open(input_file, 'r')

numbers = []
for line in file:
    numbers.append(int(line))

start_time = datetime.now()

for first in numbers:
    for second in numbers:
        for third in numbers:
            if first + second + third == 2020:
                print(first, ', ', second, ', ', third)
                print(first * second * third)

end_time = datetime.now()
total_time = end_time - start_time
print('Executed in ', total_time.microseconds, ' microseconds')
