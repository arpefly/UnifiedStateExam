with open('24.txt') as input_file:
    s = input_file.read().strip()

d = {x:s.count(x) for x in sorted(set(s))}

print(max(d.values()) - min(d.values()))
