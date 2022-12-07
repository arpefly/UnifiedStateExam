with open('24.txt') as input_file:
    s = input_file.read()

s = s.replace('O', 'A').replace('C', 'B').replace('D', 'B')
s = s.replace('BA', '@').replace('A', ' ').replace('B', ' ')
print(max(len(item) for item in s.split()))
