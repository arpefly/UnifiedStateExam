print('x y z w F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= y) and (y <= w)) or (z == (x or y))) * 1 == 0:
                    print(x, y, z, w, (((not x or y) and (not y or w)) or (z == (x or y))) * 1)
