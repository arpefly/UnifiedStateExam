with open('24.txt') as input_file:
    s = input_file.read()

cur_len = max_len = 1
for i in range(len(s)-1):
    if s[i]<=s[i+1]:
        cur_len += 1
        max_len = max(cur_len, max_len)
    else:
        cur_len = 1
print(max_len)
