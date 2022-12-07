with open('24.txt') as input_file:
    s = input_file.read()

sub = ''
while sub in s:
    sub += 'CA'
sub = sub[:-2]
print(sub in s)
print(len(sub))
