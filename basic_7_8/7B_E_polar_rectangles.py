# # E_polar_rectangles
# https://contest.yandex.ru/contest/29396/problems/E/
# Пусть задана стандартная декартова плоскость.
# Если на ней нарисовать две окружности с центром в начале координат, то
# область, находящаяся между ними, называется кольцом (на рисунке обозначена синим).
# Если на ней нарисовать два луча, то область, заметаемая первым лучом при движении
# ко второму, называется углом (т.е. область между этими двумя лучами, на
# рисунке обозначена зеленым). Полярным прямоугольником называется
# пересечение некоторого угла с некоторым кольцом (на рисунке обозначено красным).
#
# Задано несколько полярных прямоугольников. Найдите площадь их пересечения.
# Помните, что пересечение полярных прямоугольников может состоять из нескольких частей!
#
# Формат ввода
# В первой строке вводится целое число N — количество прямоугольников
# (1 <= N <= 100 000). Далее в N строках содержится описание
# прямоугольников. Каждый прямоугольник описывается четверкой действительных
# чисел r1, r2, φ1, φ2, где r1, r2 обозначают радиусы окружностей, образующих
# кольцо (r1 < r2), а φ1, φ2 обозначают углы, образованные первым и
# вторым лучами с осью абсцисс, заданные в радианах. При этом заметается
# область от первого луча до второго в направлении против часовой стрелки
# (т.е. возрастания углов), даже в случае, когда φ1 > φ2. Все числа
# заданы максимум с шестью знаками после десятичной точки. Углы лежат в
# полуинтервале [0, 2π), а радиусы не превосходят 10^6. Гарантируется,
# что φ1 != φ2.
#
# Формат вывода
# Выведите единственное число — площадь искомого пересечения. Ответ
# будет считаться правильным, если его абсолютная или относительная
# погрешность не будет превышать 10^-6.
PI = 3.141592653589793

def calc_area(r1, r2, fi1, fi2):
    a = (fi2 - fi1)*(r2 ** 2 - r1 ** 2) / 2
    return a

def input_polar_rects(filename='input.txt'):
    with open(filename) as f:
        n = int(f.readline())
        fi_coords = []
        events_fi = []
        for i in range(n):
            r1, r2, fi1, fi2 = map(float, f.readline().split())
            if fi2 > fi1:
                # прямоугольник не проходит через 0
                fi_coords.append(fi1)
                fi_coords.append(fi2)
                events_fi.append((r1, 1, fi1, fi2))  # начало
                events_fi.append((r2, -1, fi1, fi2))  # конец
            else:  # fi2 < fi1
                # прямоугольник проходит через 0
                # поэтому добавим два с разбиением в точке 0
                fi_coords.append(fi1)
                fi_coords.append(fi2)
                fi_coords.append(0)
                fi_coords.append(2 * PI)
                events_fi.append((r1, 1, 0, fi2))  # начало
                events_fi.append((r1, -1, fi1, 2 * PI))  # конец
                events_fi.append((r2, 1, 0, fi2))  # начало
                events_fi.append((r2, -1, fi1, 2 * PI))  # конец
    events_fi.sort(key=lambda x: (x[0], -x[1], x[2], x[3]))
    fi_coords.sort()
    return events_fi, fi_coords


def scanline_fi(events_fi, fi_coords):
    area = 0
    for x in range(1, len(fi_coords)):
        prev_r = 0
        cnt = 0
        for y in range(len(events_fi)):
            # Перебираем горизонтальный отрезок
            if (events_fi[y][3] <= fi_coords[x - 1]) or (events_fi[y][2] >= fi_coords[x]):
                # Если отрезок не пересекает текущую полосу – пропускаем его
                continue
            if (cnt == 1) and (events_fi[y][1] == 1):
                # Если текущий отрезок - второй, и он открывающий, запоминаем его
                prev_r = events_fi[y][0]
            # Увеличиваем или уменьшаем кол - во открытых отрезков
            cnt += events_fi[y][1]
            if (cnt == 1) and (events_fi[y][1] == -1):
                # Если все прямоугольники закрылись – прибавляем их площадь
                area += calc_area(prev_r, events_fi[y][0], fi_coords[x - 1], fi_coords[x])
    return area



events_fi, fi_coords = input_polar_rects()
area = scanline_fi(events_fi, fi_coords)
print(area)

'''
input
2
1 3 0 3
2 4 1.5 4.5
output
3.7500000000

input
2
1 2 0 3
1 2 2 1

output
3.0000000000

'''