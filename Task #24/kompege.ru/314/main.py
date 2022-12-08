with open('24.txt') as input_file:
    s = input_file.read()

print(s.count('OCK') - s.count('STOCK'))
