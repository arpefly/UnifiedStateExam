print('H L W N F')

for H in range(2):
    for L in range(2):
        for W in range(2):
            for N in range(2):
                if ((not H <= L) <= ((not W <= N) and H)) * 1 == 0:
                    print(H, L, W, N, ((not H <= L) <= ((not W <= N) and H)) * 1)
