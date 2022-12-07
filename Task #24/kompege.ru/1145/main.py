with open('24.txt') as input_file:
    s = input_file.read()

min_len = 10 ** 6 + 1
for sub in s.split('D')[1:-1]:
    if sub != '':
        min_len = min(min_len, len(sub) + 2)
print(min_len)
