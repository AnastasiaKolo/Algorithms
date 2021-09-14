# Множества

# Пример 1. Наше собственное множество
# операции:
# - добавление
# - поиск
# - удаление

setsize = 10
# создаем список из пустых списков
myset = [[] for _ in range(setsize)]


def add(x):
    if not find(x):
        myset[x % setsize].append(x)


def find(x):
    for now in myset[x % setsize]:
        if now == x:
            return True
    return False


def delete(x):
    xlist = myset[x % setsize]
    for i in range(len(xlist)):
        if xlist[i] == x:
            xlist[i] = xlist[len(xlist) - 1]
            xlist.pop()
            return

# Пример 2.

# Пример 3.
