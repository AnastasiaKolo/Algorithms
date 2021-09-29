# D_kittens
#
# На прямой в точках
# a1,a2,…,an (возможно, совпадающих) сидят n  котят. На той же прямой лежат
# m отрезков[l1,r1],[l2,r2],…,[lm,rm]
# . Нужно для каждого отрезка узнать его наполненность котятами — сколько котят сидит на отрезке.
# Формат ввода
# На первой строке
# n  и m (1≤n,m≤10^5). На второй строке n целых чисел ai (0≤ai≤10^9).
# Следующие m строк содержат пары целых чисел li,ri
# (0≤li≤ri≤10^9 ).
# Формат вывода
# Выведите m целых чисел.
# i-е число — наполненность котятами
# i-го отрезка.

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


with open('input.txt') as f:
    m, n = map(int, f.readline().split())
    nums = list(map(int, f.readline().split()))
    nums.sort()
    sections = []
    ans = []
    for i in range(n):
        l, r = map(int, f.readline().split())
        kittens = countlr(nums, l, r)
        ans.append(kittens)

print(' '.join(str(i) for i in ans))

'''
input
10 10
0 1 2 3 4 5 6 7 8 9
0 1
0 2
0 3
0 4
0 5
0 6
0 7
0 8
0 9
-10 100
output
2 3 4 5 6 7 8 9 10 10

input

output


'''