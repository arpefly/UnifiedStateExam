import re

with open('24.txt') as input_file:
    s = input_file.read()

s = s.replace('KOT', '@')
print(len(max(re.findall(r'@+', s))))
