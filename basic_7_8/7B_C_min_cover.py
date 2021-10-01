# C_min_cover
# На прямой задано некоторое множество отрезков с целочисленными координатами концов [Li, Ri].
# Выберите среди данного множества подмножество отрезков, целиком покрывающее отрезок [0, M],
# (M — натуральное число), содержащее наименьшее число отрезков.
#
# Формат ввода
# В первой строке указана константа M (1 ≤ M ≤ 5000). В каждой последующей строке записана
# пара чисел Li и Ri (Li, Ri ≤ 50000), задающая координаты левого и правого концов отрезков.
# Список завершается парой нулей. Общее число отрезков не превышает 100 000.
#
# Формат вывода
# В первой строке выходного файла выведите минимальное число отрезков, необходимое для
# покрытия отрезка [0; M]. Далее выведите список покрывающего подмножества, упорядоченный по
# возрастанию координат левых концов отрезков. Список отрезков выводится в том же формате,
# что и во входe. Завершающие два нуля выводить не нужно. Если покрытие отрезка [0, M]
# исходным множеством отрезков [Li, Ri] невозможно,
# то следует вывести единственную фразу “No solution”.

def best_section(point, idx_start, sections):
    i = idx_start
    bestsection = (0, 0)
    maxright = 0
    while (i < len(sections)) and (sections[i][0] <= point): #and (sections[i][1] >= point)
        if sections[i][1] - point > maxright:
            bestsection = sections[i]
            maxright = sections[i][1] - point
        i += 1
    return bestsection

def is_covered_multi(m, sections):
    current_point = 0
    ans = []
    i = 0
    while (current_point <= m) and (i < len(sections)):
        max_right_section = best_section(current_point, i, sections)
        if max_right_section != (0, 0):
            ans.append(max_right_section)
            current_point = max_right_section[1]
        elif max_right_section == (0, 0) and (current_point < m):
            return []
        i += 1
    if ans and ans[-1][1] < m:
        return []
    return ans

with open('input.txt') as f:
    m = int(f.readline())
    set_sections = set()
    eof = False
    while not eof:
        l, r = map(int, f.readline().split())
        if (r > 0) and (l < m):
            set_sections.add((l, r))
        elif (l, r) == (0, 0):
            eof = True
sections = sorted(set_sections, key=lambda x: (x[0], -x[1]))
ans2 = is_covered_multi(m, sections)
if ans2:
    print(len(ans2))
    for rec in ans2:
        print(str(rec[0]) + ' ' + str(rec[1]))
else:
    print('No solution')


'''
input
500
-1000 13
5000 50000
15 499
13 18
18 500
15 18
-5000 5
-8000 -3
0 0

output
3
-1000 13
13 18
18 500

input
5000
-50000 4999
0 0

output
No solution

'''

'''
input
1
-1 0
-5 -3
2 5
0 0

output
No solution

input
1
-1 0
0 1
0 0

output
1
0 1


input
100
-1 0
0 20
80 100
20 80
0 0

output
3
0 20
20 80
80 100

'''