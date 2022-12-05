from itertools import product

print('x y z w F')

for x, y, z, w in product(range(2), repeat=4):
    if (((z <= x) and (x <= w)) or (y == (z or x))) * 1 == 0:
        print(x, y, z, w, (((z <= x) and (x <= w)) or (y == (z or x))) * 1)
