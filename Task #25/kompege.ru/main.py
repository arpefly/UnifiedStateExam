from fnmatch import fnmatch

def divs(n):
    tmp = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            tmp |= {i, n // i}
    return sorted(tmp)

def task_3229():
    for x in range(0, 10**9+1, 17):
        if fnmatch(str(x), '12345?6?8'):
            print(x, x // 17)

def task_4603():
    for x in range(0, 10**8, 141):
        if fnmatch(str(x), '1234*7'):
            print(x, x // 141)

def task_3692():
    for x in range(0, 10**9, 169):
        if fnmatch(str(x), '123*567?'):
            print(x, x // 169)

def task_3693():
    for x in range(0, 10**6, 51):
        if fnmatch(str(x), '12*45*'):
            print(x, x // 51)


if __name__ == '__main__':
    task_3693()
