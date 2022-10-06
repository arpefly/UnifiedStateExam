with open('24.txt') as file:
    data = file.read()

count = 0
maxValue = 0

for i in range(1, len(data)):
    if data[i] != data[i-1]:
        count += 1
    else:
        maxValue = max(maxValue, count)
        count = 1

print(maxValue)
