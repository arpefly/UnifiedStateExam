with open('k7-0.txt') as file:
    s = file.read()

s = s.replace('A', ' ').replace('B', ' ')
s = ''.join(s).strip().split(' ')

print(len(max(s)))
