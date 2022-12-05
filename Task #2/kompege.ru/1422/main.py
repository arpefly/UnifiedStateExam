from itertools import product

print('x y z w F')

for x, y, z, w in product(range(2), repeat=4):
    if (not (z and not w) or ((z <= w) == (x <= y))) * 1 == 0:
        print(x, y, z, w, (not (z and not w) or ((z <= w) == (x <= y))) * 1)
