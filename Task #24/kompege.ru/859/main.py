with open('24.txt') as input_file:
    count = 0
    for s in input_file.readlines():
        if s.count('S') == s.count('X'):
            count += 1
    print(count)
