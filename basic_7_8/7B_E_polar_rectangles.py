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
#PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825
import math

PI = math.pi
def calc_area(r1, r2, fi1, fi2):
    a = (fi2 - fi1)*(r2 ** 2 - r1 ** 2) / 2
    return a

def input_polar_rects(filename='input.txt'):
    with open(filename) as f:
        n = int(f.readline())
        #r_set = set()
        events_fi = []
        max_r1 = 0
        min_r2 = 1000000
        for i in range(n):
            r1, r2, fi1, fi2 = map(float, f.readline().split())
            max_r1 = max(r1, max_r1)
            min_r2 = min(r2, min_r2)
            if fi2 > fi1:
                # прямоугольник не проходит через 0
                events_fi.append((fi1, 1))  # начало
                events_fi.append((fi2, -1))  # конец
            else:  # fi2 < fi1
                # прямоугольник проходит через 0
                # поэтому добавим два с разбиением в точке 0
                events_fi.append((0, 1))  # начало
                events_fi.append((fi2, -1))  # конец
                events_fi.append((fi1, 1))  # начало
                events_fi.append((2 * PI, -1))  # конец
    events_fi.sort(key=lambda x: (x[0], -x[1]))
    r_coords = [max_r1, min_r2]
    return events_fi, r_coords, n


def scanline_fi(events_fi, r_coords, n):
    area = 0
    for x in range(1, len(r_coords)):
        prev_fi = 0
        cnt = 0
        for y in range(len(events_fi)):  # Перебираем угол
            if (cnt == n - 1) and (events_fi[y][1] == 1):
                # Если текущим отерзком открылись все прямоугольники, запоминаем угол
                prev_fi = events_fi[y][0]
            # Увеличиваем или уменьшаем кол-во открытых прямоугольников
            cnt += events_fi[y][1]
            if (cnt == n - 1) and (events_fi[y][1] == -1):
                # Если хотя бы один прямогуольник закрылся – прибавляем площадь
                area += calc_area(r_coords[x - 1], r_coords[x], prev_fi, events_fi[y][0])
    return area

events_fi, r_coords, n = input_polar_rects('input.txt')
area = scanline_fi(events_fi, r_coords, n)
print(area)

# как выяснилось , надо было искать площадь пересечения всех прямоугольников,
# а я искала площадь пересечения где пересекается не меньше двух (WA на 32 тесте)
# но дальше началось TL на 42 тесте


# Решение с разбора
# Сразу находим радиус пересечения всех прямоугольников ("колбасы") потому что это определить легко,
# будет (max r1, min r2)
# *до этого я не догадалась. Если внести это дополнение в мой ответ (то есть избавляемся от массива r_coords),
# вероятно о перестанет TLить
# *просто так не удалось - теперь ML на 52 тесте
# также удаляю лишнюю инфу из events_fi
# *прошло на компиляторе 3.9 без нарушения по memory limit
#
# Решение с разбора - продолжение
# Далее разбираемся с углами методом событий. Поскольку события на круге, делаем так:
# - на первом проходе поддерживаем множество прямоугольников, кот начались, но еще не закончились
# -

'''
test 32
240.56814673910566

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