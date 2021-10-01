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
# Объединение прямоугольников





# загрузим координаты
with open('input.txt') as f:
    n = int(f.readline())
    x_coords = []
    y_sections = []
    for i in range(n):
        x1, x2, y1, y2 = map(float, f.readline().split())
        x_coords.append((x1, -1)) # начало
        x_coords.append((x2, 1))  # конец
        y_sections.append(y1, -1, x1, x2)# начало
        y_sections.append(y2, 1, x1, x2)  # конец
    active_x = 0
    area = 0
    length_x = 0
    for x in range(1, len(x_coords)):
        len_x = x[i] - x[i-1]
        prev_y = 0






    return area