# Требуется определить в заданном массиве номер самого левого и самого правого элемента,
# равного искомому числу.
#
# Формат ввода
# В первой строке вводится одно натуральное число N, не превосходящее 10^5:
# количество чисел в массиве. Во второй строке вводятся N натуральных чисел,
# не превосходящих 10^9, каждое следующее не меньше предыдущего.
# В третьей строке вводится количество искомых чисел M – натуральное число,
# не превосходящее 10^6. В четвертой строке вводится M натуральных чисел,
# не превосходящих 10^9.
#
# Формат вывода
# Для каждого запроса выведите в отдельной строке через пробел два числа:
# номер элемента самого левого и самого правого элементов массива,
# равных числу-запросу. Элементы массива нумеруются с единицы.
# Если в массиве нет такого числа, выведите в соответствующей строке два
# нуля, разделенных пробелом.
# Решаем двумя бинарными поисками первый  >= x, второй  > x

## Надо учесть ситуацию когда мы не находим элементы = х
## но находим элементы больше и меньше искомого
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

def countx(seq, x):
    indexgt = findfirst(seq, x, checkisgt)
    indexge = findfirst(seq, x, checkisge)
    return indexgt - indexge, indexge

with open('input.txt') as f:
    n = int(f.readline())
    nums = list(map(int, f.readline().split()))
    m = int(f.readline())
    reqs = list(map(int, f.readline().split()))

ans = []
for req in reqs:
    # первый индекс и ко-во элементов х
    cnt, first = countx(nums, req)
    if (cnt == 0) or (first == n):
        ans.append((0, 0))
    else:
        ans.append((first + 1, first + cnt))
print('\n'.join(str(x) + ' ' + str(y) for (x, y) in ans))