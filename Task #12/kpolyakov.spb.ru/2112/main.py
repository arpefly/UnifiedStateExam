answer = 0
for n in range(101):
    s  = '1'*n

    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '3', 1)
        s = s.replace('333', '1', 1)

    if s == '321':
        answer += 1

print(answer)
