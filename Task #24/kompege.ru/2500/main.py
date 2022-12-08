with open('24.txt') as input_file:
    s = input_file.read()

count = 0
for i in range(len(s)-3):
    if s[i]+s[i+2]+s[i+3] == 'GME':
        count += 1
print(count)
