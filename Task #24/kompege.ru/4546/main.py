with open('24.txt') as input_file:
    s = input_file.read()

max_len = 0
for i in range(3):
    cur_len = 0
    for j in range(i, len(s)-2, 3):
        if s[j]+s[j+2] == 'AA' or s[j]+s[j+2] == 'CC':
            cur_len += 1
            max_len = max(cur_len, max_len)
        else:
            cur_len = 0
print(max_len)
