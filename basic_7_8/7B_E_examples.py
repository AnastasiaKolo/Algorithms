# Найти длину объединения отрезков на прямой

def find_intersections(n, sections):
    events = []
    for i in range(n):
        events.append((sections[i][0], -1)) # начало
        events.append((sections[i][1], 1))  # конец
    events.sort()
    active = 0
    length = 0
    for i in range(len(events)):
        if active > 0:
            length += events[i][0] - events[i - 1][0]
        if events[i][1] == -1:
            active += 1
        else:
            active -= 1
    return length

# with open('input.txt') as f:
#     n = int(f.readline())
#     sections = []
#     for i in range(n):
#         x1, x2 = map(float, f.readline().split())
#         sections.append((x1, x2))
#
# l = find_intersections(n, sections)
# print(l)

# ---------------------------------------------------------------------------------
# Объединение прямоугольников - посчитать площадь


# with open('input.txt') as f:
#     n = int(f.readline())
#     x_coords = []
#     y_sections = []
#     for i in range(n):
#         x1, x2, y1, y2 = map(float, f.readline().split())
#         x_coords.append(x1)  # начало
#         x_coords.append(x2)  # конец
#         y_sections.append((y1, 1, x1, x2))  # начало
#         y_sections.append((y2, -1, x1, x2))  # конец
# x_coords.sort()
# y_sections.sort()
# area = 0
# for x in range(1, len(x_coords)):
#     prev_y = 0
#     cnt = 0
#     for y in range(len(y_sections)):
#         # Перебираем горизонтальный отрезок
#         if (y_sections[y][3] <= x_coords[x - 1]) or (y_sections[y][2] >= x_coords[x]):
#             # Если отрезок не пересекает текущую полосу – пропускаем его
#             continue
#         if cnt == 0:
#             # Если текущий отрезок - первый, запоминаем его
#             prev_y = y_sections[y][0]
#         cnt += y_sections[y][1]
#         # Увеличиваем или уменьшаем кол - во открытых отрезков
#         if cnt == 0:
#             # Если все прямоугольники закрылись – прибавляем их площадь
#             area += (y_sections[y][0] - prev_y) * (x_coords[x] - x_coords[x - 1])
# print(area)

# ---------------------------------------------------------------------------------
# Пересечение прямоугольников - посчитать площадь


with open('input.txt') as f:
    n = int(f.readline())
    x_coords = []
    y_sections = []
    for i in range(n):
        x1, x2, y1, y2 = map(float, f.readline().split())
        x_coords.append(x1)  # начало
        x_coords.append(x2)  # конец
        y_sections.append((y1, 1, x1, x2))  # начало
        y_sections.append((y2, -1, x1, x2))  # конец
x_coords.sort()
y_sections.sort()
area = 0
for x in range(1, len(x_coords)):
    prev_y = 0
    cnt = 0
    for y in range(len(y_sections)):
        # Перебираем горизонтальный отрезок
        if (y_sections[y][3] <= x_coords[x - 1]) or (y_sections[y][2] >= x_coords[x]):
            # Если отрезок не пересекает текущую полосу – пропускаем его
            continue
        if (cnt == 1) and (y_sections[y][1] == 1):
            # Если текущий отрезок - второй, и он открывающий, запоминаем его
            prev_y = y_sections[y][0]
        # Увеличиваем или уменьшаем кол - во открытых отрезков
        cnt += y_sections[y][1]
        if (cnt == 1) and (y_sections[y][1] == -1):
            # Если все прямоугольники закрылись – прибавляем их площадь
            area += (y_sections[y][0] - prev_y) * (x_coords[x] - x_coords[x - 1])
print(area)


'''
input
2
1 3 0 3
2 4 1.5 4.5

output
1.5
'''