import re

with open('24.txt') as input_file:
    s = input_file.readline()

print(len(min(re.findall(r'D+', s))))
