# Дан массив из
# N  целых чисел. Все числа от −10^9 до 10^9.
# Нужно уметь отвечать на запросы вида
# “Cколько чисел имеют значения от L до R?”.
# Формат ввода
# Число N (1≤N≤10^5). Далее N целых чисел.
# Затем число запросов K (1≤K≤10^5).
# Далее K пар чисел L,R (−10^9≤L≤R≤10^9) — собственно запросы.
#
# Формат вывода
# Выведите K чисел — ответы на запросы.

# Решаем двумя бинарными поисками первый >= L, второй > R
def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def checkisgt(index, params):
    seq, x = params
    return seq[index] > x

def checkisge(index, params):
    seq, x = params
    return seq[index] >= x

def findfirst(seq, x, check):
    ans = lbinsearch(0, len(seq) - 1, check, (seq, x))
    if not check(ans, (seq, x)):
        return len(seq)
    return ans

def countlr(seq, l, r):
    indexgt = findfirst(seq, r, checkisgt)
    indexge = findfirst(seq, l, checkisge)
    return indexgt - indexge

## проверка
with open('input.txt') as f:
    n = int(f.readline())
    nums = sorted(list(map(int, f.readline().split())))
    k = int(f.readline())
    reqs = []
    for i in range(k):
        x, y = map(int, f.readline().split())
        reqs.append((x, y))
ans = []
for req in reqs:
    m = countlr(nums, req[0], req[1])
    ans.append(m)
print(' '.join(str(i) for i in ans))

'''
input
5
10 1 10 3 4
4
1 10
2 9
3 4
2 2

output
5 2 2 0 


'''