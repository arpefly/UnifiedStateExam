print('x y z F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            if ((x == z) or ((not x) or (y and z))) * 1 == 0:
                print(x, y, z, ((x == z) or ((not x) or (y and z))) * 1)
