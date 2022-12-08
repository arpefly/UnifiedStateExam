with open('24.txt') as input_file:
    lines = input_file.readlines()

line_with_max_q = ''
line_with_max_q_idx = 0
for s in open('24.txt').readlines():
    line_with_max_q_idx = max(s.count('Q'), line_with_max_q_idx)
line_with_max_q = lines[64].strip()

d = {x:0 for x in sorted(set(line_with_max_q))}
for c in line_with_max_q:
    d[c] += 1

most_common_letter = chr(ord([i for i in d if d[i] == min(d.values())][0]))

total = 0
for s in lines:
    for c in s:
        if c == most_common_letter:
            total += 1
print(most_common_letter, total)
