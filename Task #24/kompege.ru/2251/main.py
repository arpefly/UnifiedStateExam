with open('24.txt') as input_file:
    s = input_file.read()

s = s.split('D')
max_len = 1
for i in range(len(s) - 2):
    sub = s[i] + 'D' + s[i+1] + 'D' + s[i+2]
    max_len = max(len(sub), max_len)
print(max_len)
