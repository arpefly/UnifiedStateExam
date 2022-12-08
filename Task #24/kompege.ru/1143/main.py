with open('24.txt') as input_file:
    s = input_file.read()

count = 0
for i in range(len(s)-6):
    if s[i] + s[i+6] == 'AF':
        count += 1
for i in range(len(s)-7):
    if s[i] + s[i+7] == 'AF':
        count += 1
for i in range(len(s)-8):
    if s[i] + s[i+8] == 'AF':
        count += 1
for i in range(len(s)-9):
    if s[i] + s[i+9] == 'AF':
        count += 1
print(count)