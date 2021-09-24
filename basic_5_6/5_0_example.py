# префиксные суммы
# используются , когда надо много раз дать ответ на вопрос
# чему равна суммы элементов на таком-то отрезке?
# префиксная сумма = сумма всех эл-тов от первого до текущего
# массив преф.сумм на 1 эл-т длиннее, чем исходный массив чисел

# RSQ = Range Sub Query
# ответ за О(1) построение массива за О(N)
# Реализация RSQ через префиксные суммы
def makeprefixsums(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums)+1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    return prefixsum

def rsq(prefixsum, l ,r):
    return prefixsum[r] - prefixsum[l]
# если есть лимит по времени, то вызов функции замедляет
# в питоне так
# поэтому если время очень критично то вставить код непосредственно в программу,
# без функции


# ----- пример 1----------------------------------------------
# Дана последовательность чисел длиной N и M запросов
# Запросы "Сколько нулей на полуинтервале [L, R]"
# Решение " в лоб" за O(N*M)
# - для каждого запроса перебираем все числа
# от L до R (не включительно) и считаем кол-во нулей
# В худшем случае каждый запрос за O(N) Общая сложность за O(N*M)
#
# Применим идею префиксных сумм
# Вместо префиксных сумм будем хранить кол-во нулей

def makeprefixzeroes(nums):
    prefixzeroes = [0] * (len(nums) + 1)
    for i in range(1, len(nums)+1):
        if nums[i - 1] == 0:
            prefixzeroes[i] = prefixzeroes[i - 1] + 1
        else:
            prefixzeroes[i] = prefixzeroes[i - 1]
    return prefixzeroes

def rsq(prefixzeroes, l ,r):
    return prefixzeroes[r] - prefixzeroes[l]

# ----пример 2-----------------------------------------------
# Дана последовательность чисел длиной N
# Найти кол-во отрезков с нулевой суммой
#
# Решение за O(N^3): переберем начало и конец отрезка и просто
# просуммируем все его эл-ты
def countzerosumranges(nums):
    cntranges = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            rangesum = 0
            for k in range(i ,j):
                rangesum += nums[k]
            if rangesum == 0:
                cntranges += 1
    return cntranges
# Решение за O(N^2): переберем начало и двигаем конец отрезка
# и просуммируем все его эл-ты
# здесь надо не пропустить случай когда всего одно число и это 0
def countzerosumranges(nums):
    cntranges = 0
    for i in range(len(nums)):
        rangesum = 0
        for j in range(i, len(nums)):
            rangesum += nums[j]
            if rangesum == 0:
                cntranges += 1
    return cntranges
# нормальное решение за O(N)
# посчитаем префиксные суммы.
# Одинаковые преф суммы означают, что сумма на отрезке
# с началом и концом в позициях, на которых достигаются
# одинаковые преф суммы, будет равна нулю
#
# Считаем преф суммы. Всякий раз, встречая новую преф сумму,
# мы считаем сколько раз она была раньше
def countprefixsums(nums):
    # для корректной обработки отрезков,
    # прижатых к левому краю
    prefixsumbyvalue = {0: 1}
    nowsum = 0
    for now in nums:
        if nowsum not in prefixsumbyvalue:
            prefixsumbyvalue[nowsum] = 0
        prefixsumbyvalue[nowsum] += 1
    return prefixsumbyvalue

def countzerosumranges(prefixsumbyvalue):
    cntranges = 0
    for nowsum in prefixsumbyvalue:
        cntsum = prefixsumbyvalue[nowsum]
        # комбинаторная формула, сколько пар образуют
        # возможные левые и правые груницы этих отрезков
        cntranges += cntsum * (cntsum - 1) // 2


# ------------------------------------------
# Метод двух указателей
# Дана отсортированная последовательность чисел длиной N и число K
# Нужно найти кол-во пар чисел (A, B) таких что B - A > K
#
# O(N^2) Переберем все пары и проверим для каждой пары условие

def cntpairwithdiffgtk(sortednums, k):
    cntpairs = 0
    for first in range(len(sortednums)):
        for last in range(first, len(sortednums)):
            if sortednums[last] - sortednums[first] > k:
                cntpairs += 1
    return cntpairs

# O(N) Возьмем наименьшее число (1-й указатель) и найдем
# первое подходящее большее. Все ещё большие числа подходят
# дальше двигаем первый указатель на следующее и тд.

def cntpairwithdiffgtk(sortednums, k):
    cntpairs = 0
    last = 0
    for first in range(len(sortednums)):
        while last < len(sortednums) and sortednums[last] - sortednums[first] <= k:
            last += 1
        cntpairs += len(sortednums) - last
    return cntpairs







