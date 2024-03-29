Лекция 7: «Сортировка событий»
https://youtu.be/hGixDBO-p6Q

Лекция 8: «Деревья»
https://youtu.be/lEJzqHgyels

# 0_example
# Метод сортировки событий
# # Также "Метод сканирующей прямой"
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


### События на круге
# - например ежедневно происходящие события
# - круг - это сутки
# - идея - разрезать отрезки, проходящие через полночь, на два
#
# Также делается два прохода по кругу
#
# Задача 4
# Парковка в ТЦ, на ней N мест (1.. N)
# За день приезжало M автомобилей
# при этом некоторые авто длинные и занимали несколько мест идущих подряд
# для каждого авто известно время приезда и отъезда,
# а также 2 числа - с какого по какое место он занимал
# Если в какой-то момент времени авто уехал с парковочного места,
# то на его место может сразу же встать другой\
#
# Необходимо определить, был ли момент, в котором были заняты все парковочные места

# Решение
# события - приезд и отъезд авто
# причем отъезд должен происходить раньше
# Будем поддерживать кол-во занятых мест. И если после очередного события счетчик равен N,
# то такие моменты были

def isparkingfull(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom + 1))
        events.append((timeout, -1, placeto - placefrom + 1))
    events.sort()
    occupied = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
        elif events[i][1] == 1:
            occupied += events[i][2]
        if occupied == n:
            return True
    return False

# Задача 5
# Условие аналогично
# Необходимо определить, был ли момент, в котором были заняты все парковочные места
# + мин кол-во автомобилей, которыми была занята парковка
# Если такого момента не было, вернуть M+1
#
# Решение
# Добавим еще один счетчик мин кол-во автомобилей, когда заняты все места

def mincarsonfullparking(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom + 1))
        events.append((timeout, -1, placeto - placefrom + 1))
    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
        if occupied == n:
            mincars = min(mincars, nowcars)
    return mincars

# Задача 6
# Условие аналогично
# Необходимо определить, был ли момент, в котором были заняты все парковочные места
# + мин кол-во автомобилей, которыми была занята парковка.
# А также вернуть номера машин (в порядке начального списка)
# Если такого момента не было, вернуть пустой список
#
# Решение (неэффективное)
# Добавим в событие номер авто в списке.
# При обновлении минимума копируем текущее состояние в ответ

def mincarsonfullparking(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom + 1))
        events.append((timeout, -1, placeto - placefrom + 1))
    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1
    carnums = set()
    bestcarnums = set()
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])
        if occupied == n:
            mincars = min(mincars, nowcars)
            bestcarnums = carnums.copy()
    return bestcarnums

# Решение (эффективное)
# Сделать 2 прохода
# За первый проход вычисляем мин кол-во машин
# за второй - создаем список их номеров

def mincarsonfullparking(cars, n):
    events = []
    for car in cars:
        timein, timeout, placefrom, placeto = car
        events.append((timein, 1, placeto - placefrom + 1))
        events.append((timeout, -1, placeto - placefrom + 1))
    events.sort()
    occupied = 0
    nowcars = 0
    mincars = len(cars) + 1
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
        if occupied == n and nowcars < mincars:
            mincars = nowcars
    carnums = set()
    nowcars = 0
    occupied = 0
    for i in range(len(events)):
        if events[i][1] == -1:
            occupied -= events[i][2]
            nowcars -= 1
            carnums.remove(events[i][3])
        elif events[i][1] == 1:
            occupied += events[i][2]
            nowcars += 1
            carnums.add(events[i][3])
        if occupied == n and nowcars == mincars:
            return carnums
    return set()