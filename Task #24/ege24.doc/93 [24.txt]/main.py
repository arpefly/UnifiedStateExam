with open('24.txt') as file:
    data = file.read()

cur_value = 1
max_value = 0

for i in range(1, len(data)):
    if ord(data[i]) > ord(data[i-1]):
        cur_value += 1
        look += data[i]
        if cur_value > max_value:
            max_value = cur_value
    else:
        cur_value = 1
        look = data[i]

print(max_value)
