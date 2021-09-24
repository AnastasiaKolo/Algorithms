# В этой задаче вам нужно будет много раз отвечать на запрос
# «Найдите сумму чисел на отрезке в массиве».
# Формат ввода
# В первой строке записано два целых числа
# n и q  (1≤n,q≤3⋅10^5) - размер массива и количество запросов.
# Во второй строке записаны
# n  целых чисел
# ai (1≤ai≤10^9) - сам массив.
# Далее в q  строках описаны запросы к массиву. Каждый запрос описывается двумя числами
# l,r  (1≤l≤r≤n) - левой и правой границей отрезка, на котором нужно найти сумму.
#
# Формат вывода
# Для каждого запроса в отдельной строке выведите единственное число - сумму на соответствующем отрезке.

def makeprefixsums(nums):
    prefixsum = [0] * (len(nums) + 1)
    for i in range(1, len(nums) + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    return prefixsum

def rsq(prefixsum, l, r):
    # выдает сумму на отрезке, т.е. включая границы
    return prefixsum[r] - prefixsum[l - 1]

n, q = map(int, input().split())
nums = list(map(int, input().split()))
reqs = []
for i in range(q):
    l, r = map(int, input().split())
    reqs.append((l, r))

prefixsum = makeprefixsums(nums)
for i, j in reqs:
    print(rsq(prefixsum, i, j))


'''
input
4 10
1 2 3 4
1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4

output
1
3
6
10
2
5
9
3
7
4

'''