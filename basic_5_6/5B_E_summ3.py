# Даны три массива целых чисел A,B,C и целое число S.
# Найдите такие i,j,k, что Ai+Bj+Ck=S.
#
# Формат ввода
# На первой строке число S (1≤S≤10^9). Следующие три строки содержат описание массивов
# A,B,C в одинаковом формате: первое число задает длину n соответствующего массива
# (1≤n≤15000), затем заданы n целых чисел от 1 до 10^9 — сам массив.
# Формат вывода
# Если таких i,j,k не существует, выведите единственное число−1.
# Иначе выведите на одной строке три числа —i,j,k. Элементы массивов нумеруются с нуля.
# Если ответов несколько, выведите лексикографически минимальный.

def input_list_tuples():
    lst = []
    list_input = list(map(int, input().split()))
    for ai in range(1, list_input[0] + 1):
        lst.append((list_input[ai], ai - 1))
    return sorted(lst), list_input[0]

S = int(input())
A, len_A = input_list_tuples()
B, len_B = input_list_tuples()
C = list(map(int, input().split()))
set_C = set(C[1:])
ans = []
i = 0
found = False
while (i <= len_A - 1) and (A[i][0] <= S) and not found:
    j = 0
    while (j <= len_B - 1) and (B[j][0] <= S) and not found:
        x = S - A[i][0] - B[j][0]
        if x in set_C:
            ans.append((A[i][1], B[j][1], C[1:].index(x)))
            found = True
        j += 1
    i += 1


ans.sort()
if len(ans) > 0:
    print(' '.join(str(i) for i in ans[0]))
else:
    print(-1)


'''
input
6
2 2 1
2 2 2
2 2 4
output
0 0 0


input
3
2 1 2
2 3 1
2 3 1
output
0 1 1


input
10
1 5
1 4
1 3
output
-1

input
5
4 1 2 3 4
3 5 2 1
4 5 3 2 2
output
0 1 2

'''