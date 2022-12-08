with open('24.txt') as input_file:
    s = input_file.readline().strip()

d = {x:0 for x in sorted(set(s))}
for i in range(len(s)-4):
    if s[i]+s[i+1]+s[i+3]+s[i+4] == 'CBBC':
        d[s[i+2]] += 1

print([c for c in d if d[c] == max(d.values())], max(d.values()))
