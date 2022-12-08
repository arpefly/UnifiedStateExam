with open('24.txt') as input_file:
    s = input_file.read()

count = 0
for i in range(len(s)-4):
    if s[i]+s[i+2]+s[i+4] == 'AAA':
        count += 1
print(count)
