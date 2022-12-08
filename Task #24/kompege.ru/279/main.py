with open('24.txt') as input_file:
    s = input_file.read()

print(s.replace('JBOSS', 'J@').replace('BOSSJ', '@J').replace('JBOSSJ', 'J@J').count('BOSS'))
