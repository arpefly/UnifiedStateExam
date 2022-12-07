with open('24.txt') as input_file:
    s = input_file.read()

s = s.split('A')
max_len = 0
for i in range(len(s) - 1):
    sub = s[i] + 'A' + s[i + 1]
    max_len = max(len(sub), max_len)
print(max_len)
