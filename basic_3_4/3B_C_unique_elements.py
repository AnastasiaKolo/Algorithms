# Дан список. Выведите те его элементы, которые встречаются в списке
# только один раз. Элементы нужно выводить в том порядке,
# в котором они встречаются в списке.
# Формат ввода
# Вводится список чисел. Все числа списка находятся на одной строке.
# Формат вывода
# Выведите ответ на задачу.

list1 = list(map(int, input().strip().split()))


once = set()
more = set()
for i in range(len(list1)):
    if list1[i] in once:
        more.add(list1[i])
    once.add(list1[i])
for i in range(len(list1)):
    if list1[i] not in more:
        print(list1[i], end=' ')
