print('x y z F')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print(x, y, z, (not(x == (y <= z))) * 1)
