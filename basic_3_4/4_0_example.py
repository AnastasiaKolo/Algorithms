# Словари
# Сортировка подсчетом
# Преждевременная оптимизация

# Сортировка подсчетом------------------------------------------------------------------------------
# Нужно отсортировать массив из N целых чисел, каждое из которых до 0 до K
# Значений К относительно немного (например школьные оценки)
# Обычная сортировка займет O(N log N)
# Будем считать кол-во вхождений каждого числа, а замем выведем каждое число столько раз, сколько оно
# встречалось. Это займет O(N + K) и потребует O(K) Дополнительной памяти
# Интервал значений можно сдвинуть, так чтобы он был не от 0 до K, а min .. max массива


def countsort(seq):
    # в этой функции меняется параметр, который передали в функцию
    minval = min(seq)
    maxval = max(seq)
    k = (maxval - minval + 1) # кол-во возможных значений
    count = [0] * k
    for now in seq:
        count[now - minval] += 1
    nowpos = 0
    # потом бежим по исходной последовательности
    # и меняем значения на отсортированные
    for val in range(0, k):
        for i in range(count[val]):
            seq[nowpos] = val + minval
            nowpos += 1


# Пример задачи
# Есть 2 числа X и Y без ведущих нулей
# Проверить, можно ли получить первое из второго перестановкой цифр

def isdigitpermutation(x, y):
    def countdigits(num):
        digitcount = [0] * 10
        while num > 0:
            lastdigit = num % 10
            digitcount[lastdigit] += 1
            num //= 10
        return digitcount

    digitsx = countdigits(x)
    digitsy = countdigits(y)
    for digit in range(10):
        if digitsx[digit] != digitsy[digit]:
            return False
    return True

# Словарь
# Это аналог множества, но к каждому ключу приписано значение
# Искать по значению в словаре нельзя
# Константа в сложности у словарей гораздо больше чем у спискоа,
# поэтому где возможно - лучше использовать сортировку подсчетом
# Если данные сильно разреженные - сортировку подсчетом не использовать

# Пример задачи_________________________________________________________________
# Шахматная доска размером NxN (N < 10^9)
# На ней M ладей (M < 10^5). Ладьи задаются парой координат (i, j)
# Определить, сколько пар ладей бьют друг друга
# Решение
# для каждой занятой горизонтали и вертикали будем хранить число пар ладей в них.
# кол-во пар в ряде на 1 меньше, чем кол-во ладей
# Суммируем это кол-во для всех горизонталей и вертикалей
#

def countbeatingrooks(rookcoords):
    def addrook(roworcol, key):
        if key not in roworcol:
            roworcol[key] = 0
        roworcol [key] += 1

    def countpairs(roworcol):
        pairs = 0
        for key in roworcol:
            pairs += roworcol[key] - 1
        return pairs

    rooksinrow = {}
    rooksincol = {}
    for row, col in rookcoords:
        addrook(rooksinrow, row)
        addrook(rooksincol, col)
    return countpairs(rooksinrow) + countpairs(rooksincol)

# Построить гистограмму по строке
# Hello, world!
'''
      #
      ##
##########
 !,Hdelorw
'''
# Для каждого символа посчитаем, сколько раз он встречался
# Найдем самый частый символ и переберем кол-во от этого числа до 1
# Пройдем по всем отсортированным ключам и если число больше счетчика - выведем #
def printchar(s):
    symcount = {}
    maxsymcount = 0
    for sym in s:
        if sym not in symcount:
            symcount[sym] = 0
        symcount[sym] += 1
        maxsymcount = max(maxsymcount, symcount[sym])
    sorteduniquesyms = sorted(symcount.keys())
    for row in range(maxsymcount, 0, -1):
        for sym in sorteduniquesyms:
            if symcount[sym] >= row:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    print(''.join(sorteduniquesyms))



# char = input()
# printchar(char)



# Преждевременная оптимизация
# Обращаем внимание на другие качества алгоритма:
# - потребление памяти
# - время на реализацию
# - сложность поддержки
# - возможность распараллеливания
# - необходимая квалификация сотрудника
# - стоимость оборудования


# Задача 4
# Сгруппировать слова по общим буквам
# sample input: [tea, eat, tan, ate, nat, bat]
# sample output: [[tea, eat, ate], [tan, nat], [bat]]

def groupwords(words):
    def keybyword(word):
        # здесь проблема, если слова длинные
        # то на sorted уйдет много времени
        # поэтому расчет ключа вынесли в отдельную функцию
        # чтобы при случае ее оптимизировать
        return ''.join(sorted(word))
    groups = {}
    for word in words:
        sortedword = keybyword(word)
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans

# второй вариант, функция keybyword оптимизирована
# в худших случаях (оч длинные слова)
# будет работать эффективнее
# но в обычных случаях медленнее
def groupwords(words):
    def keybyword(word):
        # преобразование типа aaba -> a3b2
        symcnt = {}
        for sym in word:
            if sym not in symcnt:
                symcmt[sym] = 0
            symcmt[sym] += 1
        lst = []
        for sym in sorted(symcnt.keys()):
            lst.append(sym)
            lst.append(str(symcnt[sym]))
        return ''.join(lst)
    groups = {}
    for word in words:
        sortedword = keybyword(word)
        if sortedword not in groups:
            groups[sortedword] = []
        groups[sortedword].append(word)
    ans = []
    for sortedword in groups:
        ans.append(groups[sortedword])
    return ans

# Критерий для разбиения на функции:
# Понятность - человек в памяти может хранить около 7 переменных одновременно
