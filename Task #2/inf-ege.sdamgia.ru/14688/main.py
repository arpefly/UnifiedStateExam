print('x y z F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not(x or y) or (z == x)) * 1 == 0:
                print(x, y, z, (not(x or y) or (z == x)) * 1)
