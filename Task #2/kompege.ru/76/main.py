print('x y z w F')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0,1:
                if (((not x and y) == z) and w) * 1 == 1:
                    print(x, y, z, w, (((not x and y) == z) and w) * 1)