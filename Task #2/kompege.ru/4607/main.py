print('x y z w F')

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= z) <= y) or (not w)) * 1 == 0:
                    print(x, y, z, w, (((x <= z) <= y) or (not w)) * 1)
