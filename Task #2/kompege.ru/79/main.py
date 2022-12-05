print('x y z w F')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((not w) and ((y or z) <= ((not x) and y))) * 1 == 1:
                    print(x, y, z, w, ((not w) and ((y or z) <= ((not x) and y))) * 1)
