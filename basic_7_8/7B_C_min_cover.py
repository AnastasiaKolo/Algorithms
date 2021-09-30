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

# отвечает на запрос, покрыт ли отрезок [0, M] указанными отрезками
def is_covered(m, events):
    covered = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            covered += 1
        else:
            covered -= 1
        if (covered <= 0) and (events[i][0] < m):
            return False
    return True

def best_section(point, idx_start, sections):
    i = idx_start
    bestsection = (0, 0)
    maxright = 0
    while (i < len(sections)) and (sections[i][0] <= point) and (sections[i][1] >= point):
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
    return ans

with open('input.txt') as f:
    m = int(f.readline())
    sections = []
    events = []
    eof = False
    while not eof:
        l, r = map(int, f.readline().split())
        if (l, r) != (0, 0):
            sections.append((l, r))
            # в массив событий сразу добавляем события с признаком
            # начало отрезка -1
            # конец отрезка 1
            # events.append((l, -1, r))
            # events.append((r, 1, l))
        elif (r < 0) or (l >= m):
            # совсем ненужные отрезки пропускаем
            pass
        else:
            eof = True
# events.sort(key=lambda x: (x[0], x[1], -x[2]))
sections.sort(key=lambda x: (x[0], -x[1]))
# ans = is_covered(m, events)
ans2 = is_covered_multi(m, sections)
# print(ans)
if ans2:
    print(len(ans2))
    for rec in ans2:
        print(str(rec[0]) + ' ' + str(rec[1]))
else:
    print('No solution')

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


'''