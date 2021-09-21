# Август и Беатриса играют в игру. Август загадал натуральное
# число от 1 до n. Беатриса пытается угадать это число, для
# этого она называет некоторые множества натуральных чисел.
# Август отвечает Беатрисе YES, если среди названных ей чисел
# есть задуманное или NO в противном случае. После нескольких
# заданных вопросов Беатриса запуталась в том, какие вопросы
# она задавала и какие ответы получила и просит вас помочь
# ей определить, какие числа мог задумать Август.
# Формат ввода
# Первая строка входных данных содержит число n — наибольшее число,
# которое мог загадать Август. Далее идут строки, содержащие вопросы
# Беатрисы. Каждая строка представляет собой набор чисел, разделенных
# пробелами. После каждой строки с вопросом идет ответ Августа:
# YES или NO. Наконец, последняя строка входных данных содержит
# одно слово HELP.
# Формат вывода
# Вы должны вывести (через пробел, в порядке возрастания)
# все числа, которые мог задумать Август.

# я сначала не учла, что среди названных монжеств
# с ответом YES могут содержаться подмножества
# N = int(input())
# numbers_include = set()
# numbers_exclude = set()
# current_list = []
# input_string = ''
# surrender = False
# while not surrender:
#     input_string = input()
#     if input_string == 'HELP':
#         surrender = True
#     else:
#         current_ans = input()
#         current_list = list(map(int, input_string.strip().split()))
#         if current_ans == 'YES':
#             if numbers_include:
#                 numbers_include = numbers_include.intersection(current_list)
#             else:
#                 numbers_include.update(current_list)
#         else:
#             numbers_exclude.update(current_list)
# answer = []
# if numbers_include:
#     answer = sorted(list(numbers_include - numbers_exclude))
# else:
#     for i in range(N):
#         if i + 1 not in numbers_exclude:
#             answer.append(i + 1)
#
# print(' '.join(str(e) for e in answer))

# Решение с разбора
N = int(input())
possible = set(range(1, N + 1))
s = input().strip()
while s != 'HELP':
    nums = set(map(int, s.split()))
    s = input().strip()
    if s == 'YES':
        possible.intersection_update(nums)
    else:
        possible.difference_update(nums)
    s = input().strip()
print(*sorted(possible))

'''
4
1 2 3
YES
1 2
YES
HELP

10
1 2 3 4 5 6 7 8 9 10
YES
1
NO
2
NO
3
NO
4
NO
6
NO
7
NO
8
NO
9
NO
10
NO
HELP

10
1 2 3 4 5
YES
2 4 6 8 10
NO
HELP
'''