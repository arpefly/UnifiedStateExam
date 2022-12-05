print('x y z F')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            if ((not x and y and z) or (not x and not z)) * 1 == 1:
                print(x, y, z, ((not x and y and z) or (not x and not z)) * 1)
