with open('24.txt') as input_file:
    s = input_file.read().strip()

d = {x:s.count(x) for x in sorted(set(s))}

print([c for c in d if d[c] == max(d.values())], max(d.values()))
