# # A_paint_straight
# На числовой прямой окрасили N отрезков.
# Известны координаты левого и правого концов каждого отрезка (Li и Ri).
# Найти длину окрашенной части числовой прямой.
#
# Формат ввода
# В первой строке находится число N, в следующих N строках -
# пары Li и Ri. Li и Ri - целые, -10^9 ≤ Li ≤ Ri ≤ 10^9, 1 ≤ N ≤ 15 000
#
# Формат вывода
# Вывести одно число - длину окрашенной части прямой.

def painted_straight(sections):
    sections.sort()
    painted = 0
    painted_length = 0
    for i in range(len(sections)):
        if painted > 0:
            painted_length += sections[i][0] - sections[i - 1][0]
        if sections[i][1] == -1:
            painted += 1
        else:
            painted -= 1
    return painted_length

with open('input.txt') as f:
    n = int(f.readline())
    sections = []
    for i in range(n):
        # в массив сразу добавляем события с признаком
        # начало отрезка -1
        # конец отрезка 1
        l, r = map(int, f.readline().split())
        sections.append((l, -1))
        sections.append((r, 1))
painted_length = painted_straight(sections)
print(painted_length)

'''
input
1
10 20
output
10

input
1
10 10
output
0

input
2
10 20
20 40

output
30


input

output



'''