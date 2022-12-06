import re

with open('24.txt') as input_file:
    s = input_file.read()

max_len = 0
for line in re.sub(r'[a-z]+', ' ', s).split():
    max_len = max(max_len, len(line))
print(max_len)
