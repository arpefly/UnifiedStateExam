print('x y z w F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x == y) and (z and not w)) == (not (((y <= w) and (z == y)) or y))) * 1 == 0:
                    print(x, y, z, w, (((x == y) and (z and not w)) == (not (((y <= w) and (z == y)) or y))) * 1)
