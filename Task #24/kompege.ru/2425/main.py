with open('24.txt') as input_file:
    s = input_file.read()

sub = ''
while sub in s:
    sub += 'DBAC'
sub = sub[:-1]
print(sub in s)
print(len(sub))
