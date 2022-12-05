print('x y z w F')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0,1:
                if ((y <= (x or z)) and (z <= y)) * 1 == 0:
                    print(x, y, z, w, ((y <= (x or z)) and (z <= y)) * 1)
