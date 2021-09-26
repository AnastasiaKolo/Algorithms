# Даны n точек на прямой, нужно покрыть их
# k отрезками одинаковой длины ℓ.
# Найдите минимальное ℓ.
#
# Формат ввода
# На первой строке n (1≤n≤10^5) и k (1≤k≤n).
# На второй n чисел xi (∣∣xi∣∣≤10^9).
# Формат вывода
# Минимальное такое ℓ, что точки можно покрыть
# k отрезками длины ℓ.

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def checkptreesinforest(days, params):
    a, k, b, m, x = params
    dmitr = a * days - a * (days // k)
    fedr = b * days - b * (days // m)
    return dmitr + fedr >= x


a, k, b, m, x = map(int, input().split())



'''
input
6 2
1 2 3 9 8 7
output
2
'''