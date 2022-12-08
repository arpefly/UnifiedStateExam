with open('24.txt') as input_file:
    s = input_file.readline().strip()

d = {x:0 for x in sorted(set(s))}

for i in range(len(s)-2):
    if s[i] == s[i+2]:
        d[s[i+1]] += 1

print([c for c in d if d[c] == max(d.values())], max(d.values()))
