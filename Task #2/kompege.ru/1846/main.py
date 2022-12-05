from itertools import product

print('a b c d F')

for a, b, c, d in product(range(2), repeat=4):
    if ((not a) and (not b) or (b == c) or d) * 1 == 0:
        print(a, b, c, d, ((not a) and (not b) or (b == c) or d) * 1)
