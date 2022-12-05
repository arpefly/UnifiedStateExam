print('a b c F')

for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            if ((a and not c) or (not b and not c)) * 1 == 1:
                print(a, b, c, ((a and not c) or (not b and not c)) * 1)
