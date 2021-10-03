# Лекция 8 Деревья
# https://youtu.be/lEJzqHgyels
# Пример 1 - собственный менеджер памяти
#
# Есть заранее неизвестное кол-во структур с двумя ссылками на другие структуры
# Известно максимальное кол-во возможных структур (ограничение по памяти)
# Учимся выделять и освобождать память
#
def initmemory(maxn):
    memory = []
    for i in range(maxn):
        memory.append([0, i + 1, 0])
    return [memory, 0]

def newnode(memstruct):
    memory, firstfree = memstruct
    memstruct[1] = memory[firstfree][1]
    return firstfree

def delnode(memstruct, index):
    memory, firstfree = memstruct
    memory[index][1] = firstfree
    memstruct[1] = index

# Бинарное дерево поиска
# у каждого узла есть два сына - левый и правый
# в левом поддереве ключи меньше, а в правом - больше
# Если ключи поступают в случайном порядке, то глубина дерева будет O(log N)
# Каждое поддерево является деревом
#
#
# Реализация поиска
# memstruct - структура в которой хранится дерево и список свободных узлов
# root - корень
def find(memstruct, root, x):
    key = memstruct[0][root][0]
    if x == key:
        return root
    elif x < key:
        left = memstruct[0][root][1]
        if left == -1:
            return -1
        else:
            return find(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            return -1
        else:
            return find(memstruct, right, x)


def createandfillnode(memstruct, key):
    index = newnode(memstruct)
    memstruct[0][index][0] = key
    memstruct[0][index][1] = -1
    memstruct[0][index][2] = -1
    return index

def add(memstruct, root, x):
    key = memstruct[0][root][0]
    if x < key:
        left = memstruct[0][root][1]
        if left == -1:
            memstruct[0][root][1] = createandfillnode(memstruct, x)
        else:
            add(memstruct, left, x)
    elif x > key:
        right = memstruct[0][root][2]
        if right == -1:
            memstruct[0][root][2] = createandfillnode(memstruct, x)
        else:
            add(memstruct, right, x)

# создание дерева
memstruct = initmemory(20)
root = createandfillnode(memstruct, 8)
add(memstruct, root, 10)
add(memstruct, root, 9)
add(memstruct, root, 14)
add(memstruct, root, 13)
add(memstruct, root, 3)
add(memstruct, root, 1)
add(memstruct, root, 6)
add(memstruct, root, 4)
add(memstruct, root, 7)

print(memstruct)
# для удаления
# смотрим является ли удаляемый эл-т листовым

def delnode(memstruct, root, x):
    index_del = find(memstruct, root, x)
    left = memstruct[0][index_del][1]
    right = memstruct[0][index_del][2]
    # если нет потомков - просто удаляем элемент
    # но надо стереть ссылку на него в элементе-родителе
    if left == -1 and right == -1:
        pass
    # если 1 потомок (неважно, левый или правый)
    # удаляем элемент, на его место переставляем его потомка

    # если два потомка - самый сложный случай
    # меняем его на самый левый из правого поддерева, а тот удаляем

# Обход дерева
# Можно получить отсортированную посл-ть всех ключей в дереве
# - Идем влево до упора
# - Когда не можем пойти влево, печатаем что хранится в узле
# - Идем направо
# - Когда не можем пойти направо, заканчиваем выполнение функции



# Небинарные деревья
# Все дети хранятся в родительском узле списком
# Обходим так же, как бинарное, запуская рекурсивную функцию для всех детей



# Сериализация дерева Хаффмана
# Алгоритм Хаффмана позволяет сопоставить более часто встреч символам более короткий код
# Каждый раз берем два самых редко встреч символа и объед их в один узел
# Строим бин дерево кладем буквы в листья. Переход в левого сына кодируется числом 0
# в правого - числом 1 , а код симовла - это все ребра на пути от корня до листа