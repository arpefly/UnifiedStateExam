print('x y z F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((x == y) or (not(y or z) or x)) * 1 == 0:
                print(x, y, z, ((x == y) or (not(y or z) or x)) * 1)
