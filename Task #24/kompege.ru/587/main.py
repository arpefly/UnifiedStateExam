with open('24.txt') as input_file:
    count = 0
    for s in input_file.readlines():
        quantity_a = s.count('A')
        quantity_b = s.count('B')
        if quantity_b / quantity_a >= 1.05:
            count += 1
    print(count)
