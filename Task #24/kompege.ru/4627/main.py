with open('24.txt') as input_file:
    s = input_file.read()

s = s.replace('NPO', '@').replace('PNO', '@')
s = s.replace('N', ' ').replace('O', ' ').replace('P', ' ')
print(max(len(item) for item in s.split()))
