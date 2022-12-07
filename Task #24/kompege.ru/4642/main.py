with open('24.txt') as input_file:
    s = input_file.read()

s = s.replace('B', 'A').replace('2', '1')
s = s.replace('A1', '@').replace('A', ' ').replace('1', ' ')
print(max(len(item) for item in s.split()))
