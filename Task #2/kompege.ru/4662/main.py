print('x y z w F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (w <= ((x <= z) <= y)) * 1 == 0:
                    print(x, y, z, w, (w <= ((x <= z) <= y)) * 1)
