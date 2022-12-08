with open('24.txt') as input_file:
    s = input_file.read()

count = 0
for i in range(len(s)-4):
    tmp = s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]
    if tmp == tmp[::-1]:
        count += 1
print(count)
