from itertools import product

print('x y z w F')

for x, y, z, w in product(range(2), repeat=4):
    if ((x == (not z)) <= ((x or w) == y)) * 1 == 0:
        print(x, y, z, w, ((x == (not z)) <= ((x or w) == y)) * 1)
