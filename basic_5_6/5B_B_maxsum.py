# В этой задаче вам требуется найти непустой отрезок массива с максимальной суммой.
# Формат ввода
# В первой строке входных данных записано единственное число
# n (1≤n≤3⋅10^5) -  размер массива.
# Во второй строке записано n целых чисел ai (−10^9≤ai≤10^9) - сам массив.
#
# Формат вывода
# Выведите одно число - максимальную сумму на отрезке в данном массиве.

def countmaxrangesum_n(nums, n):
    # сначала посчитаем префиксные суммы
    prefixsum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
    # теперь в цикле перебираем правую границу массива
    # заодно определяем минимальную пр сумму для уже пройденных эл-тов слева
    min_sum_l = min(prefixsum[0], prefixsum[1])
    max_sum = prefixsum[1]
    for i in range(2, n + 1):
        min_sum_l = min(min_sum_l, prefixsum[i - 1])
        max_sum = max(max_sum, prefixsum[i] - min_sum_l)
    return max_sum

def countmaxrangesum_n1(nums, n):
    prefixsum = [0] * (n + 1)
    prefixsum[1] = nums[0]
    min_sum_l = min(prefixsum[0], prefixsum[1])
    max_sum = prefixsum[1]
    for i in range(2, n + 1):
        prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
        min_sum_l = min(min_sum_l, prefixsum[i - 1])
        max_sum = max(max_sum, prefixsum[i] - min_sum_l)
    return max_sum

with open('input.txt') as f:
    n = int(f.readline())
    nums = list(map(int, f.readline().split()))
m = countmaxrangesum_n1(nums, n)
print(m)

# n = int(input())
# nums = list(map(int, input().split()))
#prefixsum = makeprefixsums(nums)
# import time
# start_time = time.time()


# print("time elapsed: {:.9f}s".format(time.time() - start_time))
#001994133s
'''
input
4
-1 -2 -3 -4
output
-1

input
3
100 -2 200
output 
298

input
9
2 3 -5 6 -7 8 9 -10 9
output
17

input
90
875248554 -445604143 437481928 -107163827 204210939 -487333955 222556725 -542481071 289724715 194469276 -141817133 474647116 -954169892 885929374 57632207 -227363757 483824136 -721773915 25701106 -482248053 -931511936 -926263475 404345735 -115296255 192686903 -906528483 -365222860 -915260683 -487463533 -482724370 823558524 757039438 -102417727 -904310905 12518353 -182886592 410915763 657491967 168927268 -865551273 -883478932 713844062 203564572 310342934 211943541 812330376 -106448255 -3679447 -369473910 -103337248 432370585 443724916 820978569 -826824380 549190738 419644757 296316809 -938175406 -166260290 687778869 36536643 -22107249 -800829063 -384654148 761507824 706237557 -746131101 -860259976 -123816837 -154706365 947169247 335764523 -656003919 -972830086 448437059 -918626907 978844381 -354066401 -520576954 912502631 12767561 765334613 -878039201 -218117293 615420988 -181594920 -845202007 -883773820 -187704248 271152230 
output
3804488619 (41 - 56)

input
8
9 -2 -1 -4 -6 9 1 -8
output
10

input
7
8 -1 4 6 9 -5 -8
output
26

input
4
1 2 3 4
output 
10

input
4
5 4 -10 4
output
9

input
5
1 -20 -30 2 0
output
2

input
1
1
output
1

input
1
0
output
0

input
1
-1
output
-1
'''