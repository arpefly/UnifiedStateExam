with open('24.txt') as input_file:
    s = input_file.read()

cur_sub = max_sub = s[0]
for i in range(1, len(s)):
    if s[i-1] > s[i]:
        cur_sub += s[i]
        max_sub = max(cur_sub, max_sub, key=len)
    else:
        cur_sub = s[i]
print(max_sub)
