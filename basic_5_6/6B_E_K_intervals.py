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

## Целочисленное решение

def lbinsearch(l, r, check, checkparams):
    while l < r:
        m = (l + r) // 2
        if check(m, checkparams):
            r = m
        else:
            l = m + 1
    return l

def check_covering(x, params):
    nums, k = params
    cur_section = (nums[0], nums[0] + x)
    cnt_free = k - 1
    i = 1
    while (i < len(nums)) and cnt_free >= 0:
        if cur_section[1] < nums[i]:
            cur_section = (nums[i], nums[i] + x)
            cnt_free -= 1
        i += 1
    return cnt_free >= 0


n, k = map(int, input().split())
nums = sorted(list(map(int, input().split())))
params = nums, k
l = lbinsearch(0, nums[-1] - nums[0], check_covering, params)
print(l)

'''
input
6 2
1 2 3 9 8 7
output
2

input
6 2
-10000 2 3 9 8 70000
output
10009

'''