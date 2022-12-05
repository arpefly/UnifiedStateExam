print('x y z w F')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0,1:
                if ((x and not y) or (x == z) or w) * 1 == 0:
                    print(x, y, z, w, ((x and not y) or (x == z) or w) * 1)
