with open('24.txt') as input_file:
    s = input_file.read()

s = s.replace('D', ' ')

max_len = 0
for line in s.split():
    max_len = max(max_len, len(line))
print(max_len)
