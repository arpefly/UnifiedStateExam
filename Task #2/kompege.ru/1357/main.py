from itertools import product

print('a b c d F')

for a, b, c, d in product(range(2), repeat=4):
    if (((a and b) == (not c)) and (b <= d)) * 1 == 1:
        print(a, b, c, d, (((a and b) == (not c)) and (b <= d)) * 1)
