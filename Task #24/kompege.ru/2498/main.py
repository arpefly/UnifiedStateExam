with open('24.txt') as input_file:
    s = input_file.read()

count = 0
for i in range(len(s)-2):
    if s[i]+s[i+1]+s[i+2] == 'XIX':
        count += 1
print(count)
