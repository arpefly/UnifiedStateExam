import string

file = list(open('24-1.txt').read())

for i in range(len(file)):
    if file[i] in string.ascii_uppercase:
        file[i] = ' '
print(''.join(file).split())
max_num = 0
for i in ''.join(file).split():
    if int(i) % 2 != 0 and int(i) > max_num:
        max_num = int(i)

print(max_num)
