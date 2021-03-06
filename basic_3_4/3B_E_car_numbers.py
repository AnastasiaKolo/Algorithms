# Неизвестный водитель совершил ДТП и скрылся с места происшествия.
# Полиция опрашивает свидетелей. Каждый из них говорит, что запомнил
# какие-то буквы и цифры номера. Но при этом свидетели не помнят порядок
# этих цифр и букв. Полиция хочет проверить несколько подозреваемых
# автомобилей. Будем говорить, что номер согласуется с показанием
# свидетеля, если все символы, которые назвал свидетель,
# присутствуют в этом номере (не важно, сколько раз).
#
# Формат ввода
# Сначала задано число M<=100 - количество свидетелей. Далее идет M строк, каждая
# из которых описывает показания очередного свидетеля. Эти строки непустые
# и состоят из не более чем 20 символов. Каждый символ в строке - либо цифра,
# либо заглавная латинская буква, причём символы могут повторяться.
# Затем идёт число N<=1000 - количество номеров. Следующие строки представляют из
# себя номера подозреваемых машин и имеют такой же формат, как и показания свидетелей.
#
# Формат вывода
# Выпишите номера автомобилей, согласующиеся с максимальным количеством свидетелей.
# Если таких номеров несколько, то выведите их в том же порядке, в котором они были заданы на входе.
def input_list_of_lists():
    len_list = int(input())
    input_list = [[] for _ in range(len_list)]
    for i in range(len_list):
        input_list[i] = list(input())
    return len_list, input_list

def count_similar_number(m, list_m, n, list_n):
    cnt = [0] * n
    for i in range(n):
        for j in range(m):
            if set(list_m[j]).issubset(set(list_n[i])):
                cnt[i] += 1
    return cnt


M, witness_list = input_list_of_lists()
N, plates_list = input_list_of_lists()

ans = count_similar_number(M, witness_list, N, plates_list)
max_number = max(ans)
for i in range(N):
    if ans[i] == max_number:
        print(''.join(plates_list[i]))


# решение с разбора отличается тем, что он делал список сетов из показаний   свиделетей
m = int(input())
wits = []
for _ in range(m):
    wits.append(set(input().strip()))
n = int(input())
nums = []
maxwitcnt = 0
for i in range(n):
    num = input().strip()
    numset = set(num)
    witcnt = 0
    for wit in wits:
        if wit <= numset:
            witcnt += 1
    nums.append((num, witcnt))
    maxwitcnt = max(maxwitcnt, witcnt)
ans = []
for num in nums:
    if num[1] == maxwitcnt:
        ans.append(num[0])
print('/n'.join(ans))

'''-------------------------
ввод-------------------------
3
ABC
A37
BCDA
2
A317BD
B137AC

ответ-------------------------
B137AC
'''

'''-------------------------
ввод-------------------------
2
1ABC
3A4B
3
A143BC
C143AB
AAABC1

ответ-------------------------
A143BC
C143AB

'''

'''
ввод

ответ
'''