from itertools import product

def task_1979():
    print(2*6*6*4)

def task_1980():
    print(4*3*3*3*3*4)

def  task_1981():
    count = 0
    for item in product('ПУЛЯ', repeat=6):
        if ''.join(item).count('У') == 2:
            count += 1
    print(count)

def task_1982():
    count = 0
    for item in product('ЛОДКА', repeat=4):
        if ''.join(item).count('О') >= 2:
            count += 1
    print(count)

def task_1983():
    cont = 0
    for item in product('САЛО', repeat=6):
        if 0 < ''.join(item).count('О') <= 3:
            cont += 1
    print(cont)

def task_1984():
    count = 0
    for item in product('ИГРОК', repeat=5):
        s = ''.join(item)
        if len(set(item)) == 5 and not s.startswith('К') and s.count('РОК') == 0:
            count += 1
    print(count)

def task_1985():
    count = 0
    wrong = [''.join(sub) for sub in product('АИОУ', repeat=2)] + [''.join(sub) for sub in product('БКЛН', repeat=2)]
    for item in product('АБИКОЛУН', repeat=8):
        s = ''.join(item)
        if len(set(s)) == 8 and all(sub not in s for sub in wrong):
            count += 1
    print(count)


if __name__ == '__main__':
    task_1985()
