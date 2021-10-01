
with open('input.txt', 'w') as f:
    f.write('5000\n')
    for i in range(100000):
        f.write('1 2\n')
    f.write('0 0\n')