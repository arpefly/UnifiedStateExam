print('x y z w F')

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0,1:
                if (((not y) and x) and (not z or w)) * 1 == 1:
                    print(x, y, z, w, (((not y) and x) and (not z or w)) * 1)
