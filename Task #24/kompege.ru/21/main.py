with open('24.txt') as input_file:
    s = input_file.read()

cur_len = 1
max_len = 0
for i in range(1, len(s)):
    if s[i-1] != s[i]:
        cur_len += 1
        max_len = max(cur_len, max_len)
    else:
        cur_len = 1
print(max_len)
