import re

with open('24.txt') as input_file:
    data = input_file.read()

print(len(max(re.findall(r'C+', data))))
