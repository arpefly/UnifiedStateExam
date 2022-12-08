with open('24.txt') as input_file:
    s = input_file.read()

conut = 0
for i in range(len(s)-3):
    if s[i]+s[i+1]+s[i+2]+s[i+3] == 'XXXX':
        conut += 1
print(conut)
