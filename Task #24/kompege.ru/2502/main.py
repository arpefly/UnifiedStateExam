import re

with open('24.txt') as input_file:
    count = 0
    for s in input_file.readlines():
        if len(re.findall(r'K.GE', s)) > 0:
            count += 1
    print(count)
