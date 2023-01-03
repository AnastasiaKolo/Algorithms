Лекция 3: «Множества»
https://youtu.be/PUpmV2ieIHA
Лекция 4: «Словари и сортировка подсчётом»
https://youtu.be/Nb5mW1yWVSs

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
# Дана последовательность положительных чисел длиной N
# и число Х
# Нужно найти 2 различных числа А и В из последовательности,
# таких что А + В = Х или вернуть пару 0, 0 если таких чисел нет

# решение за O(N^2)
def twotermswithsumx(nums, x):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums [j] == x:
                return nums[i], nums [j]
    return 0, 0

# решение за O(N)
def twotermswithsumx(nums, x):
    prevnums = set()
    for nownum in nums:
        if x - nownum in prevnums:
            return nownum, x - nownum
        prevnums.add(nownum)
    return 0, 0


# Пример 3.
# Дан словарь из N слов,
# длина каждого из которых не превосходит К
# В записи каждого из M слов текста (каждое длиной до К)
# может быть пропущена одна буква
# Для каждого слова сказать, входит ли оно
# (возможно, с одной пропущенной буквой) в словарь

# Решение за O(NK + M)

def wordsindict(dictionary, text):
    goodwords = set(dictionary)
    # теперь добавим возможные варианты с пропущенной буквой
    for word in dictionary:
        for delpos in range(len(word)):
            goodwords.add(word[:delpos] + word[delpos+1:])
    ans = []
    for word in text:
        ans.append(word in goodwords)
    return ans