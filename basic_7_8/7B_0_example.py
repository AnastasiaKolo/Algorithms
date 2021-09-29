# 0_example
# Метод сортировки событий
# #
# Что это такое:
# пусть есть некоторые отрезки времени (например, время которое чел находился на сайте)
# есть моменты события (например приход и уход)
# Надо что-нибудь посчитать
#
# Задача 1
# Сайт посетило N чел
# для каждого известно время входа IN время выхода OUT
# Считается что чел был на сайте с момента IN по OUT включительно
# Какое макс кол-во чел было на сайте одновременно?


def maxvisitorsonline(n, tin, tout):
    events = []
    for i in range(n):
        # константы выбраны таким образом,
        # чтобы событие входа в сортировке стояло раньше выхода
        events.append((tin[i], -1))
        events.append((tout[i], -1))
    events.sort()
    online = 0
    maxonline = 0
    for event in events:
        if event[i][1] == -1:
            online += 1
        else:
            online -= 1
        maxonline = max(online, maxonline)
    return maxonline

# Задача 2
# Условие аналогично задаче 1.
# Нужно посчитать, какое суммарное время на сайте был хотяб 1 чел
# решение
# если мы пришли в событие с ненулевым счетчиком кол-ва людей, то между
# текущим и предыдущим событием на сайте кто-то был
# прибавим к ответу время между текущим и предыдущим событием

def timewithvisitors(n, tin, tout):
    events = []
    for i in range(n):
        # константы выбраны таким образом,
        # чтобы событие входа в сортировке стояло раньше выхода
        events.append((tin[i], -1))
        events.append((tout[i], -1))
    events.sort()
    online = 0
    notemptytime = 0
    for i in range(len(events)):
        if online > 0:
            notemptytime += events[i][0] - events[i - 1][0]
        if events[i][1] == -1:
            online += 1
        else:
            online -= 1
    return notemptytime

# Задача 3
# Условие аналогично задаче 1.
# + есть начальник , который M раз заходил на сайт в моменты времени BOSS
# и смотрел сколько сейчас людей онлайн
# Посещения сайта начальником упорядочены по времени
# Определить, какие показания счетчиков увидел начальник
#
# Решение
# Создадим третий тип события - приход начальника (0)
# и при наступлении этого события будем сохранять счетчики

def bosscounters(n, tin, tout, m, tboss):
    events = []
    for i in range(n):
        # константы выбраны таким образом,
        # чтобы событие входа в сортировке стояло раньше выхода
        events.append((tin[i], -1))
        events.append((tout[i], -1))
    for i in range(m):
        # константы выбраны таким образом,
        # чтобы событие входа в сортировке стояло раньше выхода
        events.append((tboss[i], 0))
    events.sort()
    online = 0
    bossans = []
    for event in events:
        if event[i][1] == -1:
            online += 1
        elif event[i][1] == 1:
            online -= 1
        else:
            bossans.append(online)
    return bossans