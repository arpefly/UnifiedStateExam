with open('24.txt') as input_file:
    lines = [line.strip() for line in input_file.readlines()]

m = 0
ms = ''
q = ''

for line in lines:
    q += line
    cur_m = 0
    c = line[0]
    for i in range(len(line) - 1):
        if line[i] == line[i + 1]:
            c += line[i]
            cur_m = max(cur_m, len(c))
        else:
            c = line[i]
    if cur_m > m:
        m = cur_m
        ms = line

d = {x: ms.count(x) for x in sorted(set(ms))}
print([i for i in d if d[i] == max(d.values())], q.count([i for i in d if d[i] == max(d.values())][0]))
